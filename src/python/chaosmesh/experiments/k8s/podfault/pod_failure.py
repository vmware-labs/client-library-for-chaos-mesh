import os

from chaosmesh.experiments.k8s.podfault import PodChaos

curr_dir = os.path.dirname(__file__)


class PodFailure(PodChaos):

    def __init__(self, **kwargs):
        super(PodFailure, self).__init__(**kwargs)

    def action(self):
        return "pod-failure"
