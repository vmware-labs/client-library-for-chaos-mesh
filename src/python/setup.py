from setuptools import find_packages
from setuptools import setup


def get_requirements():
    with open('requirements.txt') as f:
        return f.read().splitlines()


setup(name='chaos_mesh',
      version="1.0.0",
      description='Chaos Mesh Client',
      author='Vishrant Gupta',
      author_email='gvishrant@vmware.com',
      packages=find_packages(),
      include_package_data=True,
      install_requires=get_requirements(),
      platform='any',
      zip_safe=False)
