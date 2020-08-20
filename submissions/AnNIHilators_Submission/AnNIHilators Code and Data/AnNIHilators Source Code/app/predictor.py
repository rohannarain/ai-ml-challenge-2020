import re
import boto3
import ktrain
import os
import numpy as np
from botocore import UNSIGNED
from botocore.client import Config

import shutil
import requests
import base64

import docx2txt
from pdfminer.high_level import extract_text

def parse_pdf(filename):
    extracted_str = extract_text(filename)
    clauses_full = extracted_str.splitlines()
    clauses = [i for i, l in enumerate(extracted_str.splitlines()) if len(l.split()) >= 6]
    return clauses, clauses_full

def parse_docx(filename):
    extracted_str = docx2txt.process(filename)
    clauses_full = extracted_str.splitlines()
    clauses_indices = [i for i, l in enumerate(extracted_str.splitlines()) if len(l.split()) >= 6]
    return clauses_indices, clauses_full

def preprocess_file(payload):
    payload = payload['file']
    global upload_folder
    file_obj = payload.file
    upload_folder = open(payload.filename, 'wb+')
    shutil.copyfileobj(file_obj, upload_folder)
    upload_folder.close()
    print("Parsing document!")
    if re.search(r".docx$", payload.filename):
        clauses_indices, clauses_full = parse_docx(payload.filename)
    elif re.search(r".pdf$", payload.filename):
        clauses_indices, clauses_full = parse_pdf(payload.filename)
    os.remove(payload.filename)
    return clauses_indices, clauses_full

def preprocess_pdf(payload):
    payload = payload['pdf_file']
    print(payload[:10])
    print(len(payload))
    content = base64.b64decode(payload)
    with open('clauses_file.pdf', 'wb') as f:
        f.write(content)
    clauses_indices, clauses_full = parse_pdf("clauses_file.pdf")
    print(clauses_full)
    print(clauses_indices)
    os.remove("clauses_file.pdf")
    return clauses_indices, clauses_full


class PythonPredictor:
    def __init__(self, config):
        if os.environ.get("AWS_ACCESS_KEY_ID"):
            s3 = boto3.client("s3")
        else: 
            s3 = boto3.client("s3", config=Config(signature_version=UNSIGNED))

        # download the model
        os.mkdir("distilbert_predictor")
        s3.download_file("distilbert-predictor", "distilbert_predictor2/tf_model.h5", "distilbert_predictor/tf_model.h5")
        s3.download_file("distilbert-predictor", "distilbert_predictor2/config.json", "distilbert_predictor/config.json")
        s3.download_file("distilbert-predictor", "distilbert_predictor2/tf_model.preproc", "distilbert_predictor/tf_model.preproc")

        # initialize the model
        predictor = ktrain.load_predictor("distilbert_predictor", batch_size=6)
        self.predictor = predictor

    def predict(self, payload):
        print(type(payload))
        print(payload['file'].filename)
        print('pdf_file' in payload)
        if payload.get('pdf_file', 0):
            clauses_indices, clauses_full = preprocess_pdf(payload)
        else: 
            clauses_indices, clauses_full = preprocess_file(payload)

        # Run the prediction
        probs = self.predictor.predict_proba([c for i, c in enumerate(clauses_full) if i in clauses_indices])[:, 1]
        with_indices = {i:p for i, p in zip(clauses_indices, probs)}
        probs_full = [with_indices.get(i, -1) for i in range(len(clauses_full))]
        # Probability that each clause is acceptable 
        res = [{"clause": c, 
                "probability_acceptable": 1 - p if p != -1 else -1, 
                "prediction": int(p > 0.5) if p != -1 else -1}
                for p, c in zip(probs_full, clauses_full)]

        return res

