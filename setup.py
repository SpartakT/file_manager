from setuptools import setup, find_packages

setup(
    name="file-manager",
    version="1.0.0",
    description="CLI утилита и GUI для управления файлами",
    author="SpartakT",
    author_email="doct.spartak@gmail.com",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'fm = filemanager.cli:main',
            'fm-gui = filemanager.gui:run',
        ],
    },
    python_requires=">=3.6",
    install_requires=[
        "flet>=0.83.0",
    ],
)