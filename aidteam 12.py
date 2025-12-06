import json
import random

diseases = {
    "influenza": ["fever", "cough", "body ache", "chills", "sore throat"],
    "common_cold": ["runny nose", "sneezing", "mild cough"],
    "covid-19": ["fever", "dry cough", "loss of taste", "fatigue"],
    "pneumonia": ["chest pain", "fever", "shortness of breath", "cough"],
    "diabetes": ["increased thirst", "frequent urination", "fatigue"],
    "hypertension": ["headache", "dizziness", "vision issues"],
    "heart_disease": ["chest pain", "sweating", "arm pain"],
    "asthma": ["wheezing", "chest tightness", "cough at night"],
    "migraine": ["severe headache", "nausea", "light sensitivity"],
    "urinary_tract_infection": ["burning urination", "urgency", "abdominal pain"],
    "gastroenteritis": ["diarrhea", "vomiting", "cramps"],
    "appendicitis": ["abdominal pain", "fever", "nausea"],
    "allergic_rhinitis": ["sneezing", "itchy eyes", "runny nose"],
    "bronchitis": ["persistent cough", "mucus", "chest discomfort"],
    "eczema": ["itchy skin", "red patches", "dry skin"],
    "anemia": ["fatigue", "pale skin", "dizziness"],
    "osteoporosis": ["bone pain", "back pain", "fractures"],
    "depression": ["sadness", "sleep problems", "loss of interest"],
    "anxiety": ["restlessness", "sweating", "rapid heartbeat"],
}

NUM = 30000
outfile = open("dataset_30k.jsonl", "w")

for _ in range(NUM):
    disease = random.choice(list(diseases.keys()))
    symptoms = random.sample(diseases[disease], random.randint(2, len(diseases[disease])))
    record = {
        "source": ", ".join(symptoms),
        "target": disease
    }
    outfile.write(json.dumps(record) + "\n")

outfile.close()
print("Dataset created: dataset_30k.jsonl")
