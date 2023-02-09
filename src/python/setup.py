from setuptools import find_packages
from setuptools import setup


def get_requirements():
    with open('requirements.txt') as f:
        return f.read().splitlines()


setup(name='chaos_mesh',
      version="1.0.0",
      description='A client to create experiments in ChaosMesh',
      author='Vishrant Gupta',
      author_email='gvishrant@vmware.com',
      packages=find_packages(),
      url='https://github.com/arkrwn/chaos-python',
      include_package_data=True,
      install_requires=get_requirements(),
      platform='any',
      zip_safe=False)
