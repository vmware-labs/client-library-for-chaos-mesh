from abc import ABC
from dataclasses import asdict

from chaosmesh.experiments.base.k8s.stress import StressTest
from chaosmesh.k8s.selector import Selector


class BasePodStressMemoryExperiment(StressTest, ABC):
    """
    BasePodStressMemoryExperiment is a subclass of `StressTest` and `ABC` (Abstract Base Class). It is used to define a stress experiment on memory.

    Attributes:
    None

    Methods:
    __init__(self, **kwargs)
        Initializes the `BasePodStressMemoryExperiment` class. It takes in `kwargs` as an argument and calls `super` to initialize the `StressTest` class.

    validate(self)
        Validates the arguments passed to the `BasePodStressMemoryExperiment` class. It checks if the `selector` argument is not None and is of type `Selector`. It also checks if the `workers` and `size` arguments are not None.

    spec(self, namespace, name)
        Returns a dictionary that represents the specification of the stress experiment on memory. The dictionary contains `selector`, `mode`, `stressors`, and `duration`. `selector` is a dictionary representation of the `selector` argument passed to the class. `stressors` is a dictionary containing the `workers` and `size` arguments. `duration` is the duration argument passed to the class.
    """

    def __init__(self, **kwargs):
        super(BasePodStressMemoryExperiment, self).__init__(**kwargs)

    def validate(self) -> None:
        assert self.kwargs['selector'] is not None, "label selector cannot be None"
        assert isinstance(self.kwargs['selector'], Selector), "check the selector type"

        assert self.kwargs['workers'] is not None, "workers cannot be None"
        assert self.kwargs['size'] is not None, "size cannot be None"

    def spec(self, namespace, name) -> dict:
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
