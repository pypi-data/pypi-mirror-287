from setuptools import setup, find_packages

setup(
    name="unsendme",
    version='0.1.6',
    description='An unsend library for python developers ',
    author='Harsh Bhat',
    author_email='harsh121102@gmail.com',
    packages=find_packages(),
    install_requires=[
        # Add any dependencies your SDK requires
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
