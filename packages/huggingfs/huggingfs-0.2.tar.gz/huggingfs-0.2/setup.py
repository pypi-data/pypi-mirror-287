from setuptools import setup, find_packages
setup(
    name="huggingfs",
    version="0.2",
    packages=find_packages(),
    install_requires=[
        "gradio",
        "huggingface_hub[hf_transfer]"
    ],
    entry_points={
        "console_scripts": [
            "huggingfs=huggingfs.main:main",
        ],
    },
    description="huggingface downloader web ui",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/cocktailpeanut/huggingfs",
    python_requires=">=3.6",
)

