import time

from chaosmesh.client import Client, Experiment
from chaosmesh.k8s.selector import Selector

# namespace in which to create the NetworkChaos object
ns_name = "default"

# creating the ChaosMesh client
client = Client(version="v1alpha1")

# target pods selector; by labelSector or by pods in specified namespaces
selector = Selector(labelSelectors={"app": "echoserver"}, pods=None, namespaces=[ns_name])

# name of the experiment
exp_name = "network-delay-100ms"

# default latency
latency = "100ms"

# time in seconds to sleep before deleting experiment
sleep_time = 10

# starting up the pod failure experiment
client.start_experiment(Experiment.NETWORK_DELAY, namespace=ns_name, name=exp_name, selector=selector, latency=latency)

# After we're done with the experiment we should delete it
time.sleep(sleep_time)
client.delete_experiment(Experiment.NETWORK_DELAY, namespace=ns_name, name=exp_name)

