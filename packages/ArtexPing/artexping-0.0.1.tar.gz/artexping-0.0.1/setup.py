from setuptools import setup, find_packages

setup(
    name='ArtexPing',
    version='0.0.1',
    author='Artex AI',
    description='A python internet status checking library',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/JunaidParkar/Python-Check_internet_status/',
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
        'requests==2.32.3'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Boost Software License 1.0 (BSL-1.0)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    project_urls={
        'Documentation': 'https://github.com/JunaidParkar/Python-Check_internet_status/',
        'Source': 'https://github.com/JunaidParkar/Python-Check_internet_status/',
        'Tracker': 'https://github.com/JunaidParkar/Python-Check_internet_status/',
    },
)