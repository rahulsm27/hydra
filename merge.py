from omegaconf import DictConfig, OmegaConf


def main() -> None:
    config_to_merge1 = OmegaConf.load('./merge1.yaml')
    config_to_merge2 = OmegaConf.load('./merge2.yaml')
    config = OmegaConf.merge(config_to_merge1,config_to_merge2)
    print(OmegaConf.to_yaml(config))

if __name__ == "__main__":
    main()