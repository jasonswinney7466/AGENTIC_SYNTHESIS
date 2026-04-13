AGENTIC SYNTHESIS
**Version:** 8.4.1 [STAINLESS]
**Technical Producer:** Jason Swinney @jasonswinney74@gmail.com
This is a new project from someone with a good idea. This is far from done and is vibe coded. I find it interesting to hear them talk to each other. It's also nice to comapre how different LLM's rely to questions.
I will keep working on this, while I think of the ultimate format for this is. I have not got it to solve a real world problem like world hunger, energy yet. lol

Agentic Synthesis is a high-fidelity, distributed orchestration platform designed to facilitate collaborative intelligence between autonomous AI personas. By leveraging a hybrid architecture of local hardware and cloud-based LLMs, the system allows users to "synthesize" insights through the interaction of specialized agents.

1. The Core Concept: Collaborative Synthesis
At the heart of the platform is the **Interaction Stage**. Instead of a traditional single-chat interface, Agentic Synthesis allows you to select two distinct agents and pose questions to both simultaneously. 

The magic happens in the **Synthesis**: You aren't just getting an answer; you are watching a specialized Doctor, Engineer, or Scientist process information through the lens of their unique identity. Whether they are solving a complex technical problem or engaging in a philosophical debate, the entertainment and functional value lies in the interaction between the two "minds."

2. The Soul File (Personality Engine)
Every agent is defined by a **Soul File**—a 200-character personality directive that dictates their tone, knowledge base, and behavioral constraints. 
Identity Assumption: Agents fully inhabit their roles, allowing you to listen to AI assume a specific professional or creative identity.
Dynamic Customization: Use the **Creator Hub** to initialize new agents by uploading a portrait and defining their Soul File logic.

3. Hybrid Intelligence & Benchmarking
The platform is built for the "Power User" who wants to see how different models truly perform.
Mix & Match LLMs:** Assign different "Brains" to each agent. You can have a lightweight **3B model** (running locally on your Node) debating a heavy-lifting **8B model** or a paid **Cloud API**.
Local-First Architecture: Native support for local LLM instances (via Ollama) ensures data privacy and utilizes your local GPU clusters (e.g., PC1 and PC2 nodes) for high-speed inference.
Model Benchmarking: Observe how parameter sizes and model architectures affect reasoning and persona adherence in real-time.

4. Built-in Content & Discovery The 60-Agent Roster:** A pre-populated gallery featuring 60 unique personas (30 Male/30 Female) across various disciplines—from Quantum Physics to Structural Engineering.
Random Inquiry Generator:** A dedicated "Random Inquiry" button designed to challenge your agents. With one click, the system pulls complex, high-vibe technical or philosophical questions to trigger immediate multi-agent synthesis.

5. Technical Aesthetic
The dashboard utilizes an **Emerald Emerald** tactical terminal theme, prioritizing high-contrast legibility and "Control Center" vibes.
Hardware Telemetry: Real-time monitoring of Node Load and Temperature.
System Stream: A live terminal log documenting the handshake between local nodes and cloud endpoints.

**"Synthesis isn't just about the answer—it's about the perspective."**
— *Sam, Technical Producer*

## 🛠️ HARDWARE & SETUP
This project was developed on an **NVIDIA RTX 2070 Super** using **Ubuntu 24.04 LTS (WSL2)**.

### 1. Prerequisites
- **Ollama:** Must be installed and running (`ollama serve`).
- **Python 3.12+**
- **Requirements:** `pip install fastapi uvicorn httpx`

### 2. Local Installation Path
The primary build environment is located at:
`C:\WSL\AGENTIC SYNTHESIS\`

### 3. Quick Start (Linux/WSL Terminal)
```bash
cd "/mnt/c/WSL/AGENTIC SYNTHESIS"
source venv/bin/activate
python amber_signal.py
