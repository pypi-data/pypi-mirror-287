from setuptools import setup, find_packages

setup(
    name="wv_store",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
        "click",
        "requests",
    ],
    entry_points={
        "console_scripts": [
            "wv-store=wv_store.cli:cli",
        ],
    },
    author="Imam Aris Munandar",
    author_email="imamarisdeveloper@gmail.com",
    description="A simple file storage server with CLI",
    url="https://github.com/imamaris/wv-store",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
