from setuptools import setup, find_packages

setup(
    name="throttle-loader",
    version="0.1.0",
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=[],
    author="Bryan Antoine",
    author_email="b.antoine.se@gmail.com",
    description="A simple progress loader for Python",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/bantoinese83/throttle",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'throttle=throttle.cli:main',
        ],
    },
)