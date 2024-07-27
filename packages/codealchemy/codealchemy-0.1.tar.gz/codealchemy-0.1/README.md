# CodeAlchemy

`codealchemy` is a Python package that provides decorators for capturing the execution time of functions and creating log groups for functions. This package can be used to enhance logging and performance monitoring in your Python projects.

## Installation

You can install `codealchemy` using pip:

```sh
pip install codealchemy
```

## Usage

Here is how you can use the decorators provided by `codealchemy` in your Python code:

```python
from codealchemy import log_execution_time, log_group

@log_execution_time
@log_group("ExampleGroup")
def example_function():
    import time
    time.sleep(2)
    print("Function executed")

example_function()
```

### Decorators

- **`log_execution_time`**: This decorator logs the execution time of the decorated function.
- **`log_group(group_name)`**: This decorator logs entry and exit points of the decorated function, grouping logs under a specified group name.

## Development

If you want to contribute to the development of `codealchemy`, you can set up a development environment by following these steps:

1.  Clone the repository:
    ```sh
    git clone https://github.com/girishcodealchemy/codealchemy.git
    ```
2.  Navigate to the project directory:
    ```sh
    cd codealchemy
    ```
3.  Install the package in editable mode with development dependencies:
    ```sh
    pip install -e .[dev]
    ```

## Publishing to PyPI

This project uses GitHub Actions to automate the process of publishing the package to PyPI.

### GitHub Action Workflow

The GitHub Action is defined in `.github/workflows/publish-to-pypi.yml`. It triggers on new releases and performs the following steps:

1.  Checkout the code.
2.  Set up Python.
3.  Install dependencies (`setuptools`, `wheel`, `twine`).
4.  Build the package.
5.  Publish the package to PyPI using credentials stored in GitHub Secrets.

### Setting Up GitHub Secrets

To securely store your PyPI credentials, add the following secrets to your GitHub repository:

1.  `PYPI_USERNAME`: Your PyPI username.
2.  `PYPI_PASSWORD`: Your PyPI password.

### Creating a New Release

To trigger the GitHub Action and publish the package to PyPI:

1.  Navigate to your GitHub repository.
2.  Go to the `Releases` tab.
3.  Click `Draft a new release`.
4.  Fill in the release details (tag version, release title, description).
5.  Click `Publish release`.

The GitHub Action will automatically run and upload the package to PyPI.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more details.
