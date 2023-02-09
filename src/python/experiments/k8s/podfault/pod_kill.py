import os

from .pod_chaos import PodChaos

curr_dir = os.path.dirname(__file__)


class PodKill(PodChaos):

    def __init__(self, **kwargs):
        super(PodKill, self).__init__(**kwargs)

    def action(self):
        return "pod-kill"
