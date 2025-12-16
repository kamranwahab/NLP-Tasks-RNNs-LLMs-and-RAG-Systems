<p align="center"> 
  <img src="https://img.shields.io/badge/NLP-Text%20Classification-blue" /> 
  <img src="https://img.shields.io/badge/Model-RNN%20(LSTM)-orange" /> 
  <img src="https://img.shields.io/badge/Model-LLaMA%203-green" /> 
  <img src="https://img.shields.io/badge/Technique-RAG-purple" />
  <img src="https://img.shields.io/badge/Status-Completed-success" /> 
</p>

# 🧠 NLP Tasks: RNNs, LLMs, and RAG Systems

## 📋 Description
A comprehensive comparative analysis of traditional Deep Learning (RNN/LSTM) versus modern Large Language Models (LLaMA 3) for text classification, followed by the implementation of a local Retrieval-Augmented Generation (RAG) system for querying private data.

---

## 📖 Summary & Introduction
This project explores the evolution of Natural Language Processing (NLP) techniques. It begins by training a **Recurrent Neural Network (RNN)** from scratch to classify movie reviews, demonstrating the capabilities of varied sequence models on limited data. 

It then contrasts this with **LLaMA 3**, a state-of-the-art Large Language Model running locally via **Ollama**, to evaluate zero-shot performance. Finally, the project implements a **RAG system**, enabling LLaMA 3 to answer questions based on custom, private documents that were not part of its training set, effectively solving the "hallucination" problem.

---

## 🎯 Objectives
* **Task 1:** Train and evaluate a custom RNN (LSTM) model on the IMDB sentiment analysis dataset.
* **Task 2:** Deploy LLaMA 3 locally using Ollama and compare its zero-shot classification accuracy against the custom RNN.
* **Task 3:** Build a Retrieval-Augmented Generation (RAG) system to ground LLM responses in proprietary, user-provided documents.

---

## 📂 Dataset Information

### 1. IMDB Movie Reviews (Task 1 & 2)
* **Source:** `tensorflow.keras.datasets.imdb`
* **Description:** A dataset of 25,000 movie reviews, labeled by sentiment (positive/negative).
* **Usage:** A subset of **100 reviews** was used to simulate a low-resource environment (80 Training / 20 Testing).

### 2. Custom Knowledge Base (Task 3)
* **Source:** User-generated text files.
* **Content:** * `mars_colony_rules.txt`: Fictional rules for a Mars habitat.
    * `cyber_pet_manual.txt`: Technical manual for a robotic pet.
    * `secret_history_z.txt`: Classified mission logs.
* **Purpose:** To test the RAG system's ability to retrieve specific, non-public information.

---

## 🛠️ Tools & Technologies Used

| Category | Technologies |
| :--- | :--- |
| **Languages** | ![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white) |
| **Deep Learning** | ![TensorFlow](https://img.shields.io/badge/TensorFlow-Keras-orange?logo=tensorflow&logoColor=white) ![NumPy](https://img.shields.io/badge/NumPy-Array-blue) |
| **LLM & Inference** | ![Ollama](https://img.shields.io/badge/Ollama-Local_LLM-black) **LLaMA 3** |
| **RAG Components** | `sentence-transformers` (Embeddings), `scikit-learn` (Cosine Similarity) |
| **Environment** | VS Code, Google Colab (Optional) |

---

## 📊 Key Results

### 🆚 Classification Comparison (Task 1 vs Task 2)
| Model | Type | Accuracy | Key Observation |
| :--- | :--- | :--- | :--- |
| **RNN (LSTM)** | Supervised Learning | **75.00%** | Good for specific tasks, but overfits on small data. |
| **LLaMA 3** | Zero-Shot Transfer | **85.00%** | Superior context understanding without training. |

### 🔎 RAG System Performance (Task 3)
* **Without RAG:** LLaMA hallucinated answers for private data (e.g., guessing random dates).
* **With RAG:** LLaMA correctly answered **8/10** questions by retrieving the exact sentence from the source files.
* **Insight:** The system effectively filtered out hallucinations but required precise sentence retrieval for complex queries.

---

## 🚀 How to Run


1.  **Install Dependencies**
    ```bash
    pip install tensorflow numpy pandas sentence-transformers scikit-learn requests
    ```

2.  **Run Task Scripts**
    * **Task 1 (RNN):** Run the notebook `Task1_RNN.ipynb`.
    * **Task 2 (LLaMA):** Ensure Ollama is running (`ollama serve`), then run:
        ```bash
        python task2_llama.py
        ```
    * **Task 3 (RAG):** Update the document path in the script and run:
        ```bash
        python task3_rag.py
        ```

---

<p align="center">
  <b>Developed By: Kamran Wahab | 2025(S)-MS-AI-03</b>
</p>
