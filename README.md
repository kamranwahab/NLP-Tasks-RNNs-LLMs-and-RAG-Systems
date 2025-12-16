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

## 📂 Repository Structure
The project is organized into three main tasks:

* **`Task_1_RNN/`**: Contains the Jupyter notebook for the LSTM model.
  * `rnn_sentiment_analysis.ipynb`: The main training and evaluation code.
* **`Task_2_LLaMA/`**: Scripts for running the local LLaMA model.
  * `llama_sentiment_analysis.py`: Python script for zero-shot sentiment classification.
* **`Task_3_RAG/`**: The complete RAG system implementation.
  * `rag_system.py`: The main script that performs retrieval and generation.
  * `documents/`: Folder containing the custom text files (`mars_colony_rules.txt`, etc.).
  * `rag_report.csv`: Auto-generated report comparing LLaMA with and without RAG.

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

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/kamranwahab/NLP-Tasks-RNNs-LLMs-and-RAG-Systems](https://github.com/kamranwahab/NLP-Tasks-RNNs-LLMs-and-RAG-Systems)
    cd NLP-RNN-LLaMA-RAG
    ```

2.  **Install Dependencies**
    ```bash
    pip install tensorflow numpy pandas sentence-transformers scikit-learn requests
    ```

3.  **Run Task Scripts**
    * **Task 1 (RNN):** Open and run `Task_1_RNN/rnn_sentiment_analysis.ipynb`.
    * **Task 2 (LLaMA):** Ensure Ollama is running (`ollama serve`), then run:
        ```bash
        python Task_2_LLaMA/llama_sentiment_analysis.py
        ```
    * **Task 3 (RAG):** Update the document path in `rag_system.py` and run:
        ```bash
        python Task_3_RAG/rag_system.py
        ```

---

<p align="center">
  <b>Developed By: Kamran Wahab | 2025(S)-MS-AI-03</b>
</p>
