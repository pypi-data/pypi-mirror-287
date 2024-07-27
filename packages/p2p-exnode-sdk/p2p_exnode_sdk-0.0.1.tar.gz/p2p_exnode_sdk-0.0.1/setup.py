from setuptools import setup, find_packages

setup(
    name="p2p_exnode_sdk",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "requests>=2.20.0",
        "pydantic>=1.8.0",
    ],
    description="A P2P exnode SDK",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
