[日本語版](https://github.com/opthub-org/opthub-runner-python/blob/main/README_ja.md) 👈

# opthub-runner-python

![Skills](https://skillicons.dev/icons?i=py,graphql,vscode,github)

opthub-runner-python is a Python package that provides Evaluator for local execution.

- Evaluator: Feature to evaluate solutions locally using Docker Image.

This repository describes how to install opthub-runner-python and use Evaluator.


## Getting Started
First of all, you need to set up the following environment settings in advance.

- Install Python 3.10 or newer.
- Set up pip for package management.
- Install and start Docker.*

\*For Mac users, you can install and start [Docker Desktop](https://docs.docker.com/desktop/install/mac-install/).


After completing the above environment setup, you can install `opthub-runner-python` from PyPI with the following command.

```bash
pip install opthub-runner-python
```

After installation, you can use the Evaluator class by importing it with Python code as follows.

```python
from opthub_runner.evaluator import Evaluator
```

For specific usage of the Evaluator class, please refer to [Usage Example](#usage), [Options](#option), and [Execution Results](#result).

Note that **Docker must be started** to run the code. It will not run properly unless Docker is started.


## Usage Example <span id="usage"></span>
Here is an example how to evaluate a solution using the Sphere function with the optimal solution as `[1, 1]` below.

```python
from opthub_runner.evaluator import Evaluator



evaluator = Evaluator("opthub/sphere:latest",
                      {"SPHERE_OPTIMA": [[1, 1]]}) # Initialize Evaluator

x = [0, 2] # Solution to evaluate
result = evaluator.run(x) # Evaluate

print(result) # {'objective': 2, 'feasible': None, 'constraint': None, 'info': None}
```

In the initialization of the Evaluator, the Docker Image `opthub/sphere:latest` of the Sphere function and the environment variable `SPHERE_OPTIMA` of the Docker process are set. The `run` method then starts the Docker process internally and evaluates the solution `[0, 2]`.

Information on the solutions input to the `run` method and the Docker image to be used are described in each problem on [OptHub](https://opthub.ai).

## Options <span id="option"></span>
The options used to initialize the Evaluator class are listed in the table below (* is required).

| Option | Type | Default Value | Description |
|----|----|----|----|
| docker_image* | str| - | Name of the Docker Image used for evaluation. |
| environment* | dict[str, object] | - | Environment variables. |
| rm | bool | True | Whether to remove the Docker Container after evaluation. |
|timeout | int | 43200 | Timeout for evaluation using Docker Image.　|

## Execution Results <span id="result"></span>
The `run` method of the Evaluator class returns the evaluation result. The evaluation result is represented by a dictionary object containing pairs of Key and the corresponding Value. The following table shows the Keys and the types of the Values corresponding to the Keys included in the evaluation result.

| Key | Type of Value | Description |
|----|----|----|
| objective | object | Objective function value of the solution. |
| feasible | bool or None | Feasibility of the solution. |
| constraint | object or None | Information on solution constraints. |
| info | object or None | Information on evaluation. |

Detailed descriptions of objective, constraint, feasible, and info are provided in each problem on [OptHub](https://opthub.ai).

## Troubleshooting
If you receive the following error, Docker is most likely not running. Please start Docker and re-run it. if you are Mac users, you can start Docker by launching Docker Desktop.

```shell
docker.errors.DockerException: Error while fetching server API version: ('Connection aborted.', FileNotFoundError(2, 'No such file or directory'))
```

## For Contributors

Follow these steps to set up the environment:

1. Clone this repository.
2. Set up Poetry.
3. Run `poetry install`.
4. Download the recommended VSCode Extensions.
5. Disable the following VS Code Extensions for this workspace to avoid conflicts with other packages:
    - ms-python.pylint
    - ms-python.black-formatter
    - ms-python.flake8
    - ms-python.isort

## Contact <a id="Contact"></a>

If you have any questions or concerns, please feel free to contact us (Email: dev@opthub.ai).

<img src="https://opthub.ai/assets/images/logo.svg" width="200">
