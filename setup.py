#!/usr/bin/env python
# coding: utf-8
with open("README.md", "r") as f:
	long_description = f.read()
import setuptools
setuptools.setup(name='Mymacroprocessor',
    version='0.0.2',
    description='python file macro processor',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='nufeng',
    author_email='18478162@qq.com',
    requires= ['re'],
    url='https://github.com/nufeng1999/Mymacroprocessor/',
    download_url='https://github.com/nufeng1999/Mymacroprocessor/releases/tag/0.0.1',
    packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
    keywords=['python', 'macro', 'processor', 'if','ifdef','ifndef','elif','else','endif','defined','define','undef'],
    license="apache 3.0",
    install_requires=[],
    include_package_data=True
    )
