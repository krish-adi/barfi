# Developer Notes

Following are the developer notes on getting started to contributing to the development of Barfi.

## Requirements

### Development Environment

-   Clone this repo to a local folder.
-   Python version is managed by [Pyenv](https://github.com/pyenv/pyenv): Base Python version currently is: `3.8.19`
-   Python dependencies and packaging is done using [Poetry](https://python-poetry.org/).
-   Frontend GUI environement is managed using [NVM](https://github.com/nvm-sh/nvm). Base Node version currently is: `v18.18.2`
-   If you are using a Mac, get started by installing dependencies using [Homebrew](https://brew.sh/), and continue to the following:

    -   Install Pyenv and Python using: `brew install pyenv` -> `pyenv install 3.8.19`
    -   Find the location where `Python 3.8.19` install using -> `pyenv which python`
    -   Install Poetry and activate environement: `brew install poetry` -> `cd <barfi-git-repo>` -> `poetry env use <python-3.8.19-location>` -> `poetry install`
    -   Install NVM using [these instructions](https://github.com/nvm-sh/nvm?tab=readme-ov-file#installing-and-updating) and then Node using `nvm install 18.18.2` -> `nvm use 18.18.2`.
    -   Install ui depdendencies by: `cd ui-flow` -> `npm install`

## Quickstart for development

-   To run the ui-flow in local development mode set `RELEASE = False` in `src/barfi/config.py`
-   Open 2 terminals, one for starting the Python env and the other for the UI env.
-   In terminal 1: `make serve-ui`
-   In terminal 2: `make serve-barfi`

## Checklist for building and uploading new package

-   [ ] Update Dcoumentation if required.
-   [ ] Run tests using `make tests`
-   [ ] Build the ui-flow: `cd build-ui`
-   [ ] Check `RELEASE = True` is set in `src/barfi/config.py`
-   [ ] Check linting and formatting: `make ruff`
-   [ ] Bump version number as required in `pyproject.toml`
-   [ ] Update CHANGELOG
-   [ ] Build and upload package using `make build-upload`
-   [ ] Commit the repository with the version number example: `v 1.0.0`
