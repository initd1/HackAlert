# Contributing to HackAlert

Thank you for your interest in contributing to HackAlert! We appreciate your help in making our product better and more secure.

## About HackAlert

HackAlert is a tool that scans the internet for your online persona, including financial, social, and personal accounts, to detect data breaches or hacks. With real-time notifications via text or email, you can take action before it's too late. **Stay safe and secure with HackAlert.**

## Contribution Guidelines
1. Fork the HackAlert repository by clicking the "Fork" button on the top right of the project page.
2. Clone the repository to your local machine using the following command:
```
git clone https://github.com/<YOUR-GITHUB-USERNAME>/HackAlert
```
3. Install the project requirements
```
pip install -r requirements.txt
```
4. Install pre-commit hooks
```
pre-commit install
```
5. Create a new branch for your changes using the following command:
```
git checkout -b "branch-name"
```
6. Make your changes to the code.
> ### Environment Set Up
>- Install Python and pip in your environment
>- Install **virtualenv**
>
>```bash
>pip install virtualenv
>```
>- Create a virtual environment
>```bash
>virtualenv <environment-name>
>```
>- Activate the virtual environment
>
>__Mac or Linux__
>
>```bash
>
>source <environment-name>/bin/activate
>```
>__Windows__
>
>```bash
><environment-name>\Scripts\activate.bat
>```
>- Install the required packages in the virtual environment
>
>```python
>
>    pip install -r requirements.txt
>```

7. Add the changes to the staging area using the following command:
```
git add .
```
8. Commit the changes with a meaningful commit message using the following command:
```
git commit -m "your commit message"
```
9. Push the changes to your forked repository using the following command:
```
git push origin branch-name
```
10. Go to the GitHub website and navigate to your forked repository.
11. Click the "New pull request" button.
12. Select the branch you just pushed to and the branch you want to merge into on the original repository.
13. Add a description of your changes and click the "Create pull request" button.
14. Wait for the project maintainer to review your changes and provide feedback.
15. Make any necessary changes based on feedback and repeat steps 5-12 until your changes are accepted and merged into the main project.
16. Once your changes are merged, you can update your forked repository and local copy of the repository with the following commands:

```
git fetch upstream
git checkout master
git merge upstream/master
```
Finally, delete the branch you created with the following command:
```
git branch -d branch-name
```


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
