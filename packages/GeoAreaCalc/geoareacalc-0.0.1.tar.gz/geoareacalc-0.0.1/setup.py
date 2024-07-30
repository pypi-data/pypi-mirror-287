from setuptools import setup, find_packages


def readme():
    with open('README.md', 'r', encoding='UTF-8') as f:
        return f.read()


setup(
  name='GeoAreaCalc',
  version='0.0.1',
  author='Qiaxx',
  author_email='belozertsev04@mail.ru',
  description='This library calculates the area of shapes',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/Qiaxx/GeoAreaCalc',
  packages=find_packages(),
  install_requires=[],
  classifiers=[
    'Programming Language :: Python :: 3.12',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='calculate, area, geometry, shape',
  project_urls={
    'GitHub': 'https://github.com/Qiaxx/GeoAreaCalc'
  },
  python_requires='==3.12'
)