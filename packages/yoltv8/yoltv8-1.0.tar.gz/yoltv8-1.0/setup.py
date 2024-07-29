from distutils.core import  setup
import setuptools
packages = ['yoltv8']# 唯一的包名，自己取名
setup(name='yoltv8',
	version='1.0',
	author='wjl',
    packages=packages,
    package_dir={'requests': 'requests'},)
