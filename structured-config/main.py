from dataclasses import dataclass


from omegaconf import DictConfig, OmegaConf
import hydra
from hydra.core.config_store import ConfigStore

@dataclass
class ExperimentConfig:
    model: str = "resnet18"
    nrof_epochs: int  = 30

@dataclass
class LossConfig:
    model: str  = "archface"
    nrof_typepochs: int  = 30

@dataclass
class MyConfig:
    training: ExperimentConfig  = ExperimentConfig
    loss: LossConfig  = LossConfig

# need to register our config in hyrda
cs = ConfigStore.instance()
cs.store(name='config',node=MyConfig)

@hydra.main(config_path = None, config_name ='config',version_base = None)
def main(config : DictConfig)-> None:
    print(OmegaConf.to_yaml(config))

if __name__ == "__main__":
    main()

