import uuid

import time

from src.python.client import ChaosMeshClient, Experiment
from src.python.selector import Selector

client = ChaosMeshClient()
selector = Selector(labelSelectors={"app": "filebeat"})

# name of the experiment
e_name = str(uuid.uuid4())

# starting up the experiment
client.start(Experiment.K8S_POD_FAILURE, namespace="default", name=e_name, selector=selector)
time.sleep(10)

# pausing the experiment
client.pause(Experiment.K8S_POD_FAILURE, namespace="default", name=e_name)
