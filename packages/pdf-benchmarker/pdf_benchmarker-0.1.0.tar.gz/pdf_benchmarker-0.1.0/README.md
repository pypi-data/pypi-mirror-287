# PDF Scraper Benchmark Tool

## Overview

The PDF Scraper Benchmark Tool is designed to evaluate and compare the performance of various PDF scraping libraries and command-line tools. This tool measures various metrics such as speed, accuracy, and resource usage, helping users select the best tool for their specific needs.

## Features

- **Multiple Scraper Support:** Integrates with popular Python libraries and command-line PDF scraping tools.
- **Extensible:** Easily add new scrapers via a simple plugin system.
- **Metrics Evaluation:** Benchmarks tools based on performance, accuracy, and efficiency.
- **CLI Interface:** Provides a user-friendly command-line interface for running benchmarks and generating reports.

### Prerequisites

The application can be used as an executable container. If you would like to use the the application
in this way, you will need to have Docker installed. Instructions for installing Docker on various platforms can be found [here](https://docs.docker.com/engine/install/).

If you choose to run the application locally you will need the following dependencies:

#### Core Dependencies

- Python 3.10+ and pip
- [pipx](https://pipx.pypa.io/stable/)
- [poetry](https://python-poetry.org/)
- gcc and build-essentials for building C based libraries

#### Java

The Tika and PDFBox are both Java based applications. If you plan on using those tools
you will need to have Java installed. Installation instructions for openjdk are [here](https://openjdk.org/install/).

#### Tesseract

In order to use the tesseract scraper you must have tesseract installed on your system. Instructions
for installation can be found [here](https://tesseract-ocr.github.io/tessdoc/Installation.html).

## Installation

To run the application locally on a Windows 11 machine, follow the setup instructions provided [here](#windows-setup). For other operating systems, please refer to the instructions below:

Clone the repository

```bash
git clone https://github.com/the-merge/pdf-benchmarker.git
cd pdf-benchmarker
```

Install dependencies with poetry

```bash
poetry install
poetry run python -m spacy download en_core_web_sm  # download the model for entity and predicate metrics
```

Copy the `.env.sample` to `.env`

```bash
cp .env.sample .env
```

Update `.env` with your environment variables

### Code Formatting

This project uses [`black`](https://black.readthedocs.io/en/stable/index.html) to format the code
and perform linting checks. Black integrates with many editors to automatically format
code on save. A list of supported editors and instructions for how to integrate this with your favorite tools
can be found [here](https://black.readthedocs.io/en/stable/integrations/editors.html).

Formatting can also be handled via pre-commit hooks. The `pre-commit` can be used to
install the hook:

```bash
poetry run pre-commit install
```

After the commit hook has been installed your code will be reformatted as part of your
commit workflow.

## Usage

### Python

This application uses Click to make this a command line interface.

Scrape a single file:

```bash
poetry run python -m src.pdf_benchmarker.cli pdf-benchmarker --scraper pdfminer --file "data/sample_pdfs/2404.10260.pdf" --output "data/output/pdfminer/2404.10260.txt" --overwrite
```

Replace pdfminer with the name of the scraper you want to use, and update the path to the pdf file you want to scrape.

Evaluate a single file:

```bash
poetry run python -m src.pdf_benchmarker.cli evaluate --metric cosine_similarity --scraped-file "data/output/pdfminer/2404.10260.txt" --ground-truth-file "data/sample_txts/2404.10260.txt"
```

Replace cosine_similarity with the name of the metric you want to use, and update the path to the scraped & ground truth text files.

Scrape and evaluate all files:

```bash
poetry run python -m src.pdf_benchmarker.cli evaluate-all
```

Alternatively run the python commands above through a text user interface:

```bash
poetry run python -m src.pdf_benchmarker.cli tui
```

### Docker
(From within the pdf-benchmarker directory)

To build the image: `docker build -t pdf-benchmarker .`

Scrape a single file:
(Replace pdfminer with the name of the scraper you want to use, and update the path to the pdf file you want to scrape.)
```bash
docker run \
  --rm \
  -v "${PWD}/data":/app/data \
	pdf-benchmarker \
	pdf-benchmarker \
	--scraper pdfminer \
	--file "data/sample_pdfs/embedded-images-tables.pdf“ \
	--output "data/output/pdfminer/embedded-images-tables.txt"
```

Evaluate a single file:
(Replace cosine_similarity with the name of the metric you want to use, and update the path to the scraped & ground truth text files.)
```bash
docker run \
  --rm \
  -v "${PWD}/data":/app/data \
	pdf-benchmarker \
	evaluate \
	--metric cosine_similarity \
	--scraped-file "data/output/pdfminer/2404.10260.txt" \
	--ground-truth-file "data/sample_txts/2404.10260.txt"
```

Scrape and evaluate all files:
```bash
docker run --rm -v "${PWD}/data":/app/data pdf-benchmarker scrape-all
docker run --rm -v "${PWD}/data":/app/data pdf-benchmarker evaluate-all
```

## Adding New Scrapers

To add a new scraper:

Implement the scraper class in src/scraper/scrapers.py adhering to the ScraperInterface.
Add the scraper to the factory in src/scraper/scraper_factory.py.

## Streamlit

Run with: `poetry run streamlit run src/pdf_benchmarker/streamlit/streamlit_app.py`

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## Windows Setup

By following these steps, you should be able to set up and run the project on a Windows 11 machine using a Miniconda environment.

#### Prerequisites

Install Miniconda
Download and install Miniconda by following the [instructions](https://docs.conda.io/en/latest/miniconda.html) on the official website. Ensure that the following paths are acce

```bash
  git clone https://github.com/yourusername/yourproject.git
  cd yourproject
```

Add Miniconda to the Windows `PATH` environment variable.

```bash
C:\Users\<username>\Miniconda3
C:\Users\<username>\Miniconda3\Scripts
C:\Users\<username>\Miniconda3\Library\bin
```

#### Step-by-Step Setup Guide

Create a new conda environment for the project and activate it. Replace `env_name` with your desired environment name:

```bash
  conda create --name env_name python=3.11
  conda activate env_name
```

Install pipx:

```bash
  conda install pipx
  pipx ensurepath
  # restart terminal after installation.
  pipx --version # check if install is successful
```

Install poetry:

```bash
  pipx install poetry
  # restart terminal after installation
  poetry --version # check if install is successful
```

Add Poetry to Windows `PATH` environment variable. Replace `<username>` with your user name. E.g.

```bash
C:\Users\<username>\pipx\venvs\poetry
```

Install the project dependencies specified in the `pyproject.toml` file:

```bash
  poetry install
  poetry run python -m spacy download en_core_web_sm  # download the model for entity and predicate metrics
```

Copy the `.env.sample` to `.env`. Update `.env` with your environment variables.
```bash
cp .env.sample .env
```

**Verify the Installation**
Verify that all dependencies are installed correctly and the environment is set up by running:

```bash
poetry run python -m src.pdf_benchmarker.cli evaluate --metric cer --scraped-file "data/output/pdfminer/2404.10260.txt" --ground-truth-file "data/sample_txts/2404.10260.txt"
```

## Test Coverage

This project uses [`Coverage.py`](https://coverage.readthedocs.io) to generate test coverage reports.

First, run the test suite with coverage enabled:

```bash
poetry run coverage run -m pytest
```

Next, generate a simple coverage report:

```bash
poetry run coverage report
```

You can optionally generate an HTML-based report, which allows you to click on individual files to see line-by-line coverage:

```bash
poetry run coverage html
```

Open the HTML file in your browser to view:

```bash
open htmlcov/index.html
```
You can add a command-line option that allows parsing all documents for a specific parser, 
you can modify the scrape_all command to accept a scraper parameter. 
This way, you can either run all scrapers or a specific one.
Added an option --scraper to the scrape_all command
```bash
poetry run python -m src.pdf_benchmarker.cli scrape-all --scraper pdfminer
```
