# self-updating-program
A self-updating cross-platform application made as a coding challenge

[![Build Status](https://api.cirrus-ci.com/github/BGR360/self-updating-program.svg)](https://cirrus-ci.com/github/BGR360/self-updating-program)


## Getting Started


### Installation

`self-updating-app` is a proper Python package: it can be installed via `pip`:

```
$ python3 -m venv env
(env) $ pip install git+https://github.com/BGR360/self-updating-program.git
```

To install a specific version, such as `1.0.0`, specify it using `@`:

```
$ pip install git+https://github.com/BGR360/self-updating-program.git@1.0.0
```

This will also work with a branch name or a commit hash.

### Updating

If your installed version of `self-updating-app` is out of date, it will prompt you to update the next time you start it:

```
$ self-updating-app
There is a new version available (v0.7.4).
Would you like to update? [Y/n]
```

If you select `yes`, then the app will invoke `pip` to upgrade your current installation, and the updated version will be available the next time you run the app. You could also run `pip` manually:

```
$ pip install --upgrade self-updating-app
```


### Usage

```
Usage: self-updating-app [OPTIONS]

Options:
  --install-version TEXT  Install a specific version of the program (for
                          testing).
  -y, --yes-update        Automatically agree to any updates.
  -n, --no-update         Do not check for updates.
  --version               Show the version and exit.
  -h, --help              Show this message and exit.
```


### Contributing

To contribute, fork the repository and make a pull request to the `develop` branch. Once your PR is merged, I will publish a new Release, and all installed instances will prompt their users to update the app the next time it is launched.



## How it Works


### Packaging and Distributing the Application

I use the python package [PBR](https://pypi.org/project/pbr/) to handle packaging the application. PBR is a wrapper around python's [setuptools](https://setuptools.readthedocs.io/en/latest/) that makes things a little cleaner to use and also offers nice features like [automatic version detection](#automatic-version-detection).

Python's setuptools is what is used to publish and distribute PyPi (pip) packages. A really handy feature of `pip` that I utilized in this project is that you can install python packages from GitHub repositories.


### Versions and Updating

#### Automatic Version Detection

Typically, when writing a `setuptools` package, one must explicitly code the version number into `setup.py`. Instead, PBR can automatically infer the package's version via `git` tags in the local/remote repository, and the detected version will be bundled into the package at installation time.

PBR is also included as a runtime dependency of `self-updating-app` so it can know its version at runtime and compare it to the latest version on GitHub.

#### Checking for Updates

`self-updating-app` makes a simple HTTP request to the GitHub API's `/releases` endpoint to grab the latest Release version from the GitHub repository. If the version is greater than the local version, it prompts the user to update the application.


### Continuous Integration

I chose to use [Cirrus CI](https://cirrus-ci.org/) for continuous integration testing. I originally chose Cirrus over [Circle CI](https://circleci.com/) because Circle CI does not offer Mac OS testing for free. However, looking back, I think Circle CI may have been the better choice; I found Cirrus CI to be clunky and somewhat young, and didn't actually get around to running CI/CD on Mac instances.

#### CI Tasks

On every commit, Cirrus CI runs the `Build and Run` task, which simply packages the source tree up using `setup.py` and runs `self-updating-application` to see if it works.

On every Pull Request, an extra task runs: `Install from GitHub`. This attempts to `pip install` the package directly from GitHub using the latest commit hash, with no source code present (it skips the `git clone` step that all CI tasks have by default).

Finally, whenever a Release is published on GitHub, two more tasks run:
 * `Install from GitHub and Check Version`:
   * Runs `pip install` to install the latest released version from GitHub.
   * Runs `self-updating-app --version` and checks that it is the same as the tag_name of the Release that triggered the task.
 * `Install Previous Version and Self-Update`:
   * Queries the GitHub `/releases` API to detect what the second-to-latest released version is.
   * Runs `pip install` to install that version.
   * Runs `self-updating-app --yes-update`.
   * Ensures that the application actually updated itself to the most recent version by running `self-updating-app --version`.
