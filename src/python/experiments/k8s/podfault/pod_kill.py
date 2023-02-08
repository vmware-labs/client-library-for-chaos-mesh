import os

from .pod_chaos import PodChaos

curr_dir = os.path.dirname(__file__)


class PodKill(PodChaos):

    def __init__(self, **kwargs):
        super(PodKill, self).__init__(**kwargs)

    @property
    def defaults(self):
        return {
            "action": "pod-kill",
            "gracePeriod": 0,
        }
