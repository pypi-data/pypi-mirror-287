from setuptools import setup, find_packages

setup(
    name='remote_config_fetcher',
    version='0.1.1',
    author='Steven Anaya',
    author_email='stvanayar@gmail.com',
    description='A package to fetch Firebase RemoteConfig values',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/colo-o',
    packages=find_packages(),
    install_requires=[
        'firebase-admin',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
