import setuptools

setuptools.setup(
    name="capsolver-async",
    version="0.1",
    author="Qunik",
    author_email="12.1pro2.04@gmail.com",
    description="async capsolver python libary",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/Qunik/capsolver_async",
    project_urls={
        "Bug Tracker": "https://github.com/Qunik/capsolver_async/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3"
    ],

    install_requires=[
        "httpx >= 0.27.0",
    ],
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    python_requires=">=3.10",

)