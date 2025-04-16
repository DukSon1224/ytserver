import sys
import platform
from setuptools import setup
from setuptools.command.install import install

class CustomInstallCommand(install):
  def run(self):
    # Python
    if sys.version_info[:3] != (3, 10, 11):
      sys.exit("Only for Python 3.10.11")

    # OS
    if platform.system() != "Windows":
      sys.exit("Only for Windows")

    # Windows 10
    version = platform.version()  # '10.0.19045'
    major, *_ = map(int, version.split('.'))
    if major < 10:
      sys.exit("Only for higher than Windows 10")

    super().run()


setup(
  name='myserver',
  version='0.1.1',
  description='my_server_package',
  author='rhaos',
  packages=['myserver'],
  package_data={'myserver': ['*.pyd']},
  include_package_data=True,
  cmdclass={'install': CustomInstallCommand},
  python_requires='==3.10.11',
  install_requires=[
    'fastapi==0.115.8',
    'uvicorn==0.34.0',
    'yt-dlp[default]',
  ]
)
