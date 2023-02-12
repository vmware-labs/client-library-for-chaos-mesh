from abc import ABC

from polling import poll

from chaosmesh.k8s.crd import CustomObjectsApi


class ChaosExperiment(CustomObjectsApi, ABC):

    def __init__(self, **kwargs):
        self.kwargs = kwargs
        super(ChaosExperiment, self).__init__()

        # initialize defaults
        for key, value in self.defaults.items():
            self.kwargs[key] = kwargs.get(key, value)

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

    def validate(self):
        pass

    @property
    def defaults(self) -> dict:
        yield

    def submit(self, namespace, name, labels=None):

        assert namespace is not None, "namespace can not be None"
        assert name is not None, "name can not be None"

        # validating the spec before applying it to k8s
        self.validate()

        return self.apply(name=name, namespace=namespace, labels=labels)

    def pause(self, namespace, name):
        self.add_annotation(namespace=namespace, name=name, annotations_map={"experiment.chaos-mesh.org/pause": 'true'})

    def apply(self, name, namespace, labels=None):
        applied = super().apply(namespace=namespace, object=self.manifest(namespace=namespace, name=name, labels=labels))
        self.wait_experiment_injection(namespace=namespace, name=name)
        return applied
