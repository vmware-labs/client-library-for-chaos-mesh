import os

from .pod_chaos import PodChaos

curr_dir = os.path.dirname(__file__)


class PodFailure(PodChaos):

    def __init__(self, **kwargs):
        super(PodFailure, self).__init__(**kwargs)

    @property
    def defaults(self):
        return {
            "action": "pod-failure",
            "gracePeriod": 0,
        }
