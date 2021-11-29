# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

setup(
    name="wr_demo",
    packages=find_packages(exclude=('test', 'node_modules')),
    version="1.0.0",
    description="Wrangler demo",
    author="Vincent Poilvert",
    license="",
    package_data={"wr_demo": ["py.typed"]},
    zip_safe=False,
)
