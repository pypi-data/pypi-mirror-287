from setuptools import setup, find_packages

setup(
    name='PN_DTW_FE',  # Replace with your unique package name
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'scipy',
        'fastdtw',
    ],
    entry_points={
        'console_scripts': [
            'PN_DTW_FE = PN_DTW_FE.main:main',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A package for gene expression analysis',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/PN_DTW_FE',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
