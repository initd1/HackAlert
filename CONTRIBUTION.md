# Contributing to HackAlert

Thank you for your interest in contributing to HackAlert! We appreciate your help in making our product better and more secure.
## About HackAlert

HackAlert is a tool that scans the internet for your online persona, including financial, social, and personal accounts, to detect data breaches or hacks. With real-time notifications via text or email, you can take action before it's too late. **Stay safe and secure with HackAlert.**
## Technical Development Guidelines
### Branch Naming Conventions

When creating branches, please follow these naming conventions:

  - `feature/<feature-name>` for new features
  - `enhancement/<enhancement-name>` for improvements to existing features
  - `bug/<bug-name> `for bug fixes

### Git Branch Management

  1. Create a new branch for each issue and work on the feature/bug in that branch.
  2. Merge your completed feature/bug branch into the main branch via a pull request.
  3. The main branch is a protected branch and requires approval of pull requests from feature/bug branches before being merged.
  4. When a good number of features are implemented and merged into main, a separate release branch is created from main.
  5. The release branch follows the Semantic Versioning naming convention https://semver.org/. A normal version number MUST take the form X.Y.Z where X, Y, and Z are non-negative integers, and MUST NOT contain leading zeroes. X is the major version, Y is the minor version, and Z is the patch version. Each element MUST increase numerically. For instance: 1.9.0 -> 1.10.0 -> 1.11.0.6.
  6. A tag by the same name will be created post-release.
  7. The release branch will be locked and serve as the Last Known Good for any future work.

### Environment Set-up

To set up your development environment, please follow these steps:

1. Clone the GitHub repository

```bash

git clone https://github.com/initd1/HackAlert.git
```
2. Install Python and pip in your environment

3. Install **virtualenv**

```bash
pip install virtualenv
```
4. Create a virtual environment

```bash

virtualenv <environment-name>
```
5. Activate the virtual environment

__Mac or Linux__

```bash

source <environment-name>/bin/activate
```
__Windows__

```bash

<environment-name>\Scripts\activate.bat
```
6. Install the required packages in the virtual environment

```python

    pip install -r requirements.txt
```
## Testing

It is important that before you do anything, you have the `requirements.txt` file installed as it is required for the dependencies that are used in this project.

To install all dependencies listed in this file, run the following:

```bash

python -m pip install -r requirements.txt
```
To execute tests, please ensure that you have the **pytest** module installed. The **unittest** module is used, however, this is native to Python and does not have to be installed.

To run tests, please ensure that you are in the base directory, where `tests` and `main.py` are visible.

To run tests with print output:

```bash

pytest -s
```
To run tests without print output:

```bash

pytest
```
## Docker Containerization

We suggest packaging the code in a lightweight Docker container like python-slim and running the code from it. That way, the environment is set and can be run from any environment that supports Docker.
