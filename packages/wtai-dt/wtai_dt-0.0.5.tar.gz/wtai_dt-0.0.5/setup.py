from setuptools import setup, find_packages
import os

VERSION = '0.0.5'
DESCRIPTION = 'wind turbine ai and digital twin'

setup(
    name="wtai_dt",
    version=VERSION,
    author="hnust",
    author_email="2538134102@qq.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=open('README.md',encoding="UTF8").read(),
    packages=find_packages(),
    install_requires=['moviepy'],
    keywords=['python', 'moviepy', 'cut video'],
    # data_files=[('wtai_dt', ['to_erase.json'])],
    # entry_points={
    # 'console_scripts': [
    #     'wtai_dt = wtai_dt.main:main'
    # ]
    # },
    license="MIT",
    url="https://github.com/importimport/wtai-dt",
    scripts=['wtai_dt/wtai_dt.py'],
    classifiers= [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows"
    ]
)