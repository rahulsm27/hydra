from dataclasses import dataclass


from omegaconf import DictConfig, OmegaConf
import hydra
from hydra.core.config_store import ConfigStore

@dataclass
class ExperimentConfig:
    model = "resnet18"
    nrof_epochs  = 30

@dataclass
class LossConfig:
    model  = "archface"
    nrof_typepochs  = 30

@dataclass
class MyConfig:
    training  = ExperimentConfig()
    loss  = LossConfig()

# need to register our config in hyrda
cs = ConfigStore.instance()
cs.store(name='config',node=MyConfig)

@hydra.main(config_path = None, config_name ='config',version_base = None)
def main(config : DictConfig)-> None:
    print(OmegaConf.to_yaml(config))

if __name__ == "__main__":
    main()

