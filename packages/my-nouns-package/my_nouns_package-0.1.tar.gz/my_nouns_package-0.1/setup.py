from setuptools import setup, find_packages

setup(
    name='my_nouns_package',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    description='A package to load and use a list of nouns.',
    author='Muhammad Shoaib Tahir',
    author_email='shoaibtahir410@gmail.com',
    url='https://github.com/MuhammadshoaibTahir/Punjabipiplibrary',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
