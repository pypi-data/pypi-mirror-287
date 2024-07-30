from setuptools import setup, find_packages


def readme():
  with open('README.md', 'r') as f:
    return f.read()


setup(
  name='Mekanism Database',
  version='1.1',
  author='DwZZd',
  author_email='pppgame61@gmail.com',
  description='Multifunctional asynchronous python database',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/DwZZd/Mekanism',
  packages=find_packages(),
  install_requires=['requests>=2.25.1', 'asyncio>=3.4.3', 'aiofiles>=23.2.1'],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='database ',
  project_urls={
    'GitHub': 'https://github.com/DwZZd/Mekanism'
  },
  python_requires='>=3.8'
)