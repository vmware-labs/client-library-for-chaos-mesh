from dataclasses import asdict

from chaosmesh.experiments.k8s.stress import StressTest
from chaosmesh.k8s.selector import Selector


class PodStressCPU(StressTest):

    def __init__(self, **kwargs):
        super(PodStressCPU, self).__init__(**kwargs)

    def validate(self):
        assert self.kwargs['selector'] is not None, "label selector cannot be None"
        assert isinstance(self.kwargs['selector'], Selector), "check the selector type"

        assert self.kwargs['workers'] is not None, "workers cannot be None"
        assert self.kwargs['load'] is not None, "size cannot be None"

    def spec(self, namespace, name):
        return {
            "selector": asdict(self.kwargs['selector']),
            "mode": self.kwargs.get('mode'),
            "stressors": {
                "cpu": {
                    "workers": self.kwargs.get('workers'),
                    "load": self.kwargs.get('load')
                }
            },
            "duration": self.kwargs.get('duration')
        }
