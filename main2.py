from omegaconf import DictConfig, OmegaConf
import hydra


def main() -> None:
    
    config= OmegaConf.load("./config.yaml")
    print(OmegaConf.to_yaml(config))
    print("batch_Size" , config.training.lr) # using dot
    print("lr ",config.training.lr) # using lr

# to make some value mandtory use ??? against the paramter in config

if __name__ == "__main__":
    main()