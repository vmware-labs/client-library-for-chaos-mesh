from dataclasses import dataclass

from typing import List


@dataclass
class Selector:
    """
    Class that represents the selector for selecting objects in a namespace in k8s cluster.

    Attributes:
    ----------------
    namespaces (List[str]): List of namespaces to select objects from.
    labelSelectors (dict): Dictionary of label selectors to filter the objects.
    pods (List[str]): List of pod names to select.
    """
    namespaces: List[str] = None
    labelSelectors: dict = None
    pods: List[str] = None
