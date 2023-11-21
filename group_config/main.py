from omegaconf import DictConfig, OmegaConf
import hydra

@hydra.main(config_path="config",config_name="config")
def main(config:DictConfig)-> None:
    print(OmegaConf.to_yaml(config))

if __name__ == "__main__":
    main()

#helps to select different config file using below cli
# create experimetns folder with different config file
# create config.yaml 
#python main.py +experiments=experiment-with-resnet50
