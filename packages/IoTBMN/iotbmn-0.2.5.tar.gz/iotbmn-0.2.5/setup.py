from setuptools import setup, find_packages

setup(
    name='IoTBMN',
    version='0.2.5',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    author='Muntasir',
    author_email='muntasirthameem@gmail.com',
    description='A Python library for IoT communication with a serverlet',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Bliped-Pixel/IoTBMN',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

