from setuptools import setup, find_packages

setup(
    name="pintl",
    version="0.1.0",
    packages=find_packages(),
    description="Python Internationalization Library",
    # long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Petri Lipponen",
    author_email="info@movesense.com",
    url="https://github.com/petri-lipponen-movesense/pintl",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
    install_requires=[],
    include_package_data=True,
)