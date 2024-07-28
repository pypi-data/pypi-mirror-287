import setuptools
from pathlib import Path

# import os

# database_user = os.environ.get('USER')
# database_password = os.environ.get('PASSWORD')


long_desc = Path("README.md").read_text()
setuptools.setup(
    name="holamundoplayerfcedolin1",
    version="0.0.1",
    long_description=long_desc,
    packages=setuptools.find_packages(
        exclude=["mocks", "test"]
    )
)
