from setuptools import setup, find_packages

setup(
    name='opc_full_connect',
    version='0.1.0',
    description='A Python library for connecting to OPC UA servers with OpenSSL support.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Zmeypp/opcua_access',
    author='Zmeypp',
    author_email='lmayel@gmail.com',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'asyncua==1.1.0',
        'opcua==0.98.13'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires='>=3.6',
    include_package_data=True,
)
