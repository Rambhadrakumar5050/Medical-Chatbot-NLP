import os
import xml.etree.ElementTree as ET
import re
import spacy
import networkx as nx
import pandas as pd

# Load NLP model
nlp = spacy.load("en_core_web_sm")

data_folder = "MedQuAD"

questions = []
answers = []

# 🔥 Load XML dataset (limited for speed)
folders = os.listdir(data_folder)[:5]

for folder in folders:
    folder_path = os.path.join(data_folder, folder)

    if os.path.isdir(folder_path):
        files = os.listdir(folder_path)[:10]

        for file in files:
            if file.endswith(".xml"):
                file_path = os.path.join(folder_path, file)

                tree = ET.parse(file_path)
                root = tree.getroot()

                for qa in root.iter("QAPair"):
                    q = qa.find("Question")
                    a = qa.find("Answer")

                    if q is not None and a is not None:
                        questions.append(q.text)
                        answers.append(a.text)

# Convert to DataFrame
df = pd.DataFrame({"question": questions, "answer": answers})

# Clean text
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    return text

df["question"] = df["question"].apply(clean_text)

# Extract entities
def extract_entities(text):
    doc = nlp(text)
    return [token.text for token in doc if token.pos_ in ["NOUN", "PROPN"]]

df["entities"] = df["question"].apply(extract_entities)

# Build Knowledge Graph
G = nx.Graph()

for i, row in df.iterrows():
    entities = row["entities"]
    answer = row["answer"]

    if not entities or pd.isna(answer):
        continue

    for ent in entities:
        if ent:
            G.add_edge(ent, answer)

print("Graph ready with nodes:", len(G.nodes()))

# Chatbot function
def chatbot_response(user_input):
    user_input = clean_text(user_input)
    entities = extract_entities(user_input)

    responses = []

    for ent in entities:
        if ent in G:
            responses.extend(list(G.neighbors(ent)))

    if responses:
        return responses[0]
    else:
        return "⚠️ Please consult a medical professional."