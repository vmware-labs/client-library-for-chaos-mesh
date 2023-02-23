import json
import logging
from abc import ABC

from polling import poll

from chaosmesh.k8s.crd import CustomObjectsApi

log = logging.getLogger("chaosmesh")


class ChaosExperiment(CustomObjectsApi, ABC):
    """
    The base class for all ChaosMesh experiments.

    This class provides common functionalities for all ChaosMesh experiments, including
    defaults, validation, submission, pause, and apply.

    Attributes:
        kwargs (dict): A dictionary that stores all the experiment's arguments.

    """

    def __init__(self, **kwargs):
        """
        Initializes the `ChaosExperiment` class with the given arguments.

        Args:
            kwargs (dict): A dictionary of arguments for the experiment.

        """
        self.kwargs = kwargs
        super(ChaosExperiment, self).__init__()

        # initialize defaults
        for key, value in self.defaults.items():
            self.kwargs[key] = kwargs.get(key, value)

    def _is_injected(self, namespace, name):
        """
        Check if the experiment has been injected.

        Args:
            namespace (str): The namespace of the experiment.
            name (str): The name of the experiment.

        Returns:
            bool: Whether the experiment has been injected or not.

        """
        log.debug(f"checking if experiment {name} in {namespace} namespace got injected")

        obj = self.get(name=name, namespace=namespace)
        if obj is not None:
            conditions = obj['status']['conditions']

            for condition in conditions:
                log.debug(f"chaosmesh experiment {name} status is {condition['status']} for condition type {condition['type']}")

                if condition['type'] == 'AllInjected':
                    records = obj['status']['experiment']['containerRecords']
                    for record in records:
                        if record['phase'] == 'Injected':
                            log.debug(f"chaosmesh experiment {name} got injected")
                            return True
            return False

    def _wait_experiment_injection(self, namespace, name):
        """
        Wait for the experiment to be injected.

        Args:
            namespace (str): The namespace of the experiment.
            name (str): The name of the experiment.

        """
        poll(lambda: self._is_injected(namespace, name),
             timeout=int(120),
             step=2,
             ignore_exceptions=(Exception,))

    def validate(self) -> None:
        """
        Validate the experiment's specification before submitting it to Kubernetes.

        """
        pass

    @property
    def defaults(self) -> dict:
        """
        The default values for the experiment.

        Returns:
            dict: The default values.

        """
        yield

    def submit(self, namespace, name, labels=None):
        """
        Submit the experiment to the given namespace.

        Args:
            namespace (str): The namespace to which the experiment should be submitted.
            name (str): The name of the experiment.
            labels (dict, optional): Labels to be added to the experiment's resource in Kubernetes.

        Returns:
            dict: The applied experiment's resource in Kubernetes.

        """
        assert namespace is not None, "namespace can not be None"
        assert name is not None, "name can not be None"

        # validating the spec before applying it to k8s
        self.validate()

        return self.apply(name=name, namespace=namespace, labels=labels)

    def pause(self, namespace, name):
        """
        Pauses a running ChaosMesh experiment.

        This method adds an annotation to the running experiment in order to pause it.

        Args:
            namespace (str): The namespace where the experiment is running.
            name (str): The name of the experiment.

        """
        self.add_annotation(namespace=namespace, name=name, annotations_map={"experiment.chaos-mesh.org/pause": 'true'})

    def apply(self, name, namespace, labels=None):
        """
        Submits a ChaosMesh experiment.

        This method creates a manifest for the experiment and applies it to the target namespace.
        It also waits for the experiment to be injected into the target namespace.

        Args:
            name (str): The name of the experiment.
            namespace (str): The namespace where the experiment should be applied.
            labels (dict, optional): A dictionary of labels to be applied to the experiment. Defaults to `None`.

        Returns:
            The applied experiment object.

        """
        manifest = self.manifest(namespace=namespace, name=name, labels=labels)

        log.debug(f"creating chaosmesh resource {json.dumps(manifest, indent=4)}")

        applied = super().apply(namespace=namespace, object=manifest)
        self._wait_experiment_injection(namespace=namespace, name=name)

        log.info(f"chaosmesh experiment {name} got applied")

        return applied
