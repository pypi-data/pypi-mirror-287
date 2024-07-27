#
# Created on Wed Jan 23 2024
# Copyright (c) 2024 Huy Truong
# ------------------------------
# Purpose: Store mask generation algorithm
# Version: v8 - random
# Note: It is similar to v7- random, but we add a boolean flag whether we zero required masks from context (i.e., target mask turns off (0) all positions of context that was masked (1))
# ------------------------------
#

import torch
import math
import timeit
from functools import wraps

    
def measure(func, repeat=3, number=10000):
    """Include debug statement and timeit setup"""
    @wraps(func)
    def wrapper(*args,**kwargs):
        res = func(*args,**kwargs)
        times = timeit.repeat(
            stmt=lambda: func(*args,**kwargs),
            repeat=repeat, number=number)
        print(f'The function was run in {repeat} times. The mean execution time is {sum(times)/repeat} seconds.')
        return res
    return wrapper
#@measure
def generate_batch_mask( num_nodes:list[int], mask_rate:float, required_mask: torch.Tensor, do_mask_required_mask=True, **kwargs) -> torch.Tensor:
    assert mask_rate > 0.
    N = sum(num_nodes) 
    #tensor_num_nodes has shape [batch_size]
    cumsum_num_nodes = torch.cumsum(num_nodes,dim=0) #type:ignore
    lbs = torch.nn.functional.pad(cumsum_num_nodes[:-1],[1,0]) #torch.cat([torch.zeros(size=[1]),cumsum_num_nodes[:-1]]) 
    ubs = cumsum_num_nodes
    remaining_nodes = torch.arange(N)

    if required_mask is not None:
        nonzero_inverted_required_mask = (~required_mask).nonzero()
        remaining_nodes = remaining_nodes[nonzero_inverted_required_mask]
       
    def extract_graphs(lb,ub):
        filter_mask = torch.logical_and(remaining_nodes >= lb, remaining_nodes < ub)  
        segment = remaining_nodes[filter_mask]
        gap = segment.shape[0]
        mask_num = max(math.floor(gap * mask_rate),1)
        keep_num = gap - mask_num
        permuted_idx = torch.randperm(segment.nelement())[:keep_num]
        permuted_node = segment[permuted_idx]

        return permuted_node
    
    
    keep_nodes = torch.hstack(tuple(map(extract_graphs, lbs, ubs)))

    mask = torch.ones(N, dtype= torch.bool)
    mask[keep_nodes] = 0
    
    if not do_mask_required_mask:
        mask[required_mask.nonzero()] = 0
    return mask

    

    
    

