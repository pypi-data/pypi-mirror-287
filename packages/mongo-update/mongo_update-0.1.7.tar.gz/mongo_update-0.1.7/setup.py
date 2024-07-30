from distutils.core import setup
# import setuptools

packages = ['mongo_update']
setup(name='mongo_update',
      version='0.1.7',
      author='xigua, ',
      long_description='''
      mongodb数据更新。
      ''',
      packages=packages,
      package_dir={'requests': 'requests'}, )
