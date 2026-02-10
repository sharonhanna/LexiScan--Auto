LexiScan-Auto

Intelligent Legal Document Processing System

Overview

LexiScan-Auto is an end-to-end Intelligent Document Processing (IDP) system that automatically extracts structured legal information from scanned and digital contract PDFs.
The system combines OCR, custom-trained Legal Named Entity Recognition (NER), and rule-based post-processing, and exposes the pipeline through a FastAPI REST service, with optional Docker-based deployment.

The project is designed to reduce manual contract review time by converting unstructured legal documents into structured, machine-readable JSON.

Problem Statement

Legal contracts are lengthy, complex, and time-consuming to analyze manually.
Organizations require automated systems to extract key information such as:

Parties involved

Contract dates

Monetary values

LexiScan-Auto addresses this challenge using NLP-driven automation.

Key Features

Supports both scanned and digital PDFs

OCR-based text extraction using Tesseract

Custom Legal NER model trained on the CUAD dataset

Hybrid extraction using NER + Regex-based validation

Structured JSON output for downstream use

REST API built using FastAPI

Optional Dockerized execution

System Architecture
PDF Document
     ↓
OCR (Tesseract)
     ↓
Text Preprocessing
     ↓
Custom Legal NER (spaCy)
     ↓
Post-processing & Validation
     ↓
Structured JSON Output (FastAPI)

Technology Stack

Programming Language: Python

NLP Framework: spaCy (custom-trained Legal NER)

OCR Engine: Tesseract

API Framework: FastAPI

Containerization: Docker

Dataset: CUAD (Contract Understanding Atticus Dataset)

Project Structure
LexiScan-Auto/
├── api/                 # FastAPI application
├── ocr/                 # OCR pipeline
├── ner/                 # NER training, inference & evaluation
├── pipeline/            # End-to-end execution pipeline
├── models/              # Trained spaCy Legal NER model
├── utils/               # Regex-based extractors & validators
├── data/                # Ignored dataset files
├── Dockerfile
├── requirements.txt
├── README.md
├── sample_contract.pdf
├── sample_output.json

Running the Project Locally (Without Docker)
1. Install dependencies
pip install -r requirements.txt

2. Start the API server
uvicorn api.app:app --reload

3. Access Swagger UI
http://127.0.0.1:8000/docs

Running with Docker
1. Build Docker image
docker build -t lexiscan-auto .

2. Run the container
docker run -p 8000:8000 lexiscan-auto

3. Access API
http://localhost:8000/docs

API Specification
Endpoint
POST /extract

Input

Upload a PDF file
OR

Provide raw contract text

Output (Sample)
{
  "status": "success",
  "entities": {
    "PARTY": ["Company A", "Company B"],
    "DATE": ["12 March 2022"],
    "AMOUNT": ["$500,000"]
  }
}

Model Evaluation

The Legal NER model was evaluated using a validation sample.

Metrics Used

Precision

Recall

F1-score

Results

Precision: ~0.78

Recall: ~0.75

F1-score: ~0.76

F1-score is treated as the primary metric due to entity class imbalance and the importance of balanced extraction accuracy in legal NLP systems.

Use Cases

Legal contract analysis

Compliance automation

Due diligence support

Enterprise document intelligence

AI-powered legal assistants

Contributions:
Work Done by Sharon Hanna

Designed and implemented the complete OCR pipeline using Tesseract

Integrated PDF ingestion for both scanned and digital contracts

Performed CUAD dataset ingestion and preprocessing

Converted CUAD data into spaCy-compatible NER training format

Trained a custom Legal NER model using spaCy

Implemented NER inference and evaluation with Precision, Recall, and F1-score

Built rule-based post-processing and validation logic (regex + cleanup)

Developed the end-to-end extraction pipeline

Implemented FastAPI REST API for contract entity extraction

Structured output into clean JSON format

Prepared Docker configuration for containerized execution

Created documentation, sample inputs, and evaluation scripts

Contributors

Sharon Hanna A
Samyuktha Vijayakumar
