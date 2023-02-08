import os
import uuid

from ...experiment import ChaosExperiment

curr_dir = os.path.dirname(__file__)


class PodFailure(ChaosExperiment):

    @property
    def defaults(self):
        return {"name": str(uuid.uuid4())}

    def __init__(self):
        super(PodFailure, self).__init__()

    def api_resources(self):
        return {"group": 'chaos-mesh.org', "version": 'v1alpha1',
                "plural": "podchaos"}

    def spec(self, **kwargs):
        return {
            "apiVersion": self.group + "/" + self.version,
            "kind": self.plural,
            "metadata": {
                "name": kwargs.get('name', self.defaults.get('name')),
                "namespace": kwargs.get('namespace', self.defaults.get('namespace'))
            },
            "spec": {
                # TODO add the pod failure spec; and populate it with kwargs or use default value
                "message": "specific spec"
            }
        }
