from setuptools import setup

with open('requirements.txt') as r:
    req = r.read()

setup(name="SLUtils", version="0.0.2", install_requires=req, include_package_data=True, zip_safe=False, packages=["SLUtils"])