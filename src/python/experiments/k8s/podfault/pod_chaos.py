from abc import ABC
from dataclasses import asdict

from src.python.selector import Selector
from ...experiment import ChaosExperiment


class PodChaos(ChaosExperiment, ABC):

    def __init__(self, **kwargs):
        super(PodChaos, self).__init__()
        self.kwargs = kwargs
        self.kwargs['gracePeriod'] = self.kwargs.get('gracePeriod', self.defaults.get('gracePeriod'))
        self.kwargs['mode'] = self.kwargs.get('mode', self.defaults.get('mode'))
        self.kwargs['action'] = self.defaults.get('action')

        self.kwargs['labels'] = self.kwargs.get('labels', {})
        self.kwargs['pods'] = self.kwargs.get('pods', {})

    @property
    def defaults(self):
        return {
            "action": self.action(),
            "gracePeriod": 0,
            "mode": "all"
        }

    def action(self) -> str:
        pass

    def api_resources(self):
        return {"group": 'chaos-mesh.org', "version": 'v1alpha1', "plural": "podchaos"}

    def spec(self):
        assert self.kwargs['selector'] is not None, "label selector cannot be None"
        assert isinstance(self.kwargs['selector'], Selector), "check the selector type"

        return {
            "selector": asdict(self.kwargs['selector']),
            "mode": self.kwargs.get('mode'),
            "action": self.kwargs.get('action'),
            "gracePeriod": self.kwargs.get('gracePeriod')
        }
