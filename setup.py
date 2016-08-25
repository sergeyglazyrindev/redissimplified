import sys

# dirty hack, always use wheel
sys.argv.append('bdist_wheel')

from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name='redis-beautified-ext',
    version='0.1',
    description='Redis extension to beautify access to redis data types.',
    long_description=readme(),
    classifiers=[
        'Development Status :: 0.1 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Topic :: NoSQL',
    ],
    url='https://github.com/sergeyglazyrindev/redisbeautifiedext',
    author='Sergey Glazyrin',
    author_email='sergey.glazyrin.dev@gmail.com',
    license='MIT',
    package_dir={'': 'src'},
    packages=['redisext', ],
    include_package_data=True,
    zip_safe=False,
    extras_require={
        'testing': ['nose', 'mock'],
    },
    test_suite='tests',
    install_requires=['redis==2.10.5', ]
)
