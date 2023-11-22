
# To use varialbes in config use ${}
user:
  home : $(oc.env:USER)

# To use environment vairalbe use oc.
server :
  ip : 1.2.1.2
  port : 80
host:
  hostip : https://${server.ip}:${server.port}

# Grouped config to experiment with differnt config
#helps to select different config file using below cli
# create experimetns folder with different config file
# create config.yaml 
#python main.py +experiments=experiment-with-resnet50
# We can default config in config.yaml
# defaults:
#   - experiments : experiment-with-resnet18 # '- ' before experimientsis list item


# Multirun  -run same file with different config files
python main.py -m experiment=experiment-with-resnet18,experiment-with-resent 50


#output -hydra creates output folder and stores the paramters we used to run.


#logging hydra enables logging. we need to decalare logger and logging message.

#debugging..it will print the config on command line
python main.py --cfg job

#instantiate function
# to select different parts of code for experimentation during run
# instantiate different classes using config file and differnt parameters using config file