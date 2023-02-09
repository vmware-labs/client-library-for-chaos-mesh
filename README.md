## Overview

Chaos Mesh is an open source cloud-native Chaos Engineering platform. It offers various types of fault simulation and has an enormous capability to orchestrate fault scenarios. Using Chaos Mesh, you can conveniently simulate various abnormalities
that might occur in reality during the development, testing, and production environments and find potential problems in the system. To lower the threshold for a Chaos Engineering project, Chaos Mesh provides you with a visualization operation. You
can easily design your Chaos scenarios on the Web UI and monitor the status of Chaos experiments.

Follow this [documentation](https://chaos-mesh.org/docs/) for the installation steps.

This is a Chaos Mesh client written in Python, which allows you single point of entry to create experiments.

In order to create the Chaos Mesh client you can use the following command:

```python
from chaos_mesh import ChaosMeshClient
from chaos_mesh import Selector
from chaos_mesh import Experiment

client = ChaosMeshClient()
selector = Selector(labelSelectors={"app": "filebeat"}, namespaces=None, pods=None)
```

It supports following experiments:

### Pod Fault

The pod fault is divided into three categories

- pod failure
- pod kill
- container kill

#### Pod Failure

In order to create the pod failure experiment you can use the following command

```python
# name of the experiment
exp_name = str(uuid.uuid4())

# starting up the pod failure experiment
client.start(Experiment.POD_FAILURE, namespace="default", name=exp_name, selector=selector)
```

#### Pod Kill

In order to create the pod kill experiment you can use the following command

```python
exp_name = str(uuid.uuid4())

# starting up the pod kill experiment
client.start(Experiment.POD_KILL, namespace="default", name=exp_name, selector=selector)
```

#### Container Kill

In order to create the container kill experiment you can use the following command

```python
exp_name = str(uuid.uuid4())

# starting up the pod kill experiment
client.start(Experiment.CONTAINER_KILL, namespace="default", name=exp_name, selector=selector, container_names=['main'])
```

### Stress Test

The stress test is divided into two categories

- cpu
- memory

#### CPU

In order to create the stress cpu experiment you can use the following command

```python
exp_name = str(uuid.uuid4())

# starting up the pod kill experiment
client.start(Experiment.STRESS_CPU, namespace="default", name=exp_name, selector=selector, container_names=['main'])
```

#### Memory

In order to create the stress memory experiment you can use the following command

```python
exp_name = str(uuid.uuid4())

# starting up the pod kill experiment
client.start(Experiment.STRESS_MEMORY, namespace="default", name=exp_name, selector=selector, container_names=['main'])
```

### Pausing a running experiment

In order to pause an experiment you can use the following command

```python
# pausing the experiment
client.pause(Experiment.STRESS_MEMORY, namespace="default", name=exp_name)
```
