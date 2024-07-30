from setuptools import setup, find_packages

with open('README.rst') as f:
    long_description = f.read()

setup(
    name='wrh',
    version='0.6',
    long_description=long_description,
    long_description_content_type="text/x-rst",
    description='Package for CIV550 course and UofT.',
    url='https://wrh.civmin.utoronto.ca/',
    author='Mohammed Basheer',
    author_email='mohammedadamabbaker@gmail.com',
    install_requires=['click==8.1.7','pandas==2.2.0','numpy==1.26.4','scipy==1.12.0','platypus-opt==1.2.0','tables==3.9.2', 'pywr==1.26.0'],
    packages=find_packages(),
    package_data={
        'wrh': ['json/*.json'],
    },
    entry_points={
        'console_scripts': ['wrh=wrh.cli:start_cli'],
    },
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'Natural Language :: English'
    ]
)
