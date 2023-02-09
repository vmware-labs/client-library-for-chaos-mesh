from dataclasses import asdict

from src.python.selector import Selector
from .stress_test import StressTest


class StressMemory(StressTest):

    def __init__(self, **kwargs):
        super(StressMemory, self).__init__(**kwargs)

    def spec(self):
        assert self.kwargs['selector'] is not None, "label selector cannot be None"
        assert isinstance(self.kwargs['selector'], Selector), "check the selector type"

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
