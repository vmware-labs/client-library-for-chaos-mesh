import uuid

import time

from src.python.client import ChaosMeshClient, Experiment
from src.python.selector import Selector

client = ChaosMeshClient()
selector = Selector(labelSelectors={"app": "filebeat"})

# -- Pod failure experiment --

# name of the experiment
exp_name = str(uuid.uuid4())

# starting up the pod failure experiment
client.start(Experiment.POD_FAILURE, namespace="default", name=exp_name, selector=selector)
time.sleep(10)

# pausing the experiment
client.pause(Experiment.POD_FAILURE, namespace="default", name=exp_name)

# -- Pod kill experiment --

exp_name = str(uuid.uuid4())

# starting up the pod kill experiment
client.start(Experiment.POD_KILL, namespace="default", name=exp_name, selector=selector)
time.sleep(10)

# pausing the experiment
client.pause(Experiment.POD_KILL, namespace="default", name=exp_name)

# -- Container kill experiment --

exp_name = str(uuid.uuid4())

# starting up the pod kill experiment
client.start(Experiment.CONTAINER_KILL, namespace="default", name=exp_name, selector=selector, container_names=['main'])
time.sleep(10)

# pausing the experiment
client.pause(Experiment.CONTAINER_KILL, namespace="default", name=exp_name)
