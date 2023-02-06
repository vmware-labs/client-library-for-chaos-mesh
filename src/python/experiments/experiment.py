from abc import ABC, abstractmethod

from polling import poll

from .crd import CustomObjectsApi
from ..selector import Selector


class ChaosExperiment(CustomObjectsApi, ABC):

    def __init__(self):
        super(ChaosExperiment).__init__()

    def injected(self, namespace, name):
        obj = self.get(name=name, namespace=namespace)
        if obj is not None:
            conditions = obj['status']['conditions']

            for condition in conditions:
                if condition['type'] == 'AllInjected':
                    return condition['status']

    def wait_experiment_injection(self, namespace, name):
        poll(lambda: self.injected(namespace, name),
             timeout=int(60),
             step=2,
             ignore_exceptions=(Exception,))

    def apply(self, namespace, experiment):
        self.wait_experiment_injection(namespace=namespace, name=experiment.name)
        return super().apply(namespace=namespace, object=experiment)

    @abstractmethod
    def start(self, namespace, selector: Selector):
        pass
