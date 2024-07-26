from setuptools import setup, find_packages

setup(
    name='moneyunify',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests>=2.25.1',
    ],
    description='A Python client for the MoneyUnify API to simplify mobile money payments',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Lembani Sakala',
    author_email='lembanisakala@gmail.com',
    url='https://github.com/lembani/moneyunify_py',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
