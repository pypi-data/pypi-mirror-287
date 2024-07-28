from setuptools import setup, find_packages
setup(
    name="hffs",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "huggingface_hub[hf_transfer]"
    ],
    entry_points={
        "console_scripts": [
            "hffs=hffs.main:main",
        ],
    },
    description="embeddable huggingface downloader web ui",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/cocktailpeanut/huggingfs",
    python_requires=">=3.6",
)

