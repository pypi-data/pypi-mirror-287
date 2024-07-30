from setuptools import setup, find_packages
import os

VERSION = '0.0.2'
DESCRIPTION = 'Easily cut the video by moviepy'

setup(
    name="wtai-dt",
    version=VERSION,
    author="hnust",
    author_email="2538134102@qq.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=open('README.md',encoding="UTF8").read(),
    packages=find_packages(),
    install_requires=['moviepy'],
    keywords=['python', 'moviepy', 'cut video'],
    # data_files=[('package', ['to_erase.json'])],
    entry_points={
    'console_scripts': [
        'package = package.package:run'
    ]
    },
    license="MIT",
    url="https://github.com/importimport/wtai-dt",
    scripts=['package/dataprocess.py'],
    classifiers= [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows"
    ]
)