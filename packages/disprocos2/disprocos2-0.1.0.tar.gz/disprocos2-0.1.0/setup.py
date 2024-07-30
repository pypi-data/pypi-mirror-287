from setuptools import setup, find_packages

setup(
    name='disprocos2',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'disprocos2 = disprocos2:main',
        ],
    },
    author='YN',
    author_email='emory@ex.edu.com',
    description='process the estimation of genetic distance',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
