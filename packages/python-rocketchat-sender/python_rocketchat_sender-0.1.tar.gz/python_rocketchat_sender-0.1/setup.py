from setuptools import setup, find_packages

setup(
    name='python_rocketchat_sender',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests'
    ],
    description='Send Rocket Chat messages to your server',
    author='Gerardo Mathus',
    author_email='gerardo@hybridge.education',
    url='https://github.com/hybridgeeducation/python-rocketchat-sender',  
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)
