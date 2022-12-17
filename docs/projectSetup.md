# Project Setup

## Prerequisites

The project was setup using a cookie cutter template as provided for here:
<https://github.com/khuyentran1401/data-science-template>.

To set it up, do the following:

1. Install cookiecutter

    ```bash
    conda config --add channels conda-forge
    conda install cookiecutter
    ```

1. Build template

  ```bash
  cookiecutter https://github.com/khuyentran1401/data-science-template
  ```
## Set up the environment

1. Install [Poetry](https://python-poetry.org/docs/#installation)
2. Set up the environment:

    ```bash
    make activate
    make setup
    ```

## Install new packages

To install new PyPI packages, run:

```bash
poetry add <package-name>
```

## Run the entire pipeline

To run the entire pipeline, type:

```bash
dvc repo
```

## Version your data

Read [this article](https://towardsdatascience.com/introduction-to-dvc-data-version-control-tool-for-machine-learning-projects-7cb49c229fe0) on how to use DVC to version your data.

Basically, you start with setting up a remote storage. The remote storage is where your data is stored. You can store your data on DagsHub, Google Drive, Amazon S3, Azure Blob Storage, Google Cloud Storage, Aliyun OSS, SSH, HDFS, and HTTP.

```bash
dvc remote add -d remote <REMOTE-URL>
```

Commit the config file:

```bash
git commit .dvc/config -m "Configure remote storage"
```

Push the data to remote storage:

```bash
dvc push 
```

Add and push all changes to Git:

```bash
git add .
git commit -m 'commit-message'
git push origin <branch>
```

## Auto-generate API documentation

To auto-generate API document for your project, run:

```bash
make docs
```
