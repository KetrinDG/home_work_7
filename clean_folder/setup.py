from setuptools import setup, find_namespace_packages

setup(
      name='clean',
      version='1.0',
      description='A flexible module to clean folder',
      author='author',
      author_email='degtyareva.ev1@gmail.com',
      url='',
      entry_points={'console_scripts': ['clean_folder == clean_folder.clean']},
      license='MIT',
      packages=find_namespace_packages()
      )