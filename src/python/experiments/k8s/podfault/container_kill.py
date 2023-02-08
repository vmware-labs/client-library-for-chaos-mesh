import os
from dataclasses import asdict

from src.python.selector import Selector
from .pod_chaos import PodChaos

curr_dir = os.path.dirname(__file__)


class ContainerKill(PodChaos):

    def __init__(self, **kwargs):
        super(ContainerKill, self).__init__(**kwargs)

    @property
    def defaults(self):
        return {
            "action": "container-kill",
            "gracePeriod": 0,
        }

    def spec(self, namespace, name):
        assert self.kwargs['selector'] is not None, "label selector cannot be None"
        assert isinstance(self.kwargs['selector'], Selector), "check the selector type"

        assert self.kwargs['container_names'] is not None, "container name cannot be None"

        return {
            "kind": self.plural,
            "apiVersion": self.group + "/" + self.version,
            "metadata": {
                "namespace": namespace,
                "name": name,
                "labels": self.kwargs['labels']
            },
            "spec": {
                "selector": asdict(self.kwargs['selector']),
                "mode": "all",
                "containerNames": self.kwargs['container_names'],
                "action": self.kwargs.get('action'),
                "gracePeriod": self.kwargs.get('gracePeriod')
            }
        }
