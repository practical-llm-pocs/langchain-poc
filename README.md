![Pipeline Status](https://github.com/practical-llm-pocs/langchain-poc/actions/workflows/python-app.yml/badge.svg)
[![Coverage Status](https://codecov.io/gh/practical-llm-pocs/langchain-poc/branch/main/graph/badge.svg)](https://codecov.io/gh/practical-llm-pocs/langchain-poc)


# Quick Start

## Dependencies

- Git
- Git LFS (https://git-lfs.com/)
- (Optional) pyenv (https://github.com/pyenv/pyenv#getting-pyenv)
- Python >=3.8 (`pyenv install`)
- poetry (`pip install poetry`)


# Development

## Dual CLI/API framework

This project is set up as a dual CLI/API framework, 
allowing you to use the same core functionality through both a command-line interface and a REST API. 
It utilizes FastAPI for the API layer and Click for the CLI layer, with shared functions in the `src/core` directory.

### API Examples:

1. Start the API server:

```bash
poetry run start --reload
```

2. Access the API endpoints using a web browser, curl, or a REST client:

```bash
curl http://127.0.0.1:3000/hello
curl http://127.0.0.1:3000/hello/Doge
```


### CLI Examples:

```bash
# poetry run hello
Hello World!

# poetry run hello Doge
Hello Doge!
```


# Deployment

## Serverless

The project is set up to use serverless on AWS using [default] profile.
To install serverless, go to https://www.serverless.com/framework/docs/getting-started#installation

```bash
# Deploy changes
serverless deploy

# View deployed endpoints and resources
serverless info

# Invoke deployed functions
serverless invoke
```

