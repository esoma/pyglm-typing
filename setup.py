
from setuptools import setup
from setuptools.config import read_configuration

config = read_configuration('setup.cfg')

setup(
    **config["options"],
    python_requires='>=3.6',
    package_data={
        "glm_typing": ['py.typed'],
        "glm-stubs": ['__init__.pyi'],
    }
)
