from abc import ABC
from dataclasses import asdict

from chaosmesh.k8s.experiment import ChaosExperiment


class JVMFault(ChaosExperiment, ABC):
    """
    JVMFault is a subclass of the `ChaosExperiment` class and implements the abstract base class `ABC`.

    The class provides the functionality for conducting JVM-level chaos experiments.

    Attributes:
        kwargs (dict): A dictionary of keyword arguments passed to the parent class.

    Properties:
        defaults: A generator that yields default values for the JVMFault experiment.

    Methods:
        action: Returns the action that will be performed in the JVMFault experiment.
        api_resources: Returns the API resource specifications for the JVMFault experiment.
        spec: Returns the specifications for the JVMFault experiment.
    """

    def __init__(self, **kwargs):
        """
        Initializes the JVMFault object.

        Args:
            kwargs (dict): A dictionary of keyword arguments passed to the parent class.
        """
        super(JVMFault, self).__init__(**kwargs)

    @property
    def schedule(self) -> dict:
        return {
            "type": "JVMChaos",
            "spec": "jvmChaos"
        }

    @property
    def defaults(self) -> dict:
        """
        A generator that yields default values for the JVMFault experiment.

        Returns:
            A generator that yields default values for the JVMFault experiment.
        """
        yield

    def action(self) -> str:
        """
        Returns the action that will be performed in the JVMFault experiment.

        Returns:
            str: A string representing the action to be performed.
        """
        pass

    def api_resources(self) -> dict:
        """
        Returns the API resource specifications for the JVMFault experiment.

        Returns:
            dict: A dictionary containing the API resource specifications for the JVMFault experiment.
        """
        return {"group": 'chaos-mesh.org', "version": 'v1alpha1', "plural": "jvmchaos"}

    def spec(self, namespace, name) -> dict:
        """
        Returns the specifications for the JVMFault experiment.

        Args:
            namespace (str): The namespace in which the JVMFault experiment will be executed.
            name (str): The name of the JVMFault experiment.

        Returns:
            dict: A dictionary containing the specifications for the JVMFault experiment.
        """
        return {
            "selector": asdict(self.kwargs['selector']),
            "mode": self.kwargs.get('mode'),
            "duration": self.kwargs.get('duration'),
            "action": self.action(),
            "name": name,
            "class": self.kwargs.get('targetClass'),
            "method": self.kwargs.get('method'),
            "value": self.kwargs.get('value'),
            "exception": self.kwargs.get('exception'),
            "latency": self.kwargs.get('latency'),
            "cpuCount": self.kwargs.get('cpuCount'),
            "memType": self.kwargs.get('memType'),
            "port": self.kwargs['port'],
            "ruleData": self.kwargs['ruleData'],
        }
