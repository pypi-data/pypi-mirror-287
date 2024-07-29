from setuptools import setup, find_packages

with open ("docs\\Chinese_README.md","r",encoding="utf-8") as f :
    description = f.read()

setup(
    name="rk_mcprotocal",
    version="0.0.2",
    packages=find_packages(),
    install_requires=[
 
 
    ],
    long_description=description,
    long_description_content_type="text/markdown"
)


