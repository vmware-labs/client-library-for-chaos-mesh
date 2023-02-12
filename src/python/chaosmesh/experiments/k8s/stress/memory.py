from dataclasses import asdict

from chaosmesh.experiments.k8s.stress import StressTest
from chaosmesh.k8s.selector import Selector


class PodStressMemory(StressTest):

    def __init__(self, **kwargs):
        super(PodStressMemory, self).__init__(**kwargs)

    def validate(self):
        assert self.kwargs['selector'] is not None, "label selector cannot be None"
        assert isinstance(self.kwargs['selector'], Selector), "check the selector type"

        assert self.kwargs['workers'] is not None, "workers cannot be None"
        assert self.kwargs['size'] is not None, "size cannot be None"

    def spec(self, namespace, name):
        return {
            "selector": asdict(self.kwargs['selector']),
            "mode": self.kwargs.get('mode'),
            "stressors": {
                "memory": {
                    "workers": self.kwargs.get('workers'),
                    "size": self.kwargs.get('size')
                }
            },
            "duration": self.kwargs.get('duration')
        }
