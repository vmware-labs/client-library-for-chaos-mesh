import logging
import random

import sys
import time

from chaosmesh.client import Client
from chaosmesh.experiments import Experiment
from chaosmesh.k8s.selector import Selector

client = Client(version="v1alpha1")
selector = Selector(labelSelectors={"app": "filebeat"})

logging.getLogger("chaosmesh")
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


# -- Pod failure experiment --
def test_pod_failure():
    # name of the experiment
    exp_name = "filebeat-pod-failure-" + random.randint(0, 1000000).__str__()

    # starting up the pod failure experiment
    client.start_experiment(Experiment.POD_FAILURE, namespace="default", name=exp_name, selector=selector)
    time.sleep(10)

    # pausing the experiment
    client.pause_experiment(Experiment.POD_FAILURE, namespace="default", name=exp_name)

    # deleting the experiment
    client.delete_experiment(Experiment.POD_FAILURE, namespace="default", name=exp_name)
    time.sleep(5)


# -- Pod kill experiment --
def test_pod_kill():
    exp_name = "filebeat-pod-kill-" + random.randint(0, 1000000).__str__()

    # starting up the pod kill experiment
    client.start_experiment(Experiment.POD_KILL, namespace="default", name=exp_name, selector=selector)
    time.sleep(10)

    # pausing the experiment
    client.pause_experiment(Experiment.POD_KILL, namespace="default", name=exp_name)


# -- Container kill experiment --
def test_container_kill():
    exp_name = "filebeat-container-kill-" + random.randint(0, 1000000).__str__()

    # starting up the container kill experiment
    client.start_experiment(Experiment.CONTAINER_KILL, namespace="default", name=exp_name, selector=selector, container_names=['main'])
    time.sleep(10)

    # pausing the experiment
    client.pause_experiment(Experiment.CONTAINER_KILL, namespace="default", name=exp_name)


# -- Stress CPU experiment --
def test_pod_cpu_stress():
    exp_name = "filebeat-cpu-stress-" + random.randint(0, 1000000).__str__()

    # starting up the cpu stress experiment
    client.start_experiment(Experiment.POD_STRESS_CPU, namespace="default", name=exp_name, selector=selector, container_names=['main'])
    time.sleep(10)

    # pausing the experiment
    client.pause_experiment(Experiment.POD_STRESS_CPU, namespace="default", name=exp_name)


# -- Stress memory experiment --
def test_pod_memory_stress():
    exp_name = "filebeat-memory-stress-" + random.randint(0, 1000000).__str__()

    # starting up the pod memory stress experiment
    client.start_experiment(Experiment.POD_STRESS_MEMORY, namespace="default", name=exp_name, selector=selector, container_names=['main'])
    time.sleep(10)

    # pausing the experiment
    client.pause_experiment(Experiment.POD_STRESS_MEMORY, namespace="default", name=exp_name)


# -- JVM raise exception experiment --
def test_jvm_exception():
    exp_name = "jvm-exception-" + random.randint(0, 1000000).__str__()

    # starting up the jvm exception experiment
    client.start_experiment(Experiment.RAISE_EXCEPTION, namespace="default",
                            name=exp_name, selector=selector, targetClass="com.company.Main", method="save",
                            exception="java.lang.Exception", port=8080)
    time.sleep(10)

    # pausing the experiment
    client.pause_experiment(Experiment.RAISE_EXCEPTION, namespace="default", name=exp_name)


# -- JVM stress GC experiment --
def test_jvm_gc():
    exp_name = "jvm-gc-" + random.randint(0, 1000000).__str__()

    # starting up the jvm gc experiment
    client.start_experiment(Experiment.GC, namespace="default", name=exp_name, selector=selector, port=8080)
    time.sleep(10)

    # pausing the experiment
    client.pause_experiment(Experiment.GC, namespace="default", name=exp_name)


# -- Hosts stress CPU experiment --
def test_host_memory_stress():
    exp_name = "hosts-stress-cpu-" + random.randint(0, 1000000).__str__()

    # starting up the hosts stress CPU experiment
    client.start_experiment(Experiment.HOST_STRESS_MEMORY, namespace="default", name=exp_name,
                            address=["10.225.66.224", "10.225.67.213", "10.225.66.231", "10.225.66.138", "10.225.66.192", "10.225.67.52", "10.225.67.103"],
                            size="30GB")
    time.sleep(10)

    # pausing the experiment
    client.pause_experiment(Experiment.HOST_STRESS_MEMORY, namespace="default", name=exp_name)


# -- Hosts stress Memory experiment --
def test_host_cpu_stress():
    exp_name = "hosts-stress-memory-" + random.randint(0, 1000000).__str__()

    # starting up the hosts stress memory experiment
    client.start_experiment(Experiment.HOST_STRESS_CPU, namespace="default", name=exp_name,
                            address=["10.225.66.224", "10.225.67.213", "10.225.66.231", "10.225.66.138", "10.225.66.192", "10.225.67.52", "10.225.67.103"],
                            load=1000)
    time.sleep(10)

    # pausing the experiment
    client.pause_experiment(Experiment.HOST_STRESS_CPU, namespace="default", name=exp_name)


def test_network_partition():
    exp_name = "network-partition-" + random.randint(0, 1000000).__str__()

    # starting up the network partition experiment
    client.start_experiment(Experiment.NETWORK_PARTITION, namespace="default", name=exp_name, selector=selector, external_targets=["tcx"], direction="both")
    time.sleep(10)

    # pausing the experiment
    client.pause_experiment(Experiment.NETWORK_PARTITION, namespace="default", name=exp_name)


test_pod_failure()
test_pod_kill()
test_container_kill()
test_pod_cpu_stress()
test_pod_memory_stress()
test_jvm_exception()
test_jvm_gc()
test_host_memory_stress()
test_host_cpu_stress()
test_network_partition()
