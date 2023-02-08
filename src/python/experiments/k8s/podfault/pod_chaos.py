import os
from abc import ABC

from src.python.selector import Selector
from ...experiment import ChaosExperiment

curr_dir = os.path.dirname(__file__)


class PodChaos(ChaosExperiment, ABC):

    def __init__(self, **kwargs):
        super(PodChaos, self).__init__()
        self.kwargs = kwargs
        self.kwargs['action'] = self.defaults.get('action')
        self.kwargs['gracePeriod'] = self.kwargs.get('gracePeriod', self.defaults.get('gracePeriod'))
        self.kwargs['labels'] = self.kwargs.get('labels', {})
        self.kwargs['pods'] = self.kwargs.get('pods', {})

    def api_resources(self):
        return {"group": 'chaos-mesh.org', "version": 'v1alpha1', "plural": "podchaos"}

    def spec(self, namespace, name):
        assert self.kwargs['selector'] is not None, "label selector cannot be None"
        assert isinstance(self.kwargs['selector'], Selector), "check the selector type"

        return {
            "kind": self.plural,
            "apiVersion": self.group + "/" + self.version,
            "metadata": {
                "namespace": namespace,
                "name": name,
                "labels": self.kwargs['labels']
            },
            "spec": {
                "selector": {
                    # TODO Multiple namespace support?
                    "namespaces": [
                        namespace,
                    ],
                    "labelSelectors": self.kwargs['selector'].get(),
                    "pods": self.kwargs['pods']
                },
                "mode": "all",
                "action": self.kwargs.get('action'),
                "gracePeriod": self.kwargs.get('gracePeriod')
            }
        }
