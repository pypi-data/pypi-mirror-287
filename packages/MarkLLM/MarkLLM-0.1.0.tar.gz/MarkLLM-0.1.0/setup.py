from setuptools import setup, find_packages, Extension
from setuptools.command.build_ext import build_ext
from Cython.Build import cythonize
import numpy as np
import os

# 获取cython文件的路径
cython_files = [
    "watermark/exp_edit/cython_files/levenshtein.pyx",
    "watermark/its_edit/cython_files/levenshtein.pyx"
]

# 创建扩展模块
extensions = [
    Extension(
        "watermark.exp_edit.cython_files.levenshtein",
        sources=["watermark/exp_edit/cython_files/levenshtein.pyx"],
        include_dirs=[np.get_include()]
    ),
    Extension(
        "watermark.its_edit.cython_files.levenshtein",
        sources=["watermark/its_edit/cython_files/levenshtein.pyx"],
        include_dirs=[np.get_include()]
    )
]

# 读取requirements.txt中的依赖项
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="MarkLLM",
    version="0.1.0",
    author="Leyi Pan",
    author_email="panleyi2003@gmail.com",
    description="MarkLLM: An Open-Source Toolkit for LLM Watermarking",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/THU-BPM/MarkLLM",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
    install_requires=requirements,  
    ext_modules=cythonize(extensions),
    cmdclass={'build_ext': build_ext},
    zip_safe=False,
)