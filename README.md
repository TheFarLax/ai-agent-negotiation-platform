# Autonomous AI Commerce on GenLayer

Autonomous AI-to-AI commerce powered by GenLayer Intelligent Contracts and decentralized validator consensus.

---

## Overview

This project demonstrates how autonomous AI agents can negotiate, validate, and finalize agreements using GenLayer’s Intelligent Contract infrastructure.

Traditional smart contracts struggle with subjective decision-making and real-world ambiguity. GenLayer solves this using decentralized AI-powered validators capable of reasoning, voting, and reaching consensus.

This platform showcases:

- AI buyer and seller negotiation
- Autonomous agreement generation
- Validator-backed consensus simulation
- GenLayer Intelligent Contract deployment
- Real on-chain agreement execution
- Decentralized AI commerce workflows

---

## Architecture

```text
User
↓
Frontend (Next.js)
↓
FastAPI Backend
↓
AI Buyer + Seller Agents
↓
Negotiation Agreement
↓
GenLayer Intelligent Contract
↓
Validator Consensus
↓
On-chain Agreement Storage
```

---

## Features

### Autonomous AI Negotiation

AI buyer and seller agents negotiate:
- pricing
- deadlines
- delivery conditions
- acceptance criteria

---

### Intelligent Contracts on GenLayer

Agreements are deployed and executed using GenLayer Intelligent Contracts.

---

### Validator Consensus

Simulated decentralized validators independently evaluate agreements and reach consensus.

---

### Real GenLayer Integration

The application communicates with a live local GenLayer simulator network using real RPC transactions.

---

### Subjective Decentralized Execution

Demonstrates GenLayer’s core thesis:
> decentralized reasoning and trustless subjective consensus for autonomous AI commerce.

---

# Tech Stack

## Frontend
- Next.js
- React
- TailwindCSS
- Axios

## Backend
- FastAPI
- Python
- GenLayer Python SDK

## Infrastructure
- GenLayer Simulator
- Intelligent Contracts
- Validator Consensus System
- Local RPC Network

## AI
- Ollama / OpenRouter
- Autonomous Negotiation Agents

---

# Project Structure

```text
ai-agent-negotiator/
│
├── backend/
│   ├── agents/
│   ├── contracts/
│   ├── icontracts/
│   ├── negotiation/
│   ├── services/
│   ├── main.py
│   ├── deploy_contract.py
│   └── interact_contract.py
│
├── frontend/
│
├── screenshots/
│
└── README.md
```

---

# How It Works

## Step 1 — AI Negotiation

The user submits a task request.

Example:

```text
Need SaaS landing page copy delivered in 24 hours under $250
```

AI buyer and seller agents autonomously negotiate terms.

---

## Step 2 — Agreement Creation

Once consensus is reached between agents:

- final price is generated
- deadline is finalized
- agreement becomes eligible for execution

---

## Step 3 — Store On GenLayer

The backend submits a real transaction to the GenLayer local network.

The Intelligent Contract executes:

```python
create_agreement(...)
```

Validators execute and finalize state transitions.

---

## Step 4 — Validator Consensus

Independent validators evaluate agreement conditions and produce consensus results.

---

# Running Locally

## 1. Clone Repository

```bash
git clone YOUR_REPO_URL
cd ai-agent-negotiator
```

---

## 2. Start GenLayer Simulator

```bash
cd ~/genlayer-simulator

cp .env.example .env

docker compose up
```

---

## 3. Start Backend

```bash
cd backend

source ../venv/bin/activate

uvicorn main:app --reload
```

Backend runs on:

```text
http://127.0.0.1:8000
```

---

## 4. Start Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend runs on:

```text
http://localhost:3000
```

---

# Deploy Intelligent Contract

```bash
python deploy_contract.py
```

---

# Run Contract Interaction

```bash
python interact_contract.py
```

---

# Demo Flow

1. User enters task request
2. AI agents negotiate autonomously
3. Final agreement generated
4. Agreement stored on GenLayer
5. Validators simulate decentralized consensus
6. Consensus finalized

---

# Screenshots

Add screenshots here:

```text
screenshots/
```

Recommended:
- negotiation timeline
- final agreement
- validator consensus
- successful GenLayer transaction

---

# Why GenLayer?

Current blockchains are excellent at deterministic computation but weak at subjective reasoning.

GenLayer enables:
- decentralized AI validation
- trustless subjective consensus
- autonomous dispute resolution
- AI-native commerce infrastructure

This project demonstrates those ideas in practice.

---

# Future Improvements

- Wallet integration
- Real validator voting
- Appeals system
- Escrow payments
- Multi-agent marketplaces
- Autonomous settlement
- Reputation systems
- AI service discovery

---

# Built With GenLayer

Powered by:
- GenLayer Intelligent Contracts
- Validator-backed execution
- Autonomous AI negotiation
- Decentralized subjective consensus

---

# License

MIT License

---

# Author

Built by Ritesh using GenLayer.

Exploring the future of autonomous AI commerce.
