import logging

from chaosmesh.experiments import Experiment
from chaosmesh.experiments.factory import ExperimentFactory
from chaosmesh.schedules import Schedule

log = logging.getLogger("chaosmesh")


class Client:
    """
    The `Client` class provides the interface to interact with the chaos mesh experiments.

    Attributes:
        factory (ExperimentFactory): An instance of `ExperimentFactory` class to get the experiment instance.

    Methods:
        start_experiment (experiment_type: Experiment, namespace: str, name: str, **kwargs) -> dict:
            Starts the specified chaos experiment.

        pause_experiment (experiment_type: Experiment, namespace: str, name: str, **kwargs) -> dict:
            Pauses the specified chaos experiment.

        delete_experiment (experiment_type: Experiment, namespace: str, name: str, **kwargs) -> dict:
            Deletes the specified chaos experiment.

        schedule_experiment (experiment_type: Experiment, namespace: str, name: str, cron_schedule: str, **kwargs) -> dict:
            Schedules the specified chaos experiment to run on a cron schedule.

        delete_schedule (experiment_type: Experiment, namespace: str, name: str, **kwargs) -> dict:
            Deletes the schedule for the specified chaos experiment.
    """

    def __init__(self, version: str):
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

    def schedule_experiment(self, experiment_type: Experiment, namespace: str, name: str, cron_schedule: str, **kwargs):
        """
        Creates a schedule for the specified chaos experiment.

        Arguments:
            experiment_type (Experiment): The type of chaos experiment to schedule.
            namespace (str): The namespace in which the experiment is to be run.
            name (str): The name of the chaos experiment.
            cron_schedule (str): The cron schedule in which the experiment should run.
            **kwargs: The optional parameters for the experiment.

        Returns:
            dict: The created schedule's resource in Kubernetes.
        """
        log.info(f"scheduling {experiment_type.value} experiment {name} in {namespace} namespace")
        return Schedule(experiment=self.factory.get_experiment(experiment_type, **kwargs), schedule=cron_schedule, **kwargs).submit(namespace=namespace, name=name)

    def delete_schedule(self, experiment_type: Experiment, namespace: str, name: str, **kwargs):
        """
        Deletes the schedule for the specified chaos experiment.

        Arguments:
            experiment_type (Experiment): The type of chaos experiment to unschedule.
            namespace (str): The namespace in which the experiment is running.
            name (str): The name of the chaos experiment.
            **kwargs: The optional parameters for the experiment.

        Returns:
            Schedule
        """
        log.info(f"deleting schedule for {experiment_type.value} experiment {name} in {namespace} namespace")
        return Schedule(self.factory.get_experiment(experiment_type, **kwargs)).delete(namespace=namespace, name=name)
