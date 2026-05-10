# Adapted from https://github.com/pybind/cmake_example/blob/master/setup.py
import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'
import re
import sys
import platform
import subprocess
import importlib
from sysconfig import get_paths

import importlib
from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext
from setuptools.command.install import install
from distutils.sysconfig import get_config_var
from distutils.version import LooseVersion

class CMakeExtension(Extension):
    def __init__(self, name, sourcedir, build_with_cuda):
        Extension.__init__(self, name, sources=[])
        self.sourcedir = os.path.abspath(sourcedir)
        self.build_with_cuda = build_with_cuda

class Build(build_ext):
    def run(self):
        try:
            out = subprocess.check_output(['cmake', '--version'])
        except OSError:
            raise RuntimeError("CMake must be installed to build the following extensions: " +
                               ", ".join(e.name for e in self.extensions))

        super().run()



    def build_extension(self, ext):

        setup_dir = os.path.abspath(os.path.dirname(__file__))
        build_dir = os.path.abspath(self.build_lib)
        inc_dir = os.path.abspath(sys.exec_prefix + "/include")

        cuda_available = torch.cuda.is_available()

        cmake_args = [
                      #'-G', 'Ninja',
                      '-DCMAKE_LIBRARY_OUTPUT_DIRECTORY=' + build_dir,
                      '-DPYTHON_LIBRARY=' + sys.executable,
                      '-DPYTHON_INCLUDE_PATH=' + inc_dir,
                      '-DCMAKE_LIBRARY_OUTPUT_DIRECTORY_RELEASE=' + build_dir,
                      '-DCMAKE_RUNTIME_OUTPUT_DIRECTORY_RELEASE=' + build_dir,
                      '-DDIFFVG_CUDA=0'
                    ]

        env = os.environ.copy()
        env['CFLAGS'] = '/wd4820 /wd4626 /wd5027 /wd4365 /wd5219 /wd4244 /wd4456 /wd4996 /wd4710 /wd4711 /wd4702'
        env['CXXFLAGS'] = '/wd4820 /wd4626 /wd5027 /wd4365 /wd5219 /wd4244 /wd4456 /wd4996 /wd4710 /wd4711 /wd4702'
        env['_CRT_SECURE_NO_WARNINGS'] = '1'
        env['_CRT_NONSTDC_NO_WARNINGS'] = '1'

        if not os.path.exists(self.build_temp):
             os.makedirs(self.build_temp)

        subprocess.check_call(['cmake', setup_dir] + cmake_args, cwd=self.build_temp, env=env)
        subprocess.check_call(['cmake', '--build', '.', '--config', 'Release'], cwd=self.build_temp, env=env)










torch_spec = importlib.util.find_spec("torch")
tf_spec = importlib.util.find_spec("tensorflow")
packages = []
build_with_cuda = False
if torch_spec is not None:
    packages.append('pydiffvg')
    import torch
    if torch.cuda.is_available():
        build_with_cuda = True
if tf_spec is not None and sys.platform != 'win32':
    packages.append('pydiffvg_tensorflow')
    if not build_with_cuda:
        import tensorflow as tf
        if tf.test.is_gpu_available(cuda_only=True, min_cuda_compute_capability=None):
            build_with_cuda = True
if len(packages) == 0:
    print('Error: PyTorch or Tensorflow must be installed. For Windows platform only PyTorch is supported.')
    exit()
# Override build_with_cuda with environment variable
if 'DIFFVG_CUDA' in os.environ:
    build_with_cuda = os.environ['DIFFVG_CUDA'] == '1'

setup(name = 'diffvg',
      version = '0.0.1',
      install_requires = ["svgpathtools"],
      description = 'Differentiable Vector Graphics',
      ext_modules = [CMakeExtension('diffvg', '', build_with_cuda)],
      cmdclass = dict(build_ext=Build, install=install),
      packages = packages,
      zip_safe = False)
