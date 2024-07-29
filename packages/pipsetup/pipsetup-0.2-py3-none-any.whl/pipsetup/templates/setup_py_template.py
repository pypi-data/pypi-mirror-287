from setuptools import setup, find_packages
import setuptools_scm

setup(
    name="{project_name}",
    use_scm_version=True,
    setup_requires=["setuptools>=42", "setuptools_scm"],
    packages=find_packages(include=['{project_name}', '{project_name}.*']),
    include_package_data=True,
    install_requires=['library_externals'],
    test_suite='tests',
    author="{author}",
    author_email="{email}",
    description="A simple example of a Python library",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/{author}/{project_name}",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)