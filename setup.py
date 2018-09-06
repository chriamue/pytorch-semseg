#!/usr/bin/env python

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(name='pytorch-semseg',
                 version='0.1.3',
                 description='Semantic Segmentation Architectures Implemented in PyTorch',
                 long_description=long_description,
                 long_description_content_type="text/markdown",
                 license='MIT',
                 author='chriamue',
                 author_email='chriamue@gmail.com',
                 url="https://github.com/meetshah1995/pytorch-semseg",
                 install_requires=['numpy>=1.12.1',
                                   'scipy>=0.19.0',
                                   'torch>=0.4.1',
                                   'torchvision>=0.2.0',
                                   'tqdm>=4.11.2',
                                   'visdom>=0.1.1',
                                   'pydensecrf'],
                 packages=setuptools.find_packages(),
                 classifiers=(
                     "Intended Audience :: Developers",
                     "Intended Audience :: Education",
                     "Intended Audience :: Science/Research",
                     "Scientific/Engineering :: Artificial Intelligence",
                     "Programming Language :: Python :: 3",
                     "License :: OSI Approved :: MIT License",
                     "Operating System :: OS Independent",
                 ),
                 )
