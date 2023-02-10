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
client.start(Experiment.POD_STRESS_CPU, namespace="default", name=exp_name, selector=selector, container_names=['main'])
time.sleep(10)

# pausing the experiment
client.pause(Experiment.POD_STRESS_CPU, namespace="default", name=exp_name)

# -- Stress memory experiment --

exp_name = "filebeat-memory-stress-" + random.randint(0, 1000000).__str__()

# starting up the pod kill experiment
client.start(Experiment.POD_STRESS_MEMORY, namespace="default", name=exp_name, selector=selector, container_names=['main'])
time.sleep(10)

# pausing the experiment
client.pause(Experiment.POD_STRESS_MEMORY, namespace="default", name=exp_name)

# -- JVM raise exception experiment --

exp_name = "jvm-exception-" + random.randint(0, 1000000).__str__()

# starting up the pod kill experiment
client.start(Experiment.RAISE_EXCEPTION, namespace="default",
             name=exp_name, selector=selector, targetClass="com.vmware.Main", method="save",
             exception="java.lang.Exception", port=8080)
time.sleep(10)

# pausing the experiment
client.pause(Experiment.RAISE_EXCEPTION, namespace="default", name=exp_name)

# -- JVM stress GC experiment --

exp_name = "jvm-gc-" + random.randint(0, 1000000).__str__()

# starting up the pod kill experiment
client.start(Experiment.GC, namespace="default", name=exp_name, selector=selector, port=8080)
time.sleep(10)

# pausing the experiment
client.pause(Experiment.GC, namespace="default", name=exp_name)

# -- Hosts stress CPU experiment --

exp_name = "hosts-stress-cpu-" + random.randint(0, 1000000).__str__()

# starting up the pod kill experiment
client.start(Experiment.HOST_STRESS_MEMORY, namespace="default", name=exp_name,
             address=["10.225.66.224", "10.225.67.213", "10.225.66.231", "10.225.66.138", "10.225.66.192", "10.225.67.52", "10.225.67.103"],
             size="30GB")
time.sleep(10)

# pausing the experiment
client.pause(Experiment.HOST_STRESS_MEMORY, namespace="default", name=exp_name)

# -- Hosts stress Memory experiment --

exp_name = "hosts-stress-memory-" + random.randint(0, 1000000).__str__()

# starting up the pod kill experiment
client.start(Experiment.HOST_STRESS_CPU, namespace="default", name=exp_name,
             address=["10.225.66.224", "10.225.67.213", "10.225.66.231", "10.225.66.138", "10.225.66.192", "10.225.67.52", "10.225.67.103"],
             load=1000)
time.sleep(10)

# pausing the experiment
client.pause(Experiment.HOST_STRESS_CPU, namespace="default", name=exp_name)
