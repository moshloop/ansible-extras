
from subprocess import *
from setuptools import setup, find_packages
from setuptools.command.install import install
from ansible_extras import __version__
import os
from os.path import isfile

__name__ = 'ansible-extras'
cwd = os.getcwd()
base = __name__
data_files = []
for dir in ['library', 'meta', 'filter_plugins']:
  files = []
  for file in [f for f in os.listdir(dir) if isfile("%s/%s/%s" % (cwd,dir,f))]:
    files.append("%s/%s" % (dir,file))
  data_files.append(("%s/%s" % (base, dir), files))


class link_role(install):
    def run(self):
        install.run(self)
        print (self)


setup(
    name = __name__,
    version = __version__,
    packages = [__name__.replace("-", "_")],
    data_files = data_files,
    cmdclass = {'install': link_role},
    url = 'https://www/github.com/moshloop/ansible-extras',
    author = 'Moshe Immerman', author_email = 'moshe.immerman@gmail.com'
)