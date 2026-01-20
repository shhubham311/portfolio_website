import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from openai import OpenAI  # For Groq
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

# --- GROQ CLIENT SETUP ---
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY")
)

# --- RESUME LINK ---
RESUME_LINK = "https://drive.google.com/file/d/1yifNHLsLcUhe9zUzhGc3XfiCd5dBR2R3/view?usp=drive_link"

# --- RESUME CONTEXT ---
RESUME_CONTEXT = f"""
NAME: Shubham Kumar
LOCATION: Buxar, Bihar
ROLE: AI & Machine Learning Engineer
SUMMARY: AI Engineer with 10 months of experience building Computer Vision and Multimodal RAG systems. Specialist in MLOps, Real-time Inference, and LLM integration.
CONTACT: shubham31103@gmail.com | +91 6204992324
LINKS: linkedin.com/in/shubhamkumar311/ | github.com/shhubham311/

RESUME LINK: {RESUME_LINK}

EDUCATION:
B.Tech CSE, Lovely Professional University (Sep 2021 - July 2025), CGPA: 8.50

EXPERIENCE:
Data Engineering & AI/ML Intern at BiUP Technologies Pvt. Ltd. (Feb 2025 - Nov 2025)
- Multimodal RAG Pipeline: Architected document ingestion (PDF, DOCX, XLSX) using FastAPI & LLMs (Claude/OpenAI). Reduced manual extraction time by 90% using Pinecone.
- Real-Time Computer Vision: Engineered vehicle photography guidance using YOLOv8 & Flask with <60ms latency.
- Reliability: Fixed critical PyTorch serialization issues and optimized AWS S3 logging.

PROJECTS:
1. Real-Time IoT Intrusion Detection System (MLOps):
   - End-to-end pipeline detecting network attacks (DDoS, Mirai Botnet) on IoT devices.
   - Metrics: 99.81% Accuracy, 97.85% F1 Macro, <50ms Inference Latency.
   - Tech: XGBoost, FastAPI, Docker, GitHub Actions (CI/CD), MLflow.
   - Solved extreme class imbalance (rare attacks vs normal traffic) using stratified sampling and class weighting.

2. ProfitGenAI - AI-Powered E-commerce Sales Agent:
   - Hybrid recommendation engine for 50,000+ products with <150ms response time.
   - Combines FAISS vector search with profitability re-ranking algorithms.
   - Uses Llama-based LLM via Groq API for dynamic, persona-driven sales pitches.
   - Deployed on Hugging Face Spaces using Docker and Git LFS.

3. Advanced Predictive Maintenance System:
   - Achieved 70.36% R² accuracy (RMSE: 36.80) on NASA C-MAPSS dataset.
   - Architecture: FastAPI backend (~100ms latency) + Streamlit dashboard.
   - Features: Hybrid anomaly detection (Isolation Forest) and Optuna hyperparameter tuning.

SKILLS:
Languages: Python, SQL (MySQL), HTML
Frameworks: PyTorch, FastAPI, Flask, YOLOv8, Docker, AWS (S3)
Core Competencies: Computer Vision, RAG Pipelines, MLOps, Object Detection, Prompt Engineering, Vector Databases (Pinecone/FAISS)
"""

SYSTEM_PROMPT = f"""
You are a professional AI Assistant representing Shubham Kumar on his portfolio website.
Your tone is professional, corporate, and concise. 
You are speaking directly to a recruiter or hiring manager.

Instructions:
1. Answer strictly based on the CONTEXT provided below.
2. Highlight Shubham's specific metrics (e.g., "99.81% accuracy", "<50ms latency") to demonstrate technical depth.
3. If the user asks about "resume" or "cv", provide the link: {RESUME_LINK}.
4. If the user asks about something not in the context, politely say you don't have that information and suggest contacting Shubham directly.
5. Keep answers under 3-4 sentences unless detailed technical info is requested.

CONTEXT:
{RESUME_CONTEXT}
"""

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    try:
        completion = client.chat.completions.create(
            model="meta-llama/llama-4-maverick-17b-128e-instruct",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": data.get('message', '')}
            ],
            temperature=0.5, max_tokens=300
        )
        return jsonify({"response": completion.choices[0].message.content})
    except Exception as e:
        print(f"Groq Error: {e}")
        return jsonify({"response": "I am currently unavailable."}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=False)