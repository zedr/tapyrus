from setuptools import setup, find_packages


setup(
    name="tapyrus",
    version="0.1.0",
    packages=find_packages(),
    package_dir={"": "src"},
    entry_points={"console_scripts": ["tapyrus=tapyrus.cmd:main"]},
)
