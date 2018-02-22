from setuptools import setup


def readme():
    with open('README') as f:
        return f.read()


setup(name='pypcaxilink',
      version='0.1',
      description='python driver for the pcaxilink FPGA libraries',
      long_description=readme(),
      url='None',
      author='Jennifer Holt',
      author_email='jholt1978@gmail.com',
      license='MIT',
      packages=['pypcaxilink'],
      install_requires=[
      ],
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['nose'])
