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
      author='Vishrant Gupta',
      author_email='gvishrant@vmware.com',
      packages=find_packages(),
      url='https://github.com/vishrantgupta/chaos-mesh',
      include_package_data=True,
      install_requires=get_requirements(),
      platform='any',
      zip_safe=False)
