import io
from setuptools import setup, find_packages

def read_requirements():
    with open("requirements.txt") as fp:
        content = fp.readlines()
    return [line.strip() for line in content if not line.startswith("#")]

setup(
    name="unique-llama-models",  # Change this to a unique name
    version="0.0.2",
    author="Meta Llama",
    author_email="llama-oss@meta.com",
    description="Llama models",
    long_description=io.open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/meta-llama/llama-models",
    package_dir={"llama_models": "models"},
    classifiers=[],
    python_requires=">=3.10",
    install_requires=read_requirements(),
    include_package_data=True,
)
