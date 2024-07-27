from setuptools import setup, find_packages

setup(
    name="titanium-proto",
    version="0.2.5",
    description="A Python library to generate C++ classes from JSON for working with structs.",
    author="Lucas D. Franchi",
    author_email="LucasD.Franchi@gmail.com",
    packages=find_packages(),
    package_data={
        'titanium-proto': ['titanium_proto/templates/*.jinja2'],
    },
    include_package_data=True,
    python_requires=">=3.7",
    entry_points={
        'console_scripts': [
            'titanium-proto = titanium_proto.titanium_proto:main',
        ],
    },
    extras_require={
        "dev": [
            "pytest >= 6.2.4",
            "pytest-cov >= 2.12.1",
            "coverage >= 5.5",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
