# Chaos Mesh Client
## Introduction
Chaos Mesh is an open source cloud-native Chaos Engineering platform that allows you to simulate various faults and orchestrate fault scenarios in your kubernetes cluster. This client is written in Python and provides a single point of entry to create and manage experiments in Chaos Mesh.

## Getting Started
To start using Chaos Mesh, please follow the installation steps in the [documentation](https://chaos-mesh.org/docs/).

To create a Chaos Mesh client, you can use the following code:

```python
from chaosclient.client import ChaosMeshClient, Experiment
from chaosclient.k8s.selector import Selector

# creating the ChaosMesh client
client = ChaosMeshClient()

# target pods selector; by labelSector or by pods in specified namespaces
selector = Selector(labelSelectors={"app": "filebeat"}, pods=None, namespaces=None)
```

## Experiment Types
Chaos Mesh supports various types of experiments, including Pod faults, stress tests, JVM faults, and Host faults.

### Pod Faults
- Pod failure
- Pod kill
- Container kill

### Stress Tests
- CPU
- Memory

### JVM Faults
- GC
- Exception

### Host Faults
- CPU
- Memory

## Experiment Examples
Here are some examples of how you can create experiments in Chaos Mesh:

### Pod Failure Experiment
```python
# name of the experiment
exp_name = str(uuid.uuid4())

# starting up the pod failure experiment
client.start(Experiment.POD_FAILURE, namespace="default", name=exp_name, selector=selector)
```

### Pod Kill Experiment
```python
exp_name = str(uuid.uuid4())

# starting up the pod kill experiment
client.start(Experiment.POD_KILL, namespace="default", name=exp_name, selector=selector)
```

### Container Kill Experiment
```
exp_name = str(uuid.uuid4())

# starting up the pod kill experiment
client.start(Experiment.CONTAINER_KILL, namespace="default", name=exp_name, selector=selector, container_names=['main'])
```

### CPU Stress Test Experiment
```python
exp_name = str(uuid.uuid4())

# starting up the pod kill experiment
client.start(Experiment.POD_STRESS_CPU, namespace="default", name=exp_name, selector=selector, container_names=['main'])
```

### Memory Stress Test Experiment
```python
exp_name = str(uuid.uuid4())

# starting up the pod kill experiment
client.start(Experiment.POD_STRESS_MEMORY, namespace="default", name=exp_name, selector=selector, container_names=['main'])
```

### GC Experiment
```python
# name of the experiment
exp_name = str(uuid.uuid4())

client.start(Experiment.GC, namespace="default", name=exp_name, selector=selector, port=8080)
```

### Exception Experiment
```python
exp_name = str(uuid.uuid4())

client.start(Experiment.RAISE_EXCEPTION, namespace="default",
             name=exp_name, selector=select
```

### Host CPU stress

```python
exp_name = str(uuid.uuid4())

# starting up the host cpu stress experiment
client.start(Experiment.HOST_STRESS_CPU, namespace="default", name=exp_name,
             address=["10.225.66.224", "10.225.67.213", "10.225.66.231", "10.225.66.138", "10.225.66.192", "10.225.67.52", "10.225.67.103"],
             load=1000)
```

### Host Memory stress

```python
exp_name = str(uuid.uuid4())

# starting up the host memory stress experiment
client.start(Experiment.HOST_STRESS_MEMORY, namespace="default", name=exp_name,
             address=["10.225.66.224", "10.225.67.213", "10.225.66.231", "10.225.66.138", "10.225.66.192", "10.225.67.52", "10.225.67.103"],
             size="30GB")
```

## Pause an experiment

In order to pause an experiment you can use the following command

```python
# pausing the experiment
client.pause(Experiment.POD_STRESS_MEMORY, namespace="default", name=exp_name)
```

## Delete the experiment

The experiment can be removed from the k8s cluster using the following command

```python
client.delete(Experiment.POD_STRESS_MEMORY, namespace="default", name=exp_name)
```
