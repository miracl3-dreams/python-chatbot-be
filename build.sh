#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Download NLTK punkt data
python -m nltk.downloader punkt
