
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
# using partial we can pass only some parameters from config and some paramters from code. for example adam optimizer

# packages in hdyra # where the content of each input config is place
 in the final config file for grouped packages
PRIORITIES

# Package specified in the default list
# pakcakge specified in the package directive
# default packge of config file itself


# check small project for above concepts


# Structure config - same thing as configy.yaml implemented using classes
# best uses - validate .yaml file using structure config. structure config is used to develop schema. register it..default that schema in the yaml file.

# The @dataclass decorator is a feature introduced in Python 3.7 that simplifies the creation of classes primarily used to store data. It automatically generates special methods, such as __init__, __repr__, and others, based on the class attributes. This can lead to more concise and readable code. Here's a basic guide on how to use the @dataclass decorator:


#pydantic for data type validations
two ways
1.# from pydantic.dataclasse import dataclass
use pydatntic dataclass decorator to declare varaibles
2. using basemdel

from datetime import datetime
from typing import Tuple

from pydantic import BaseModel


class Delivery(BaseModel):
    timestamp: datetime
    dimensions: Tuple[int, int]


m = Delivery(timestamp='2020-01-02T03:04:05Z', dimensions=['10', '20'])
print(repr(m.timestamp))
#> datetime.datetime(2020, 1, 2, 3, 4, 5, tzinfo=TzInfo(UTC))
print(m.dimensions)
#> (10, 20)


# glcoud auth login
# gcloud config set project <projectid>

# Google cloud storge - to store data
# create bucket using ui
copy file
# gsutil cp ./makefile gs://cyberbully_r/makefile
# gsutil cp <file to be copeied> gs://<bucket name>/<filename>
copy dir
# gsutil cp -r <direname> gs://<bucketanme>/

download dir
# gsutil cp -r  gs://<bucketanme>/<dirname> <direname>

# Google compute engine - vm creation.

# security -> scrent manager

# sql


# Artifact registry  -to store docker images
# Create repository on colud - repsoitory name - artifact

# copying docker iamges
# run the commond desplayed on setup instrucitons
gcloud auth configure-docker \
    asia-south1-docker.pkg.dev

rename docker image
 docker tag python:3.8-slim asia-south1-docker.pkg.dev/mlendtoend/artifact/python-image:firsttag
 # docker tag <image name> <host name of repository see above command>/<project name>/<repostory name >/<image name on gcp>:<tag name>



# firewall - allow port tcp for particular instance by creating firewall rule and applying it to instance

#instance groups - multile instances in one group