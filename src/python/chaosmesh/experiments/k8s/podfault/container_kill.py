import os
from dataclasses import asdict

from chaosmesh.experiments.k8s.podfault import PodChaos
from chaosmesh.k8s.selector import Selector

curr_dir = os.path.dirname(__file__)


class ContainerKill(PodChaos):

    def __init__(self, **kwargs):
        super(ContainerKill, self).__init__(**kwargs)

    def action(self):
        return "container-kill"

    def validate(self):
        assert self.kwargs['selector'] is not None, "label selector cannot be None"
        assert isinstance(self.kwargs['selector'], Selector), "check the selector type"

        assert self.kwargs['container_names'] is not None, "container name cannot be None"

    def spec(self, namespace, name):
        return {
            "selector": asdict(self.kwargs['selector']),
            "mode": self.kwargs['mode'],
            "containerNames": self.kwargs['container_names'],
            "action": self.kwargs.get('action'),
            "gracePeriod": self.kwargs.get('gracePeriod')
        }
