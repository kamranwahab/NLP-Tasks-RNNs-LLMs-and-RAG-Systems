import os
import requests
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# ==========================================
# CONFIGURATION
# ==========================================
# UPDATE THIS PATH to the folder where you saved your 3 text files
DOCS_PATH = r"C:\Users\Kamran Wahab\Desktop\UET\Semester 02\NLP\Sir Atta NLP Tasks\Task 3\Task3_Documents" 

OLLAMA_API = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3"
EMBEDDING_MODEL = "all-MiniLM-L6-v2" # [cite: 57]

# ==========================================
# RAG SYSTEM FUNCTIONS
# ==========================================

def load_documents(folder_path):
    """Reads all .txt files from the specified folder."""
    documents = {}
    print(f"📂 Reading documents from: {folder_path}")
    
    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"The folder '{folder_path}' does not exist. Please create it.")
        
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, "r", encoding="utf-8") as f:
                documents[filename] = f.read()
    
    if not documents:
        raise ValueError("No .txt files found! Please add the text files to the folder.")
        
    print(f"✅ Loaded {len(documents)} files.")
    return documents

def create_chunks(documents):
    """Breaks documents into small chunks for searching[cite: 53]."""
    chunks = []
    chunk_sources = []
    
    for filename, text in documents.items():
        # Split by newlines or periods to get sentences/paragraphs
        parts = [p.strip() for p in text.replace('.', '\n').split('\n') if len(p) > 10]
        for part in parts:
            chunks.append(part)
            chunk_sources.append(filename)
            
    return chunks, chunk_sources

def query_llama(prompt):
    """Sends a prompt to the local Ollama LLaMA 3 model."""
    payload = {"model": MODEL_NAME, "prompt": prompt, "stream": False}
    try:
        response = requests.post(OLLAMA_API, json=payload)
        return response.json().get("response", "").strip()
    except Exception as e:
        return f"Error: {e}"

# ==========================================
# MAIN EXECUTION
# ==========================================
def main():
    # 1. Load and Embed Documents
    docs = load_documents(DOCS_PATH)
    chunks, sources = create_chunks(docs)
    
    print("⚙️  Loading Embedding Model...")
    embedder = SentenceTransformer(EMBEDDING_MODEL) # [cite: 56]
    chunk_embeddings = embedder.encode(chunks)
    
    # 2. Define 10 Questions based on the documents 
    questions = [
        "When was the Mars Colony established?",
        "What is the currency used on Mars?",
        "How much water is allowed per citizen on Mars?",
        "What is the fine for violating water rations?",
        "How often does the Cyber-Dog 3000 need charging?",
        "How do you reset the Cyber-Dog?",
        "What languages come installed on the Cyber-Dog?",
        "Who led the team in Operation Z?",
        "What did they find in the Pacific Ocean?",
        "Where is the alien probe stored now?"
    ]
    
    results = []
    
    print("\n" + "="*60)
    print("STARTING COMPARISON (10 Questions)")
    print("="*60)
    
    for i, q in enumerate(questions):
        print(f"\n[{i+1}/10] Question: {q}")
        
        # --- A. LLaMA ALONE (NO RAG) ---
        print("   🤖 Asking LLaMA (No Context)...")
        # We explicitly tell LLaMA to use its own knowledge
        prompt_no_rag = f"Answer this question based on your training data: {q}"
        ans_no_rag = query_llama(prompt_no_rag)
        
        # --- B. LLaMA + RAG (WITH CONTEXT) ---
        print("   🔎 Retrieving Context...")
        # Find best chunk [cite: 61]
        q_emb = embedder.encode([q])
        similarities = cosine_similarity(q_emb, chunk_embeddings)[0]
        best_idx = np.argmax(similarities)
        best_chunk = chunks[best_idx]
        best_source = sources[best_idx]
        
        print(f"      (Found info in {best_source})")
        
        # Build RAG Prompt [cite: 63-66]
        prompt_rag = f"""
        Use ONLY the following context to answer the question.
        Context: "{best_chunk}"
        
        Question: {q}
        Answer:
        """
        ans_rag = query_llama(prompt_rag)
        
        # Store for report
        results.append({
            "Question": q,
            "LLaMA Alone": ans_no_rag,
            "LLaMA + RAG": ans_rag,
            "Source File": best_source
        })

    # 3. Save Final Report
    df = pd.DataFrame(results)
    df.to_csv("task3_final_report.csv", index=False)
    print("\n✅ Report saved to 'task3_final_report.csv'.")
    
    # Print a quick table preview
    print("\n" + "="*30)
    print("SUMMARY PREVIEW")
    print(df[["Question", "LLaMA + RAG"]].to_string())

if __name__ == "__main__":
    main()