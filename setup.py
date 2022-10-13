from setuptools import setup

with open('requirements.txt') as r:
    req = r.read()

setup(
    name="SLunixUtils", 
    version="0.1.0", 
    install_requires=req, 
    include_package_data=True, 
    zip_safe=False, 
    packages=["SLunixUtils"]
)