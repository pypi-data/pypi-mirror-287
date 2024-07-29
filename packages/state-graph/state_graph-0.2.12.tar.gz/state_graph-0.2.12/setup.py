from setuptools import setup, find_packages
import os


os.system("rm -rf build dist")

setup(
    name="state_graph",
    version="0.2.12",
    packages=find_packages(),
    install_requires=[
        "pydantic",
        "networkx",
        "beartype",
        "rich",
        "ipython",
        # "resend",
    ],
)
