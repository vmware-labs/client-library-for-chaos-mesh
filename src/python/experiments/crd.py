from abc import abstractmethod, ABC
from dataclasses import asdict

import time
from kubernetes.client import ApiException
from polling import TimeoutException

from .k8s.manifest import Manifest, Metadata
from .k8s_resource import K8SResource


class CustomObjectsApi(K8SResource, ABC):
    """
    Class for custom object api
    """

    def __init__(self):
        super(CustomObjectsApi, self).__init__()

    @abstractmethod
    def api_resources(self):
        pass

    @property
    def group(self):
        return self.api_resources().get('group')

    @property
    def version(self):
        return self.api_resources().get('version')

    @property
    def plural(self):
        return self.api_resources().get('plural')

    @abstractmethod
    def spec(self) -> dict:
        pass

    def manifest(self, namespace, name, labels: dict = None) -> dict:
        return asdict(Manifest(
          kind=self.plural,
          api_version=self.group + "/" + self.version,
          metadata=Metadata(namespace=namespace, name=name, labels=labels),
          spec=self.spec()
        ))

    @property
    def client(self):
        """
        Returns the CustomObjectAPI client
        :return: 
        """
        return self.k8sclient.CustomObjectsApi()

    def apply(self, namespace, object):
        return self.client.create_namespaced_custom_object(group=self.group, version=self.version, namespace=namespace, plural=self.plural, body=object, pretty='true')

    def get_clustered(self, name):
        return self.client.get_cluster_custom_object(group=self.group, version=self.version, plural=self.plural, name=name)

    def get(self, namespace, name):
        return self.client.get_namespaced_custom_object(group=self.group, version=self.version, plural=self.plural, name=name, namespace=namespace)

    def list(self, namespace, **kwargs):
        return self.client.list_namespaced_custom_object(group=self.group, version=self.version, namespace=namespace, plural=self.plural, **kwargs)

    def list_clustered(self):
        return self.client.list_cluster_custom_object(group=self.group, version=self.version, plural=self.plural)

    def add_annotation(self, namespace, name, annotations_map):
        return self.client.patch_namespaced_custom_object_with_http_info(group=self.group, version=self.version, namespace=namespace, plural=self.plural, name=name,
                                                                         body={
                                                                             "metadata": {"annotations": annotations_map}
                                                                         })

    def status(self, namespace, name):
        """
        Returns the status of k8s object
        :param namespace: 
        :param name: 
        :return: 
        """
        return self.client.get_namespaced_custom_object_status(group=self.group, version=self.version, namespace=namespace, plural=self.plural, name=name)['status']

    def delete(self, namespace, name, retries=120, foreground=True):
        """
        Delete object in foreground by default
        :param foreground: 
        :param namespace: 
        :param name: 
        :param retries: 
        :return: 
        """
        deleted = None
        try:
            deleted = self.client.delete_namespaced_custom_object(group=self.group, version=self.version, namespace=namespace, plural=self.plural, name=name)
            if foreground:
                while self.get(namespace, name) is not None:
                    retries -= 1
                    if retries == 0:
                        raise TimeoutException("Timeout out deleting the resource")
                    time.sleep(1)
        except ApiException as e:
            if e.status == 404:
                pass
            else:
                raise

        return deleted

    def exists(self, name, namespace):
        try:
            obj = self.get(name=name, namespace=namespace)
            return obj is not None
        except ApiException as e:
            if e.status == 404:
                return False
            else:
                raise
