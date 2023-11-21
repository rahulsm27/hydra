from omegaconf import DictConfig, OmegaConf
import hydra
import os

def main() -> None:
    os.environ["USER"] = "rahul"
    config= OmegaConf.load(".environment-variable-config.yaml")
    print(OmegaConf.to_yaml(config))
    print(OmegaConf.to_yaml(config,resolve=True))

# to make some value mandtory use ??? against the paramter in config

if __name__ == "__main__":
    main()