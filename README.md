![Pipeline Status](https://github.com/practical-llm-pocs/langchain-poc/actions/workflows/python-app.yml/badge.svg)
[![Coverage Status](https://codecov.io/gh/practical-llm-pocs/langchain-poc/branch/main/graph/badge.svg)](https://codecov.io/gh/practical-llm-pocs/langchain-poc)


# Quick Start

## Dependencies

- Git
- Git LFS (https://git-lfs.com/)
- (Optional) pyenv (https://github.com/pyenv/pyenv#getting-pyenv)
- Python >=3.9.16 (`pyenv install`)
- poetry (`pip install poetry`)
- Python packages (`poetry install`)
- Dependencies for custom tool curl_rss_tool (+ html2text + sumy)
  - html2text (`sudo apt install html2text`)
  - nltk data (`poetry run python -m nltk.downloader all`)
- Ollama
  - llama3 model, or other models used

## Env

Create a .env.local file, then update with your API keys.

```bash
cp .env.example .env.local
```


# Development

## Dual CLI/API framework

This project is set up as a dual CLI/API framework, 
allowing you to use the same core functionality through both a command-line interface and a REST API. 
It utilizes FastAPI for the API layer and Click for the CLI layer, with shared functions in the `src/core` directory.

### API Examples:

1. Start a ollama server:

```bash
ollama serve 
```

3. Start the API server:

```bash
poetry run start --reload
```

3. Access the API endpoints using a web browser, curl, or a REST client:

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


# Testing

```bash
poetry run test
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

