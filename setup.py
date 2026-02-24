from setuptools import setup, find_packages

setup(
    name="my_file-manager",
    version="1.0.0",
    description="CLI утилита для управления файлами",
    author="SpartakT",
    author_email="doct.spartak@gmail.com",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'fm = filemanager.cli:main',
        ],
    },
    python_requires=">=3.6",
    install_requires=[],
)