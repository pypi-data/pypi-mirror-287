# setup.py

from setuptools import setup, find_packages

setup(
    name="rkt-cli-test-101",
    version="0.0.1",
    packages=find_packages("todoapp"),
    package_dir={"": "todoapp"},
    include_package_data=True,
    install_requires=["Click"],
    entry_points={
        "console_scripts": [
            "todov1 = todov1.todov1:cli",
            "todov2 = todov2.todo:cli",
            "todov3 = todov3.todo:cli",
            # "todov4 = todov4.cli:cli",
        ]
    },
)
