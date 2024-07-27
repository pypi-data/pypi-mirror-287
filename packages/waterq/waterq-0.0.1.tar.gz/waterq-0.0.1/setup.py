import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="waterq",
    version="0.0.1",
    author="yoshiyasu takefuji",
    author_email="takefuji@keio.jp",
    description="waterq for detecting water quality anomalities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/y-takefuji/water",
    project_urls={
        "Bug Tracker": "https://github.com/y-takefuji/water",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    py_modules=['waterq'],
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
    entry_points = {
        'console_scripts': [
            'waterq = waterq:main'
        ]
    },
)
