from chaosmesh.experiments import Experiment
from chaosmesh.experiments.factory import ExperimentFactory


class Client:

    def __init__(self):
        self.factory = ExperimentFactory.get_instance()

    def start_experiment(self, experiment_type: Experiment, namespace: str, name: str, **kwargs):
        self.factory.get_experiment(experiment_type, **kwargs).submit(namespace, name)

    def pause_experiment(self, experiment_type: Experiment, namespace: str, name: str, **kwargs):
        self.factory.get_experiment(experiment_type, **kwargs).pause(namespace, name)

    def delete_experiment(self, experiment_type: Experiment, namespace: str, name: str, **kwargs):
        self.factory.get_experiment(experiment_type, **kwargs).delete(namespace=namespace, name=name)
