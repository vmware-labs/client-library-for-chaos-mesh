from glob import iglob

import semver
from setuptools import find_packages
from setuptools import setup

version_file = "version.txt"


# NOTE: major or minor version should be manually updated if the changes are NOT backward compatible
def bump_version():
    with open(version_file) as f:
        version = f.read().strip()

    incremented_version = semver.VersionInfo.parse(version).bump_patch()
    with open(version_file, "w") as file:
        file.write(str(incremented_version))

    return str(incremented_version)


def get_requirements():
    with open('requirements.txt') as f:
        return f.read().splitlines()


setup(name='chaos_mesh',
      version=bump_version(),
      description='A client to create experiments in ChaosMesh',
      long_description='''
This is a Chaos Mesh client written in Python, which allows you single point of entry to create experiments.

In order to create the Chaos Mesh client you can use the following command:

```python
from chaos_client import ChaosMeshClient, Experiment
from k8s.selector import Selector

client = ChaosMeshClient()
selector = Selector(labelSelectors={"app": "filebeat"}, namespaces=None, pods=None)

# name of the experiment
exp_name = str(uuid.uuid4())

# starting up the pod failure experiment
client.start(Experiment.POD_FAILURE, namespace="default", name=exp_name, selector=selector)
```
      ''',
      author='Vishrant Gupta',
      author_email='gvishrant@vmware.com',
      packages=find_packages(),
      url='https://github.com/vishrantgupta/chaos-mesh',
      include_package_data=True,
      install_requires=get_requirements(),
      platform='any',
      data_files=[
          ('version.txt', iglob('version.txt', recursive=True)),
      ],
      zip_safe=False)
