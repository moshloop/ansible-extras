from subprocess import *
from setuptools import setup, find_packages
from setuptools.command.install import install
from ansible_extras import __version__
import os
import shutil
from os.path import isfile

__name__ = 'ansible-extras'
cwd = os.getcwd()
base = __name__
role_name = base.split('-')[1]
data_files = []
for dir in ['library', 'meta', 'filter_plugins']:
  files = []
  for file in [f for f in os.listdir(dir) if isfile("%s/%s/%s" % (cwd,dir,f))]:
    files.append("%s/%s" % (dir,file))
  data_files.append(("%s/%s" % (base, dir), files))


class link_role(install):
    def run(self):
        install.run(self)
        dist = "%s/%s/%s" % (os.getcwd(), self.install_data,self.config_vars['dist_name'])
        role = "/etc/ansible/roles/%s" % role_name
        print ("Renaming %s to %s" % (dist,role))
        shutil.rmtree(role)
        os.renames(dist,role)

setup(
    name = __name__,
    version = __version__,
    packages = [__name__.replace("-", "_")],
    data_files = data_files,
    cmdclass = {'install': link_role},
    url = 'https://www/github.com/moshloop/ansible-extras',
    author = 'Moshe Immerman', author_email = 'moshe.immerman@gmail.com'
)