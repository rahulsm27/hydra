import hydra
from omegaconf import DictConfig
from hydra.utils import instantiate
import torch


class MyClass:
    def __init__(self,name:str) -> None:
        self.name = name

    def say_hello(self) -> None:
        print(f"Hell {self.name}")

@hydra.main(config_path=".", config_name ="config", version_base=None)
def main(config : DictConfig) -> None:
    my_class = MyClass(name = "Rahul") 
    my_class.say_hello()

    my_class_hdyra = instantiate(config.my_class)
    my_class_hdyra.say_hello()

    # Lets instantiate torch optimizer using hydra

    parameters = torch.nn.Parameter(torch.randn(10,10)) 
    partial_optimizer = instantiate(config.optimizer) # partial optimizer based on only few parameters from config file
    
    optimizer = partial_optimizer([parameters])
    print(optimizer)


if __name__ == "__main__":
    main()


