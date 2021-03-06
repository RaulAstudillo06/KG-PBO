from typing import Callable, Dict, List, Optional

import os
import sys

from src.pbo_trial import pbo_trial


def experiment_manager(
    problem: str,
    obj_func: Callable,
    input_dim: int,
    comp_noise_type: str,
    comp_noise: float,
    algo: str,
    batch_size: int,
    num_init_queries: int,
    num_max_iter: int,
    first_trial: int,
    last_trial: int,
    restart: bool,
    algo_params: Optional[Dict] = None,
    ignore_failures: bool = False,
) -> None:

    for trial in range(first_trial, last_trial + 1):
        pbo_trial(
            problem=problem,
            obj_func=obj_func,
            input_dim=input_dim,
            comp_noise_type=comp_noise_type,
            comp_noise=comp_noise,
            algo=algo,
            algo_params=algo_params,
            batch_size=batch_size,
            num_init_queries=num_init_queries,
            num_max_iter=num_max_iter,
            trial=trial,
            restart=restart,
            ignore_failures=ignore_failures,
        )
