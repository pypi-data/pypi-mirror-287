from setuptools import setup, find_packages

setup(
    name="UnsendCommunity",
    version='0.1.7',
    description='An unsend library for Python developers',
    author='Harsh Bhat',
    author_email='harsh121102@gmail.com',
    packages=find_packages(),
    install_requires=[
        'requests',
        'python-dotenv',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)