from setuptools import setup, find_packages

setup(
    name='my_proofpoint_lib',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    include_package_data=True,
    description='A Python library for interacting with Proofpoint APIs',
    author='Your Name',
    url='https://github.com/eaobserveit/Policy-Packs/my_proofpoint_lib',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
