from setuptools import setup, find_packages

#Leer contenido del archivo README.md
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="TesseralHackProject",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    author="Tesseral",
    description="Consultar cursos hack4u",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://hack4u.io"
)