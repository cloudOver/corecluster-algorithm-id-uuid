from distutils.core import setup
from setuptools import find_packages
from distutils.command.install import install as _install

def version():
    f = open('debian/changelog')
    v = f.readline().split()[1]
    return v[1:-1]

setup(
  name = 'corecluster-algorithm-id-uuid',
  packages = find_packages(exclude=['config', 'config.*']),
  version = '17.04.01',
  description = 'Default ID generator for CoreCluster',
  author = 'Maciej Nabozny',
  author_email = 'maciej.nabozny@cloudover.io',
  url = 'http://cloudover.org/corecluster/',
  download_url = 'https://github.com/cloudOver/CoreCluster/archive/master.zip',
  keywords = ['corecluster'],
  classifiers = [],
  install_requires = ['corecluster'],
)
