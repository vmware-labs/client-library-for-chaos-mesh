from enum import Enum


class Experiment(Enum):
    """An enumeration class that represents the different types of experiments that can be run.

    Attributes:
        POD_FAILURE (str): Indicates a Pod failure experiment.
        POD_KILL (str): Indicates a Pod kill experiment.
        CONTAINER_KILL (str): Indicates a Container kill experiment.
        POD_STRESS_CPU (str): Indicates a Pod stress CPU experiment.
        POD_STRESS_MEMORY (str): Indicates a Pod stress memory experiment.
        RAISE_EXCEPTION (str): Indicates an experiment that raises an exception.
        GC (str): Indicates a garbage collection experiment.
        HOST_STRESS_MEMORY (str): Indicates a Host stress memory experiment.
        HOST_STRESS_CPU (str): Indicates a Host stress CPU experiment.
        NETWORK_PARTITION (str): Indicates Network Partition experiment.
        NETWORK_BANDWIDTH (str): Indicates Network Bandwidth experiment.
    """
    POD_FAILURE = "POD_FAILURE"
    POD_KILL = "POD_KILL"
    CONTAINER_KILL = "CONTAINER_KILL"

    POD_STRESS_CPU = "POD_STRESS_CPU"
    POD_STRESS_MEMORY = "POD_STRESS_MEMORY"

    RAISE_EXCEPTION = "RAISE_EXCEPTION"
    GC = "GC"

    HOST_STRESS_MEMORY = "HOST_STRESS_MEMORY"
    HOST_STRESS_CPU = "HOST_STRESS_CPU"

    NETWORK_PARTITION = "NETWORK_PARTITION"
    NETWORK_BANDWIDTH = "NETWORK_BANDWIDTH"
