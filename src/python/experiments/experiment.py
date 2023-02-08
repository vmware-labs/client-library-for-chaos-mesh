import uuid
from abc import ABC, abstractmethod

from polling import poll

from .crd import CustomObjectsApi


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

    @abstractmethod
    @property
    def spec(self, **kwargs):
        pass

    @abstractmethod
    @property
    def defaults(self):
        pass

    def submit(self, experiment_name=defaults['name'], namespace=None, **kwargs):
        self.apply(experiment_name=experiment_name, namespace=namespace, kwargs=kwargs)
        return experiment_name

    def pause(self, experiment_name, namespace):
        # TODO implement this; by injecting pause
        pass

    def apply(self, experiment_name, namespace, **kwargs):
        self.wait_experiment_injection(namespace=namespace, name=experiment_name)
        return super().apply(namespace=namespace, object=self.spec(kwargs))
