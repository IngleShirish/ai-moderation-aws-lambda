# AI Context-Aware Comment Moderation (POC)

This project demonstrates a **context-aware comment moderation system** built using **FastAPI, AWS Lambda, API Gateway, and Amazon Bedrock (Nova Micro)**.

The service analyzes user comments against the **article context (headline + summary)** and determines whether the comment is **safe or unsafe**.

This Proof of Concept (POC) shows how **AI-powered moderation pipelines can be integrated into news or media platforms** to prevent harmful, abusive, or off-topic discussions.

---

# Features

* Context-aware comment moderation
* Multi-stage moderation pipeline
* Serverless deployment using AWS Lambda
* FastAPI based API service
* Optional comment ID tracking
* Uses Amazon Bedrock Nova Micro for AI moderation
* Designed for scalability and low cost

Moderation detects:

* Hate speech
* Harassment
* Violence or threats
* Spam
* Group insults
* Inflammatory tone
* Misinformation relative to the article
* Off-topic political arguments
* Comments likely to start arguments

---

# Architecture

Client
    │
    ▼
API Gateway
    │
    ▼
AWS Lambda (FastAPI + Mangum)
    │
    ▼
Moderation Pipeline
    ├── Stage 1: Rule Based Filter
    ├── Stage 2: AI Moderation
    └── Stage 3: Context-Aware Moderation
            │
            ▼
          Amazon Bedrock (Nova Micro)

---

# Moderation Pipeline

## Stage 1 — Rule Based Filter

Fast keyword-based checks for obvious violations.

Examples:

* abusive language
* threats
* spam keywords

Purpose:

* filter obvious violations
* reduce LLM calls
* reduce cost

---

## Stage 2 — AI Moderation

Inputs:

* article headline
* comment text

The AI model evaluates the comment for:

* hate speech
* harassment
* violence
* spam
* group insults
* inflammatory tone

This stage provides deeper semantic moderation compared to rule-based filtering.

---

## Stage 3 — Context-Aware Moderation

The comment is evaluated relative to the **article content**.

Inputs:

* article headline
* article summary
* comment text

Detects:

* misinformation
* unrelated political arguments
* hostile tone
* attempts to start arguments between readers

---

# Example API Request

POST /moderate

Example request body:

```json
{
  "article_id": "1001",
  "comment_id": "c101",
  "headline": "Bernard Fanning tells heckler to 'fuck off' at Sydney concert",
  "summary": "Singer Bernard Fanning responded angrily during a concert after an audience member objected to his political commentary.",
  "comment": "Immigrants like them ruin everything."
}
```

---

# Example API Response

```json
{
  "comment_id": "c101",
  "safe": false,
  "category": "hate",
  "severity": "high",
  "confidence": 0.92,
  "reason": "The comment targets a group in a hostile manner.",
  "stage": "ai_context"
}
```

---

# Project Structure

```
ai-moderation-lambda
│
├── app
│   ├── main.py
│   ├── models.py
│   │
    ├── bedrock
│   │   ├── client.py
│   │   ├── parser.py
│   ├── moderation
│   │   ├── pipeline.py
│   │   ├── stage1_rules.py
│   │   ├── stage2_rules.py
│   │   └── stage3_context.py
│   │
│   ├── prompts
│   │   ├── stage2_prompt.py
│   │   └── stage3_prompt.py
│   │
│   └── utils
│       └── bedrock_client.py
│
├── run_local.py
├── requirements.txt
├── serverless.yml
├── package.json
└── README.md
```

---

# Deployment

The service is deployed using **Serverless Framework**.

## Install dependencies

```
pip install -r requirements.txt
```

---

## Deploy to AWS

```
serverless deploy
```

After deployment an API endpoint will be created.

Example endpoint:

```
https://xxxxx.execute-api.us-east-1.amazonaws.com/moderate
```

---

# Security Measures (POC)

Basic protections implemented:

* API Gateway rate limiting
* API key protection
* Lambda concurrency limits

These protections prevent:

* API abuse
* unexpected Bedrock costs
* excessive calls from a single user

---

# Cost Estimate

Using Amazon Bedrock **Nova Micro**.

Typical moderation request:

* ~250 input tokens
* ~30 output tokens

Cost for **30,000 comments**:

≈ **$0.40 – $0.50**

This makes the system extremely **cost efficient for large scale moderation**.

---

# Future Improvements

Production systems could include:

* Redis cache for moderation decisions
* DynamoDB storage for moderation logs
* asynchronous moderation pipeline using SQS
* user reputation scoring
* multilingual moderation
* ML-based toxicity scoring
* moderation analytics dashboard

---

# Use Cases

This system can be integrated into:

* News websites
* Blog platforms
* Online communities
* Social media platforms
* Media publishing systems

---

# Technologies Used

* Python
* FastAPI
* AWS Lambda
* API Gateway
* Amazon Bedrock
* Nova Micro Model
* Serverless Framework

---

# License

This repository is a **Proof of Concept (POC)** demonstrating AI-powered moderation workflows for scalable content platforms.
