from abc import ABC, abstractmethod

from kubernetes import client

from .kubeclient import load_kube_config


class K8SResource(ABC):
    """
    Base class for all the k8s resources
    """

    def __init__(self):
        load_kube_config()

    @abstractmethod
    def client(self):
        """
        Returns the k8s client
        :return: 
        """
        pass

    @property
    def k8sclient(self):
        """
        Returns the kubernetes cluster client
        :return: 
        """
        return client
