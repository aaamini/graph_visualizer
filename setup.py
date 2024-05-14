from setuptools import setup, find_packages

setup(
    name='graph_visualizer',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'matplotlib',
        'colorcet',
        'torch-geometric'
    ],
    include_package_data=True,
    description='A package for visualizing graphs using 3d-force-graph.',
    author='Arash A. Amini',
    author_email='aaamini@ucla.edu',
    url='https://github.com/aaamini/graph_visualizer',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
