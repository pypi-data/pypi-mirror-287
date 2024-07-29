# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from os import path
import os

# packages = find_packages('.')
# print(packages)

here = os.path.abspath(os.path.dirname(__file__))

with open(path.join(here, 'readme.md')) as f:
    long_description = f.read()


setup(
    name="SuffixAutomaton",
    # packages=find_packages(),
    py_modules=['SuffixAutomaton'],
    version='0.1.4',
    description='suffix automaton by words, to get text common substrings',
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires='>=3.0',

    # include_package_data=True,
    package_data={
        # 引入任何包下面的 *.txt、*.rst 文件
        # "": ["*.txt", "*.rst"],
        # 引入 hello 包下面的 *.msg 文件
        # "ZiCutter": ["HanZi/*.txt"],
    },
    # data_files=[('data', ['data/ChaiZi.txt'])],

    url='https://github.com/laohur/SuffixAutomaton',
    keywords=['Suffix Automaton', 'sam'],
    author='laohur',
    author_email='laohur@gmail.com',
    license='[Anti-996 License](https: // github.com/996icu/996.ICU/blob/master/LICENSE)',
)

"""
python setup.py sdist
python setup.py bdist_wheel
twine upload dist/*
"""
