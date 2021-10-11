import io
from setuptools import find_packages, setup

with io.open("README.md", "rt", encoding="utf8") as f:
    readme = f.read()

setup(
    name="DinoBot",
    version="1.0.0",
    url="https://github.com/M0NsTeRRR/DinoBot",
    license="CeCILL v2.1",
    maintainer="Ludovic Ortega",
    maintainer_email="ludovic.ortega@adminafk.fr",
    description="DinoBot is a discord bot manager for Lyon 2",
    long_description=readme,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.8,<3.10",
    install_requires=[
        "discord.py==1.7.3",
        "toml==0.10.2",
        "discord.py==1.7.3",
        "sentry-sdk==1.4.3",
        # "requests==2.26.0",
        "openpyxl==3.0.9",
        "python-dateutil==2.8.2",
    ],
    extras_require={
        "dev": ["pre-commit==2.15.0"],
    },
)
