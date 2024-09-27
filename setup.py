from setuptools import setup, find_packages

setup(
    name='treemaker',
    version='0.1',
    author='Nnamdi Michael Okpala',
    author_email='okpalan@protonmail.com', 
    description='A tool for creating directory structures from a specified tree format.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/okpalan/treemaker',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
