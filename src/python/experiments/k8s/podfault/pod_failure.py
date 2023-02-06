import os
from dataclasses import dataclass

from kubecrd import KubeResourceBase

from ...experiment import ChaosExperiment

curr_dir = os.path.dirname(__file__)


@dataclass
class PodFailure(ChaosExperiment, KubeResourceBase):
    __group__ = 'chaos-mesh.org'
    __version__ = 'v1alpha1'

    def __init__(self):
        super(PodFailure, self).__init__()

    def api_resources(self):
        return {"group": self.__group__, "version": self.__version__, "plural": "podchaos"}

    def start(self, namespace, selector):
        self.crd_schema()
