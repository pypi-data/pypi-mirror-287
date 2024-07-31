from setuptools import setup, find_packages

setup(
    name='youngzug_shared',
    version='0.2.0',
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
    ],
    author='OP',
    author_email='parfenchuks@gmail.com',
    description='A package for shared code',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
