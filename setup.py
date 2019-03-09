from setuptools import setup

setup(
    name='turtleproject',
    version='0.1',
    author_email='giacomo.tarroni@gmail.com',
    description='A simple version of the turtle graphics library',
    author='Giacomo Tarroni',
    packages=['simpleturtle'],
    install_requires=['graphics.py', 'numpy']
)
