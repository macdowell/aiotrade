import os
from setuptools import setup

def read(f_name):
    return open(os.path.join(os.path.dirname(__file__), f_name)).read()


setup(name="pytrader", version="0.0.1",
      author="Evgenii Y. Zhuravlev",
      author_email="e.zhuravlev@cybsec.org",
      description=("An demonstration of how to create, document, and publish "
                   "to the cheese shop a5 pypi.org."),
      license="Apac",
      keywords="example documentation tutorial",
      url="http://packages.python.org/an_example_pypi_project",
      packages=['an_example_pypi_project', 'tests'],
      long_description=read('README'),
      classifiers=[
          "Development Status :: 1 - Planning",
          "Topic :: Utilities",
          "License :: OSI Approved :: BSD License",
      ])
