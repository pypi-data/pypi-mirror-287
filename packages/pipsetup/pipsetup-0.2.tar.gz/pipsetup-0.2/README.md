# pipsetup

`pipsetup` is a Python tool for generating a structured project template, making it easier to set up and start new Python projects. It automates the creation of essential project files and directories, streamlining the setup process.

[![Publish](https://github.com/leonardogonzalolaura/workspace_setup_pip/actions/workflows/publish.yml/badge.svg)](https://github.com/leonardogonzalolaura/workspace_setup_pip/actions/workflows/publish.yml)
 
 ![PyPI version](https://img.shields.io/pypi/v/pipsetup.svg)

## Features

- Generate a standard Python project structure.
- Create essential files such as `setup.py`, `setup.cfg`, `README.md`, `LICENSE`, and `MANIFEST.in`.
- Customize the project structure with user-defined project names, author names, and email addresses.

## Installation

You can install `pipsetup` via PyPI (Python Package Index). Use the following command:

```sh
pip install pipsetup
```

## Usage

After installing `pipsetup`, you can use it directly from the command line to create a new project. The command format is as follows:

```bash
pipsetup <project_name> <autor> <email>
```

## Parameters

- `<project_name>`: The name of the new project you want to create.
- `<autor>`: The author of the project.
- `<email>`: The email address of the author.

## Example

To create a new project named `my_new_project` with the author `John Doe` and email `john.doe@example.com`, run the following command:

```bash
pipsetup my_new_project "John Doe" john.doe@example.com
