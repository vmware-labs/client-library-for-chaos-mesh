import random

import time

from client import *
from k8s.selector import *

client = ChaosMeshClient()
selector = Selector(labelSelectors={"app": "filebeat"})

# -- Pod failure experiment --

# name of the experiment
exp_name = "filebeat-pod-failure-" + random.randint(0, 1000000).__str__()

# starting up the pod failure experiment
client.start(Experiment.POD_FAILURE, namespace="default", name=exp_name, selector=selector)
time.sleep(10)

# pausing the experiment
client.pause(Experiment.POD_FAILURE, namespace="default", name=exp_name)

# -- Pod kill experiment --

exp_name = "filebeat-pod-kill-" + random.randint(0, 1000000).__str__()

# starting up the pod kill experiment
client.start(Experiment.POD_KILL, namespace="default", name=exp_name, selector=selector)
time.sleep(10)

# pausing the experiment
client.pause(Experiment.POD_KILL, namespace="default", name=exp_name)

# -- Container kill experiment --

exp_name = "filebeat-container-kill-" + random.randint(0, 1000000).__str__()

# starting up the pod kill experiment
client.start(Experiment.CONTAINER_KILL, namespace="default", name=exp_name, selector=selector, container_names=['main'])
time.sleep(10)

# pausing the experiment
client.pause(Experiment.CONTAINER_KILL, namespace="default", name=exp_name)

# -- Stress CPU experiment --

exp_name = "filebeat-cpu-stress-" + random.randint(0, 1000000).__str__()

# starting up the pod kill experiment
client.start(Experiment.STRESS_CPU, namespace="default", name=exp_name, selector=selector, container_names=['main'])
time.sleep(10)

# pausing the experiment
client.pause(Experiment.STRESS_CPU, namespace="default", name=exp_name)

# -- Stress memory experiment --

exp_name = "filebeat-memory-stress-" + random.randint(0, 1000000).__str__()

# starting up the pod kill experiment
client.start(Experiment.STRESS_MEMORY, namespace="default", name=exp_name, selector=selector, container_names=['main'])
time.sleep(10)

# pausing the experiment
client.pause(Experiment.STRESS_MEMORY, namespace="default", name=exp_name)
