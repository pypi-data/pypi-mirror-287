import codecs
import os
from setuptools import setup, find_packages

# these things are needed for the README.md show on pypi
here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()


VERSION = '0.0.1'
DESCRIPTION = '一个用来自主操控记忆内存的智能体'
LONG_DESCRIPTION = ' 一个用来自主操控记忆内存的智能体  '

# Setting up
setup(
    name="mem_agent",
    version=VERSION,
    author="whoiswennie",
    author_email="3287305464@qq.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['qdrant-client==1.9.1'],
    keywords=['python','AI Agent','LLM','memory'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)