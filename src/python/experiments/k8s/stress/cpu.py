from dataclasses import asdict

from src.python.selector import Selector
from .stress_test import StressTest


class StressCPU(StressTest):

    def __init__(self, **kwargs):
        super(StressCPU, self).__init__(**kwargs)

    def spec(self):
        assert self.kwargs['selector'] is not None, "label selector cannot be None"
        assert isinstance(self.kwargs['selector'], Selector), "check the selector type"

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
