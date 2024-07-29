from setuptools import setup, find_packages

setup(
    name='neuralviz',
    version='0.5.0',
    description='A package for visualizing neural network training and decision boundaries.',
    author='Jit Roy',
    author_email='your.email@example.com',
    packages=find_packages(include=['nn_visualizer', 'nn_visualizer.*']),
    install_requires=[
        'matplotlib',
        'numpy',
        'torch',
        'seaborn',
        'scikit-learn'
    ],
    python_requires='>=3.6',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)