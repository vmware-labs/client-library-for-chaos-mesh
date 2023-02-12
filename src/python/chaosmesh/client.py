import logging

from chaosmesh.experiments import Experiment
from chaosmesh.experiments.factory import ExperimentFactory

log = logging.getLogger("chaosmesh")


class Client:
    """
    The `Client` class provides the interface to interact with the chaos mesh experiments.

    Attributes:
        factory (ExperimentFactory): An instance of `ExperimentFactory` class to get the experiment instance.

    Methods:
        start_experiment (Experiment, str, str, **kwargs) -> None:
            Starts the specified chaos experiment.

        pause_experiment (Experiment, str, str, **kwargs) -> None:
            Pauses the specified chaos experiment.

        delete_experiment (Experiment, str, str, **kwargs) -> None:
            Deletes the specified chaos experiment.
    """

    def __init__(self, version):
        """
        The constructor for the `Client` class.

        Arguments:
            version (str): The version of chaos mesh to be used.
        """
        self.factory = ExperimentFactory.get_instance(version)

    def start_experiment(self, experiment_type: Experiment, namespace: str, name: str, **kwargs):
        """
        Starts the specified chaos experiment.

        Arguments:
            experiment_type (Experiment): The type of chaos experiment to start.
            namespace (str): The namespace in which the experiment is to be run.
            name (str): The name of the chaos experiment.
            **kwargs: The optional parameters for the experiment.

        Returns:
            dict: The applied experiment's resource in Kubernetes.
        """
        log.info(f"starting {experiment_type.value} experiment {name} in {namespace} namespace")
        return self.factory.get_experiment(experiment_type, **kwargs).submit(namespace, name)

    def pause_experiment(self, experiment_type: Experiment, namespace: str, name: str, **kwargs) -> None:
        """
        Pauses the specified chaos experiment.

        Arguments:
            experiment_type (Experiment): The type of chaos experiment to pause.
            namespace (str): The namespace in which the experiment is running.
            name (str): The name of the chaos experiment.
            **kwargs: The optional parameters for the experiment.

        Returns:
            None
        """
        log.info(f"pausing {experiment_type.value} experiment {name} in {namespace} namespace")
        self.factory.get_experiment(experiment_type, **kwargs).pause(namespace, name)

    def delete_experiment(self, experiment_type: Experiment, namespace: str, name: str, **kwargs):
        """
        Deletes the specified chaos experiment.

        Arguments:
            experiment_type (Experiment): The type of chaos experiment to delete.
            namespace (str): The namespace in which the experiment is running.
            name (str): The name of the chaos experiment.
            **kwargs: The optional parameters for the experiment.

        Returns:
            dict: The deleted experiment's resource in Kubernetes.
        """
        log.info(f"deleting {experiment_type.value} experiment {name} in {namespace} namespace")
        return self.factory.get_experiment(experiment_type, **kwargs).delete(namespace=namespace, name=name)
