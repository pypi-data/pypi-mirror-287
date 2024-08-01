from setuptools import setup, find_packages

setup(
    name="preprocessmzML",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pyopenms",
        "numpy>=1.20,<1.24",
        "matplotlib",
    ],
    entry_points={
        'console_scripts': [
            'preprocess_mzml=preprocessmzML.main:main',
        ],
    },
    author="Bharath Nair",
    author_email="bharath@palaeome.org",
    description="A package for preprocessing mzML files for ZooMS analysis",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/bharathabnair/preprocessmzML",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
