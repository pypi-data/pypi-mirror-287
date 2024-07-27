#
# Created on Sun Mar 31 2024
# Copyright (c) 2024 Huy Truong
# ------------------------------
# Purpose: Simple Trainer
# ------------------------------
#
from typing import Callable, Protocol, Union, Type
from torch.nn.modules import Module
from gentraframe.utils import *
from gentraframe.config import TrainConfig, GTConfig
from gentraframe.gradient_clipping import GradientClipping
from gentraframe.gen_random_mask_v8 import generate_batch_mask
from torch_geometric.loader import DataLoader
import torch
import torch.nn.functional as F
from datetime import datetime
import wandb
import os
import time
import numpy as np
from torch_geometric.data import Dataset 
from abc import abstractmethod
class TrainerConfig(GTConfig):
    models: list[torch.nn.Module ]
    datasets : list[Dataset] 
    task: Literal['supervised','semi']

class Trainer:
    @abstractmethod
    def forward_fn(self, models: list[torch.nn.Module], data: Data, batch_mask: Optional[torch.Tensor] = None) -> Any:
        pass
    
    def train_one_epoch(self, models: list[torch.nn.Module],
                        optimizer: torch.optim.Optimizer, 
                        loader: DataLoader,
                        criterion : Callable, 
                        metric_fn_dict: dict[str, Callable],
                        config : TrainConfig, 
                        task: str, **kwargs ) -> tuple[float, dict, Any]:  
        #edge_attrs = config.use_data_edge_attrs.split(',') if config.use_data_edge_attrs is not None else None
        device = config.device if config.device == 'cuda' and torch.cuda.is_available() else 'cpu'
        mask_rate = config.mask_rate
        use_data_batch = config.use_data_batch
        for pt in models:
            pt.train()
        
        len_loader_dataset = len(loader.dataset) # type:ignore
        total_loss = 0
        total_metric_dict = {k: 0 for k in metric_fn_dict.keys()}

        for data in loader:  # Iterate in batches over the training dataset.
            optimizer.zero_grad()  # Clear gradients.
            
            if task == 'semi':
                num_nodes = torch.unique(data.batch, return_counts=True)[1]
                batch_mask = generate_batch_mask(num_nodes=num_nodes,
                                                edge_index=data.edge_index,
                                                mask_rate=mask_rate,
                                                required_mask=None) #type:ignore
            else:
                batch_mask = data.mask if hasattr(data,'mask') else None

            data.x = data.x.to(device)
            data.y = data.y.to(device)
            
            data.edge_attr = data.edge_attr.to(device) if 'edge_attr' in data else None
            data.batch = data.batch.to(device) if use_data_batch else None
            data.edge_index = data.edge_index.to(device)

            if task == 'semi':
                data.x[batch_mask] =  0
                out = self.forward_fn(models=models, data=data, batch_mask=batch_mask)
                y_pred = apply_masks(out, [batch_mask]) #out[batch_mask] #type:ignore
                y_true = data.y[batch_mask]
            else:
                data.x = data.x
                out = self.forward_fn(models=models, data=data, batch_mask=batch_mask)
                y_pred = out[batch_mask] if batch_mask is not None else out
                y_true = data.y 


            tr_loss = criterion(y_pred, y_true)
            tr_loss.backward()  # Derive gradients.
            optimizer.step()  # Update parameters based on gradients.

            #forward target
            with torch.no_grad():
                total_loss += float(tr_loss) * data.num_graphs
                y_pred_rescaled = y_pred
                y_true_rescaled = y_true
                
                for k, fn in metric_fn_dict.items():
                    computed_metric = fn(y_pred_rescaled, y_true_rescaled)
                    total_metric_dict[k] += computed_metric * data.num_graphs

        
        with torch.no_grad():
            metric_dict = {k : total_metric_dict[k] / len_loader_dataset for k in total_metric_dict.keys() }
            return total_loss /len_loader_dataset, metric_dict, out
    
    def test_one_epoch(self, models: list[torch.nn.Module],
                        loader: DataLoader,
                        criterion : Callable, 
                        metric_fn_dict: dict[str, Callable],
                        config: TrainConfig,
                        task:str,**kwargs) -> tuple[float, dict]:  
        device = config.device if config.device == 'cuda' and torch.cuda.is_available() else 'cpu'
        #edge_attrs = config.use_data_edge_attrs.split(',') if config.use_data_edge_attrs is not None else None
        
        mask_rate = config.mask_rate
        use_data_batch = config.use_data_batch

        for pt in models:
            pt.eval()
        
        with torch.no_grad():
            total_loss = 0
            total_metric_dict = {k: 0 for k in metric_fn_dict.keys()}
            len_loader_dataset = len(loader.dataset) # type:ignore
            for data in loader:
                #assert data.edge_index.max() < data.num_nodes

                if task == 'semi':
                    batch_mask = generate_batch_mask(num_nodes=torch.unique(data.batch, return_counts=True)[1],
                                                    edge_index=data.edge_index,
                                                    mask_rate=mask_rate,
                                                    required_mask=None) #type:ignore
                else:
                    batch_mask = data.mask if hasattr(data,'mask') else None

                data.x = data.x.to(device)
                data.y = data.y.to(device)

                data.edge_attr = data.edge_attr.to(device) if 'edge_attr' in data else None
                data.batch = data.batch.to(device) if use_data_batch else None
                data.edge_index = data.edge_index.to(device)

                if task == 'semi':
                    data.x[batch_mask] = 0
                    out = self.forward_fn(models=models, data=data, batch_mask=batch_mask)
                    y_pred = apply_masks(out, [batch_mask]) #type:ignore
                    y_true = data.y[batch_mask]
                else:
                    out = self.forward_fn(models=models, data=data, batch_mask=batch_mask)
                    y_pred = out[batch_mask] if batch_mask is not None else out
                    y_true = data.y 

                val_loss = criterion(y_pred, y_true)
                #update metrics
                y_pred_rescaled = y_pred
                y_true_rescaled = y_true
                total_loss += float(val_loss) * data.num_graphs
                for k, fn in metric_fn_dict.items():
                    computed_metric = fn(y_pred_rescaled, y_true_rescaled)
                    total_metric_dict[k] += computed_metric * data.num_graphs

            
            metric_dict = {k : total_metric_dict[k] / len_loader_dataset for k in total_metric_dict.keys() }
            return total_loss / len_loader_dataset, metric_dict

    def as_dict(self, args: TrainConfig) -> dict:

        merged_config = args.as_dict()
        #if self.pl_config is not None:
        #    merged_config.update( self.pl_config.as_dict())
        
        return merged_config
    
    def load(self, models: list[torch.nn.Module], model_path: str, device:str, do_load: bool) -> list[torch.nn.Module] :
        #TODO: model loading should belong to ModelBuilder
        model_names = [ model.name if hasattr(model,'name') else type(model).__name__ for model in models]  #type:ignore
        
        ret_models = []
        for i, m in enumerate(models):
            model : torch.nn.Module = m  #type:ignore
            model_name= model_names[i]
            print(f'#######{model_name}#########')
            print(model)
            print("Model parameters: ", sum(p.numel() for p in model.parameters()))
            
            if do_load:
                if model_path is None :
                    print(f'model_path keys are not found! Please distinguish model path from save_path folder! We use a new model!')
                elif not os.path.exists(model_path):
                    raise FileNotFoundError(f'{model_path} file is not found')
                else:
                    model, cp_dict = load_checkpoint(path=model_path,
                                            model=model,
                                            load_key=getattr(model, 'name'),)
                    
            model = model.to(device, non_blocking=True)
            ret_models.append(model)
        return ret_models

    
    def start_profiler(self, run_prefix: str, task: str, model_name:str, save_path:str, project_name: str, arg_dict: dict, log_method: str='')-> tuple[str,str]:
        """start wandb
        Returns:
            str: run name
        """
       

        postfix = datetime.today().strftime('%Y%m%d_%H%M')
        run_name = f'{run_prefix}+{task}+{model_name}+{postfix}'
        
        # start a new wandb run to track this script
        if log_method == 'wandb':
            wandb.init(
                # set the wandb project where this run will be logged
                project=project_name, 
                name = run_name,
                # track hyperparameters and run metadata
                config= arg_dict,
                settings=None,
            )

        os.makedirs(save_path,exist_ok=True)

        return run_name, postfix
    
   

    def get_inpout_config(self)-> Optional[GTConfig]:  #type:ignore
        """return the input output config"""
        return TrainerConfig()
    
    def get_train_loader(self, datasets : list[Dataset],train_args: TrainConfig,**kwargs) -> DataLoader:
        return DataLoader(datasets[0], batch_size=train_args.batch_size, shuffle=True) #type:ignore
    
    def get_val_loader(self, datasets : list[Dataset],train_args: TrainConfig, **kwargs) -> DataLoader:
        return DataLoader(datasets[1], batch_size=train_args.batch_size, shuffle=True) #type:ignore
    
    def get_test_loader(self, datasets : list[Dataset],train_args: TrainConfig, **kwargs) -> DataLoader:
        return DataLoader(datasets[-1], batch_size=train_args.batch_size, shuffle=True) #type:ignore
    

    def get_optimizer(self, models: list[torch.nn.Module ], train_args: TrainConfig, **kwargs) -> torch.optim.Optimizer:
        if len(models) == 1:
            optimizer = torch.optim.Adam(models[0].parameters(), lr=train_args.lr, weight_decay=train_args.weight_decay)
        else:
            param_groups = [{'params': (p for n, p in model.named_parameters())} for model in models]
            optimizer = torch.optim.Adam(param_groups, lr=train_args.lr, weight_decay=train_args.weight_decay) #TODO: add eps
        return optimizer

    def get_train_metric_fn_dict(self, task: str, **kwargs) -> dict:
        return get_metric_fn_collection(prefix='train', task = task) #type:ignore
    
    def get_val_metric_fn_dict(self, task: str, **kwargs) -> dict:
        return  get_linear_probing_metric_fn_collection(prefix='val', task = task) #type:ignore
    
    def get_test_metric_fn_dict(self, task: str, **kwargs) -> dict:
        return  get_linear_probing_metric_fn_collection(prefix='test', task = task) #type:ignore

    def get_scheduler(self, **kwargs) -> Optional[Any]:
        return None

    def run(self, inpout: Type[TrainerConfig],  outputs: list[str], config: TrainConfig, **kwargs) -> Union[dict[str,Any], tuple, Any]:
        models : list[torch.nn.Module ]= inpout.models
        datasets : list[Dataset] = inpout.datasets
        task= inpout.task

        train_args = config
        model_path = config.model_path
        do_load = config.do_load

        #check conditions
        assert models is not None and len(models) > 0
        assert datasets is not None and len(datasets) >= 2

        #setup some configs
        #edge_attrs = train_args.use_data_edge_attrs.split(',') if train_args.use_data_edge_attrs is not None else None
        
        train_loader = self.get_train_loader(datasets, train_args=train_args, **kwargs)
        valid_loader = self.get_val_loader(datasets, train_args=train_args,  **kwargs)

        device = train_args.device if train_args.device == 'cuda' and torch.cuda.is_available() else 'cpu'
        model_names = [ model.name if hasattr(model,'name') else type(model).__name__ for model in models] #type:ignore
        setattr(train_args, 'model_name', '+'.join(model_names) )
        run_name, postfix = self.start_profiler(run_prefix= train_args.run_prefix,
                                                task=task, 
                                                model_name=getattr(train_args,'model_name'), 
                                                save_path=train_args.save_path, 
                                                project_name= train_args.project_name,
                                                arg_dict=train_args.as_dict(), 
                                                log_method=train_args.log_method)  #self.start_profiler(task=task, args=train_args)
        
        models = self.load(models, model_path= model_path, device=device, do_load= do_load)
        print('#'*80)
        print(self.as_dict(train_args))
        print('#'*80)
        if task == 'semi':
            print(f'gen-mask version: {generate_batch_mask.__module__}')

        # get loss fn
        criterion = get_criterion(train_args.criterion, device= device)
        
        # feed models into optimizer
        optimizer = self.get_optimizer(models,train_args,**kwargs)
        
        # gather metrics
        train_metric_fn_dict= self.get_train_metric_fn_dict(task=task,**kwargs) #get_metric_fn_collection(prefix='train', task = task) 
        val_metric_fn_dict=  self.get_val_metric_fn_dict(task=task,**kwargs) #get_linear_probing_metric_fn_collection(prefix='val', task = task)
       
        # define scheduler and gradient clipping
        scheduler = self.get_scheduler(**kwargs)
        #grad_clipper = GradientClipping(percentile=10) if train_args.use_gradient_clipping else None
    

        #intial records
        best_loss = np.inf
        best_error = np.inf
        best_acc = 0
        best_epoch = 0
        
        start_time = time.time()
        dt1 = datetime.fromtimestamp(start_time)
        print('Start time:', dt1)
        print("*" * 80)

        #############
        #TODO: norm configs should be defined here
        ############
        best_model_path= ''
        last_model_path= ''
        for epoch in range(1, train_args.epochs + 1):
            tr_loss, tr_metric_dict, out = self.train_one_epoch(models=models,
                                                        optimizer=optimizer , 
                                                        loader=train_loader,
                                                        criterion= criterion, 
                                                        metric_fn_dict = train_metric_fn_dict,
                                                        config=config,
                                                        task =task,
                                                        **kwargs 
                                                        )
            
            val_loss, val_metric_dict = self.test_one_epoch(models=models,
                                                        loader= valid_loader,
                                                        criterion= criterion, 
                                                        metric_fn_dict = val_metric_fn_dict,
                                                        config = config,
                                                        task =task,
                                                        **kwargs 
                                                        )
            
            
            if val_loss < best_loss:
                best_loss = val_loss
                best_metric_dict = val_metric_dict
                best_epoch = epoch
                # save training_checkpoint
                best_model_path = os.path.join(config.save_path,f"best_{getattr(train_args,'model_name')}_{postfix}.pth")
                save_kwargs= dict(
                    path= best_model_path,
                    optimizer_state_dict=optimizer.state_dict() if optimizer else None, 
                    epoch=best_epoch, 
                    loss=best_loss, 
                    val_metric_dict = best_metric_dict, 
                    #edge_attrs=edge_attrs,
                    norm_type=train_args.norm_type, 
                )

                for model in  models:
                    save_kwargs.update({ getattr(model,'name'):  model.state_dict()})
                save_checkpoint(**save_kwargs) #type:ignore

            if (epoch == 1 or (epoch % train_args.log_per_epoch) == 0 ) and not math.isnan(tr_loss):
                print_metrics(epoch=epoch,
                        tr_loss=tr_loss, 
                        val_loss=val_loss,
                        tr_metric_dict=tr_metric_dict, 
                        val_metric_dict=val_metric_dict,
                        )
                last_model_path=os.path.join(config.save_path,f"last_{getattr(train_args,'model_name')}_{postfix}.pth")
                save_kwargs= dict(
                    path= last_model_path,
                    optimizer_state_dict= optimizer.state_dict() ,   #type:ignore
                    epoch=best_epoch, #type:ignore
                    loss=best_loss,   #type:ignore
                    val_metric_dict = best_metric_dict, 
                    #edge_attrs=edge_attrs,
                    norm_type=train_args.norm_type, 
                )
                for model in  models:
                    save_kwargs.update({ getattr(model,'name'):  model.state_dict()})
                save_checkpoint(**save_kwargs) #type:ignore

            if train_args.log_method == 'wandb':
                log_metrics_on_wandb(epoch=epoch,
                                commit=True,
                                train_loss=tr_loss,
                                val_loss=val_loss,
                                best_loss=best_loss,
                                best_epoch=best_epoch,
                                tr_metric_dict=tr_metric_dict,
                                val_metric_dict=val_metric_dict,
                                )
                
            
            if scheduler is not None:
                scheduler.step(val_loss)  
        
        end_time = time.time()
        dt2 = datetime.fromtimestamp(end_time) 
        print("*" * 80)
        print('End time:', dt2)
        print('Executation time: ', dt2 - dt1)

        if train_args.log_method == 'wandb':
            wandb.finish()
        
        if best_model_path != '':
            model_paths  = [best_model_path]
        else:
            model_paths = [last_model_path]

        return model_paths

class SingleTrainer(Trainer):
    def forward_fn(self, models: list[Module], data: Data, batch_mask: Optional[torch.Tensor] = None) -> Any:
        assert len(models) == 1
        out =  models[0](x=data.x, edge_index=data.edge_index, batch=data.batch, edge_attr=data.edge_attr)
        return out
    
