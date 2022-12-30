from setuptools import setup, find_packages

setup(
      name='clean',
      version='1.0',
      description='A flexible module to clean folder',
      author='author',
      author_email='degtyareva.ev1@gmail.com',
      url='',
      modules=['clean'],
      entry_points={'console_scripts': ['pip install -e']},
      packages = find_packages(where="clean_folder"),
      package_dir = {"": "clean_folder"},
      include_package_data=True
      )