# 🏥 MediBot - AI-Powered Medical Chatbot

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![NLP](https://img.shields.io/badge/NLP-spaCy%20%7C%20NLTK-green.svg)](https://spacy.io)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> **⚠️ Medical Disclaimer:** This chatbot is  for educational and research purposes only. Not intended for medical diagnosis or treatment. Always consult qualified healthcare professionals.
 
## 📋 Table of Contents 
- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Architecture](#architecture)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [API Endpoints](#api-endpoints)
- [Performance](#performance)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

MediBot is an intelligent medical chatbot that leverages Natural Language Processing (NLP) to:
- Analyze patient symptoms from natural language input
- Predict possible medical conditions
- Recommend appropriate specialists
- Provide health information and first-aid suggestions

**Accuracy:** 85%+ on test dataset | **Response Time:** <2 seconds

## ✨ Features

### Core Capabilities
- ✅ **Symptom Analysis** - Extract symptoms from free-text descriptions
- ✅ **Disease Prediction** - ML-based classification of 50+ conditions
- ✅ **Specialist Recommendation** - Match diseases to medical specialists
- ✅ **Multi-format Input** - Text and voice (speech-to-text) support
- ✅ **Conversational Memory** - Remembers context within a session

### Technical Features
- 🔍 **NLP Pipeline** - Tokenization, lemmatization, entity recognition
- 🧠 **ML Models** - Random Forest + SVM ensemble
- 💾 **Lightweight** - Runs locally, no cloud dependencies
- 🔒 **Privacy-First** - No patient data stored permanently

## 🛠️ Tech Stack

| Category | Technologies |
|----------|-------------|
| **Backend** | Python 3.8+, Flask/FastAPI |
| **NLP** | NLTK, spaCy, scikit-learn |
| **ML Models** | Random Forest, SVM, TF-IDF Vectorizer |
| **Database** | SQLite (lightweight) |
| **Frontend** | HTML5, CSS3, JavaScript / Streamlit |
| **Voice** | SpeechRecognition, pyttsx3 (TTS) |
| **Deployment** | Docker, GitHub Actions (CI/CD) |

## 🏗️ Architecture
