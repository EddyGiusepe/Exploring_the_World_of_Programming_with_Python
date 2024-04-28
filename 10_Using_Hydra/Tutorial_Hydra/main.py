#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro
"""
from dataclasses import dataclass
from typing import Any

import hydra
from omegaconf import DictConfig, OmegaConf

import os, logging
logger = logging.getLogger(__name__)

@dataclass
class ImageConfig:
    size: int
    channels: int

@dataclass
class DatasetConfig:
    image: ImageConfig
    classes: int

@dataclass
class MainConfig:
    dataset : DatasetConfig
    feature_extractor: Any
    classifier: Any

cs = hydra.core.config_store.ConfigStore()
cs.store(name="config_schema", node=MainConfig)

@hydra.main(version_base="1.3", config_path='./configs', config_name='config')
def train(cfg: DictConfig):

    # Print the configuration:
    print(OmegaConf.to_yaml(cfg, resolve=True))

    # Log the current working directory:
    logger.info(f'Diretório de Trabalho: {os.getcwd()}')

if __name__=='__main__':
    train()
