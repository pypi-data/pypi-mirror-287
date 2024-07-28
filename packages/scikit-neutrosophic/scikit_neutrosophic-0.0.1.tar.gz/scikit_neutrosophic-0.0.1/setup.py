from setuptools import setup, find_packages
import pathlib

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name='scikit-neutrosophic',
    version='0.0.1',
    description='Neutrosophic Machine Learning Algorithms',
    long_description=README,
    long_description_content_type='text/markdown',
    author='Gyanendra Chaubey',
    author_email='gyanendrachaubey68@gmail.com',
    url='https://github.com/GyanendraChaubey/scikit-neutrosophic',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scipy',
        'scikit-learn'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires='>=3.6',
)
