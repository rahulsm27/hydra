from omegaconf import DictConfig, OmegaConf
import hydra


def main() -> None:
    
    config= OmegaConf.load("./variable-interpolation.yaml")
    print(OmegaConf.to_yaml(config))
    print(OmegaConf.to_yaml(config,resolve=True))

# to make some value mandtory use ??? against the paramter in config

if __name__ == "__main__":
    main()