from abc import ABC, abstractmethod

from polling import poll

from .crd import CustomObjectsApi


class ChaosExperiment(CustomObjectsApi, ABC):

    def __init__(self):
        super(ChaosExperiment, self).__init__()

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
    def spec(self, namespace, name):
        pass

    @property
    def defaults(self):
        yield

    def submit(self, namespace, name):
        return self.apply(name=name, namespace=namespace)

    def pause(self, namespace, name):
        self.add_annotation(namespace=namespace, name=name, annotations_map={"experiment.chaos-mesh.org/pause": 'true'})

    def apply(self, name, namespace):
        applied = super().apply(namespace=namespace, object=self.spec(namespace=namespace, name=name))
        self.wait_experiment_injection(namespace=namespace, name=name)
        return applied
