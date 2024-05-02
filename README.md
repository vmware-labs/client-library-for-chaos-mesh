[![Upload Python Package](https://github.com/vmware-labs/client-library-for-chaos-mesh/actions/workflows/python-publish.yml/badge.svg?branch=main)](https://github.com/vmware-labs/client-library-for-chaos-mesh/actions/workflows/python-publish.yml)

# Client Library for Chaos Mesh

## Introduction

Chaos Mesh is an open source cloud-native Chaos Engineering platform that allows you to simulate various faults and orchestrate fault scenarios in your kubernetes cluster. This client is written in Python and provides a single point of entry to
create and manage experiments in Chaos Mesh.

## Getting Started

To start using Chaos Mesh, please follow the installation steps in the [documentation](https://chaos-mesh.org/docs/).

To create a Chaos Mesh client, you can use the following code:

```python
from chaosmesh.client import Client, Experiment
from chaosmesh.k8s.selector import Selector

# creating the ChaosMesh client
client = Client(version="v1alpha1")

# target pods selector; by labelSector or by pods in specified namespaces
selector = Selector(labelSelectors={"app": "filebeat"}, pods=None, namespaces=None)
```

## Supported API Version

- `chaos-mesh.org/v1alpha1`

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

### Host Disk Fault

- Read payload
- Write payload
- Fill

### Network Attack

- Partition
- Bandwidth

## Experiment Examples

Here are some examples of how you can create experiments in Chaos Mesh:

### Pod Failure Experiment

```python
# name of the experiment
exp_name = str(uuid.uuid4())

# starting up the pod failure experiment
client.start_experiment(Experiment.POD_FAILURE, namespace="default", name=exp_name, selector=selector)
```

### Pod Kill Experiment

```python
exp_name = str(uuid.uuid4())

# starting up the pod kill experiment
client.start_experiment(Experiment.POD_KILL, namespace="default", name=exp_name, selector=selector)
```

### Container Kill Experiment

```
exp_name = str(uuid.uuid4())

# starting up the pod kill experiment
client.start_experiment(Experiment.CONTAINER_KILL, namespace="default", name=exp_name, selector=selector, container_names=['main'])
```

### CPU Stress Test Experiment

```python
exp_name = str(uuid.uuid4())

# starting up the pod kill experiment
client.start_experiment(Experiment.POD_STRESS_CPU, namespace="default", name=exp_name, selector=selector, container_names=['main'])
```

### Memory Stress Test Experiment

```python
exp_name = str(uuid.uuid4())

# starting up the pod kill experiment
client.start_experiment(Experiment.POD_STRESS_MEMORY, namespace="default", name=exp_name, selector=selector, container_names=['main'])
```

### GC Experiment

```python
# name of the experiment
exp_name = str(uuid.uuid4())

client.start_experiment(Experiment.GC, namespace="default", name=exp_name, selector=selector, port=8080)
```

### Exception Experiment

```python
exp_name = str(uuid.uuid4())

client.start_experiment(Experiment.RAISE_EXCEPTION, namespace="default",
                        name=exp_name, selector=select
```

### Host CPU stress

```python
exp_name = str(uuid.uuid4())

# starting up the host cpu stress experiment
client.start_experiment(Experiment.HOST_STRESS_CPU, namespace="default", name=exp_name,
                        address=["10.225.66.224", "10.225.67.213", "10.225.66.231", "10.225.66.138", "10.225.66.192", "10.225.67.52", "10.225.67.103"],
                        load=1000)
```

### Host Memory stress

```python
exp_name = str(uuid.uuid4())

# starting up the host memory stress experiment
client.start_experiment(Experiment.HOST_STRESS_MEMORY, namespace="default", name=exp_name,
                        address=["10.225.66.224", "10.225.67.213", "10.225.66.231", "10.225.66.138", "10.225.66.192", "10.225.67.52", "10.225.67.103"],
                        size="30GB")
```

### Host Disk Fault Read payload

```python
exp_name = "disk-fault-read-payload-" + random.randint(0, 1000000).__str__()

# starting up the read payload experiment
client.start_experiment(Experiment.HOST_READ_PAYLOAD, namespace="default", name=exp_name, selector=selector, address=["address"], size="1024K", path="/", payload_process_num=1)
```

### Host Disk Fault Write payload

```python
exp_name = "disk-fault-write-payload-" + random.randint(0, 1000000).__str__()

# starting up the write payload experiment
client.start_experiment(Experiment.HOST_WRITE_PAYLOAD, namespace="default", name=exp_name, selector=selector, address=["address"], size="1024K", path="/",
                        payload_process_num=1)
```

### Host Disk Fill

```python
exp_name = "disk-fault-fill-" + random.randint(0, 1000000).__str__()

# starting up the disk fill experiment
client.start_experiment(Experiment.HOST_DISK_FILL, namespace="default", name=exp_name, selector=selector, address=["address"], size="1024K", path="/", fill_by_fallocate=True)
```

### Network Partition

```python
exp_name = "network-partition-" + random.randint(0, 1000000).__str__()

# starting up the network partition experiment
client.start_experiment(Experiment.NETWORK_PARTITION, namespace="default", name=exp_name, selector=selector, external_targets=["target"], direction="both")
```

### Network Bandwidth

```python
exp_name = "network-bandwidth-" + random.randint(0, 1000000).__str__()

# starting up the network bandwidth experiment
client.start_experiment(Experiment.NETWORK_BANDWIDTH, namespace="default", name=exp_name, selector=selector, rate="1bps", buffer=1, limit=1, direction="to",
                        external_targets=["target"])
```

## Pause an experiment

In order to pause an experiment you can use the following command

```python
# pausing the experiment
client.pause_experiment(Experiment.POD_STRESS_MEMORY, namespace="default", name=exp_name)
```

## Delete the experiment

The experiment can be removed from the k8s cluster using the following command

```python
client.delete_experiment(Experiment.POD_STRESS_MEMORY, namespace="default", name=exp_name)
```

## Schedule experiments

Schedule an experiment using the following command

```python
client.schedule_experiment(Experiment.POD_STRESS_CPU, namespace="default", name=exp_name, cron_schedule="*/2 * * * *", selector=selector, container_names=['main'])
```

## Logging

Initializing the ChaosMesh logger

```python
import logging, sys

logging.getLogger("chaosmesh")
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
```
