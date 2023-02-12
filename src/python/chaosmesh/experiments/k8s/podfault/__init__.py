from abc import ABC
from dataclasses import asdict

from chaosmesh.k8s.experiment import ChaosExperiment
from chaosmesh.k8s.selector import Selector


class PodChaos(ChaosExperiment, ABC):

    def __init__(self, **kwargs):
        super(PodChaos, self).__init__(**kwargs)

    @property
    def defaults(self):
        return {
            "action": self.action(),
            "gracePeriod": 0,
            "mode": "all",
            "labels": {},
            "pods": {}
        }

    def action(self) -> str:
        pass

    def api_resources(self):
        return {"group": 'chaos-mesh.org', "version": 'v1alpha1', "plural": "podchaos"}

    def validate(self):
        assert self.kwargs['selector'] is not None, "label selector cannot be None"
        assert isinstance(self.kwargs['selector'], Selector), "check the selector type"

    def spec(self, namespace, name) -> dict:
        return {
            "selector": asdict(self.kwargs['selector']),
            "mode": self.kwargs.get('mode'),
            "action": self.kwargs.get('action'),
            "gracePeriod": self.kwargs.get('gracePeriod')
        }
