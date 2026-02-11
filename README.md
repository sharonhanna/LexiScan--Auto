<u>LexiScan-Auto</u>

<u>Intelligent Legal Document Processing System</u>

<u>Overview</u>

LexiScan-Auto is an end-to-end Intelligent Document Processing (IDP) system that automatically extracts structured legal information from scanned and digital contract PDFs.
The system combines OCR, custom-trained Legal Named Entity Recognition (NER), and rule-based post-processing, and exposes the pipeline through a FastAPI REST service, with optional Docker-based deployment.

The project is designed to reduce manual contract review time by converting unstructured legal documents into structured, machine-readable JSON.

<u>Problem Statement</u>

Legal contracts are lengthy, complex, and time-consuming to analyze manually.
Organizations require automated systems to extract key information such as:

* **Parties involved**
* **Contract dates**
* **Monetary values**

LexiScan-Auto addresses this challenge using NLP-driven automation.

<u>Key Features</u>

* **Supports both scanned and digital PDFs**
* **OCR-based text extraction using Tesseract**
* **Custom Legal NER model trained on the CUAD dataset**
* **Hybrid extraction using NER + Regex-based validation**
* **Structured JSON output for downstream use**
* **REST API built using FastAPI**
* **Optional Dockerized execution**

<u>System Architecture</u>

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

<u>Technology Stack</u>

* **Programming Language:** Python
* **NLP Framework:** spaCy (custom-trained Legal NER)
* **OCR Engine:** Tesseract
* **API Framework:** FastAPI
* **Containerization:** Docker
* **Dataset:** CUAD (Contract Understanding Atticus Dataset)

<u>Project Structure</u>

LexiScan-Auto/
├── **api/**                 # FastAPI application
├── **ocr/**                 # OCR pipeline
├── **ner/**                 # NER training, inference & evaluation
├── **pipeline/**            # End-to-end execution pipeline
├── **models/**              # Trained spaCy Legal NER model
├── **utils/**               # Regex-based extractors & validators
├── **data/**                # Ignored dataset files
├── **Dockerfile**
├── **requirements.txt**
├── **README.md**
├── **sample_contract.pdf**
├── **sample_output.json**

<u>Running the Project Locally (Without Docker)</u>

1. **Install dependencies**
   pip install -r requirements.txt

2. **Start the API server**
   uvicorn api.app:app --reload

3. **Access Swagger UI**
   [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

<u>Running with Docker</u>

1. **Build Docker image**
   docker build -t lexiscan-auto .

2. **Run the container**
   docker run -p 8000:8000 lexiscan-auto

3. **Access API**
   [http://localhost:8000/docs](http://localhost:8000/docs)

<u>API Specification</u>

<u>Endpoint</u>

* **POST /extract**

<u>Input</u>

* **Upload a PDF file**
  OR
* **Provide raw contract text**

<u>Output (Sample)</u>

{
"status": "success",
"entities": {
"PARTY": ["Company A", "Company B"],
"DATE": ["12 March 2022"],
"AMOUNT": ["$500,000"]
}
}

<u>Model Evaluation</u>

The Legal NER model was evaluated using a validation sample.

<u>Metrics Used</u>

* **Precision**
* **Recall**
* **F1-score**

<u>Results</u>

* **Precision:** ~0.78
* **Recall:** ~0.75
* **F1-score:** ~0.76

F1-score is treated as the primary metric due to entity class imbalance and the importance of balanced extraction accuracy in legal NLP systems.

<u>Use Cases</u>

* **Legal contract analysis**
* **Compliance automation**
* **Due diligence support**
* **Enterprise document intelligence**
* **AI-powered legal assistants**

<u>Contributions</u>

<u>Work Done by Sharon Hanna</u>

- **Designed and implemented the OCR pipeline using Tesseract for both scanned and digital PDF contracts**
- **Integrated PDF ingestion and text extraction into the overall processing workflow**
- **Performed CUAD dataset ingestion, preprocessing, and annotation preparation**
- **Converted CUAD data into spaCy-compatible format for Legal NER training**
- **Trained a custom Legal Named Entity Recognition (NER) model using spaCy**
- **Implemented NER inference and evaluation using Precision, Recall, and F1-score metrics**
- **Built rule-based post-processing and validation logic for:**
  - **Date normalization and format validation**
  - **Monetary value validation**
  - **Termination clause detection**
- **Integrated NER and validation components into a structured JSON output format**
- **Developed the end-to-end extraction pipeline (OCR → NER → Validation → Structured Output)**
- **Prepared Docker configuration for containerized execution**
- **Created evaluation scripts, sample test inputs, and technical documentation**


<u>Contributors</u>

* **Sharon Hanna A**
* **Samyuktha Vijayakumar**
