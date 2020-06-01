import os
from setuptools import find_packages, setup

VERSION = "0.0.1.dev1"

ROOT_PATH = os.path.abspath(os.path.dirname(__file__))


def get_requirements(env):
    with open("requirements-{}.txt".format(env)) as fp:
        return [x.strip() for x in fp.read().split("\n") if not x.startswith("#")]


install_requires = get_requirements("dev")

with open("README.md") as f:
    long_description = f.read()

print("Started!")

setup(
    name='demo',
    version=VERSION,
    description='Demo app for python aws click',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Varun Tomar',
    author_email='varuntomar2019@gmail.com',
    python_requires=">=3.6",
    package_dir={"": "src"}, # all distutils packages are under src
    packages=find_packages("src"), #  include all packages under src
    url="https://github.com/tomarv2/demo-python-aws-click",
    classifiers=[  # Optional: A list of strings describing the categories for the package.
        'Programming Language :: Python :: 3.6',
        'Operating System :: OS Independent',
    ],
    # setup_requires=['pytest-runner'], # Using setup_requires is discouraged in favor of PEP-518.
    tests_require=['pytest'], # If your project’s tests need one or more additional packages besides those needed to install it.
    install_requires=install_requires, # A string or list of strings specifying what other distributions need to be installed when this one is. 
    entry_points='''
        [console_scripts]
        demo=cli:entrypoint
    '''
)

print("Finished!")
