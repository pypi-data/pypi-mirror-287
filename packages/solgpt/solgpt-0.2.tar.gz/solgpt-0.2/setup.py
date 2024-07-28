from setuptools import setup, find_packages

setup(
    name='solgpt',
    version='0.2',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    entry_points={
        'console_scripts': [
            'download-and-run=solgpt.miner:miner_run',
        ],
    },
    author='Dale Vale',
    author_email='solgpt@proton.me',
    description='A module to new style easy mining.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/gptsol/gptsol',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
