## Overview

Chaos Mesh is an open source cloud-native Chaos Engineering platform. It offers various types of fault simulation and has an enormous capability to orchestrate fault scenarios. Using Chaos Mesh, you can conveniently simulate various abnormalities
that might occur in reality during the development, testing, and production environments and find potential problems in the system. To lower the threshold for a Chaos Engineering project, Chaos Mesh provides you with a visualization operation. You
can easily design your Chaos scenarios on the Web UI and monitor the status of Chaos experiments.

Follow this [documentation](https://chaos-mesh.org/docs/) for the chaos mesh installation steps.

This is a Chaos Mesh client written in Python, which allows you single point of entry to create experiments.

In order to create the Chaos Mesh client you can use the following command:

```python
from chaosclient.chaos_client import ChaosMeshClient, Experiment
from chaosclient.k8s import Selector

client = ChaosMeshClient()
selector = Selector(labelSelectors={"app": "filebeat"}, namespaces=None, pods=None)
```

It supports following experiments:

### Pod Fault

The library supports the following Pod fault

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

The library supports the following Pod stress tests

- cpu
- memory

#### CPU

In order to create the stress cpu experiment you can use the following command

```python
exp_name = str(uuid.uuid4())

# starting up the pod kill experiment
client.start(Experiment.POD_STRESS_CPU, namespace="default", name=exp_name, selector=selector, container_names=['main'])
```

#### Memory

In order to create the stress memory experiment you can use the following command

```python
exp_name = str(uuid.uuid4())

# starting up the pod kill experiment
client.start(Experiment.POD_STRESS_MEMORY, namespace="default", name=exp_name, selector=selector, container_names=['main'])
```

### JVM Fault
The library supports the following JVM fault

- GC
- Exception

#### GC

In order to create the GC experiment you can use the following command

```python
# name of the experiment
exp_name = str(uuid.uuid4())

client.start(Experiment.GC, namespace="default", name=exp_name, selector=selector, port=8080)
```

#### Exception

In order to create the Exception experiment you can use the following command

```python
exp_name = str(uuid.uuid4())

client.start(Experiment.RAISE_EXCEPTION, namespace="default",
             name=exp_name, selector=selector, targetClass="com.vmware.Main", method="save",
             exception="java.lang.Exception", port=8080)
```

### Host stress

The library supports the following Host fault

- cpu
- memory

#### CPU

In order to create the stress cpu experiment you can use the following command

```python
exp_name = str(uuid.uuid4())

# starting up the host cpu stress experiment
client.start(Experiment.HOST_STRESS_CPU, namespace="default", name=exp_name,
             address=["10.225.66.224", "10.225.67.213", "10.225.66.231", "10.225.66.138", "10.225.66.192", "10.225.67.52", "10.225.67.103"],
             load=1000)
```

#### Memory

In order to create the stress memory experiment you can use the following command

```python
exp_name = str(uuid.uuid4())

# starting up the host memory stress experiment
client.start(Experiment.HOST_STRESS_MEMORY, namespace="default", name=exp_name,
             address=["10.225.66.224", "10.225.67.213", "10.225.66.231", "10.225.66.138", "10.225.66.192", "10.225.67.52", "10.225.67.103"],
             size="30GB")
```


### Pausing a running experiment

In order to pause an experiment you can use the following command

```python
# pausing the experiment
client.pause(Experiment.POD_STRESS_MEMORY, namespace="default", name=exp_name)
```
