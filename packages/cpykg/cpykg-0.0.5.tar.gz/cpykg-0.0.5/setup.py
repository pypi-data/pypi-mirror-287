from setuptools import setup, find_packages

setup(
    name="cpykg",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    package_data={
        "cpykg": ["data/*.csv"]
    },
    include_package_data=True,
)