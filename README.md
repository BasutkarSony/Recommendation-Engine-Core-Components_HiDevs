# Recommendation Engine Core Components

A modular Python-based recommendation engine that implements the fundamental building blocks of modern recommendation systems. The project demonstrates similarity calculation, candidate generation, recommendation scoring, ranking, and evaluation metrics using clean object-oriented programming principles.

---

## Project Overview

Recommendation systems are widely used by platforms such as Netflix, Amazon, Spotify, and YouTube to provide personalized suggestions. This project focuses on implementing the core algorithmic components of a recommendation engine that can later be integrated into a complete recommendation system.

The project consists of four independent modules:

- Similarity Calculator
- Candidate Generator
- Recommendation Scorer & Ranker
- Recommendation Evaluator

Each module is designed to be modular, reusable, and easy to extend.

---

## Project Demo

**Demo Video:**  
👉 [Demo](https://drive.google.com/file/d/14_HpaxvH0wB-4R0PPmIfwmCyG2tZYwP1/view?usp=sharing)

---

## Features

### Similarity Calculator
- Cosine Similarity
- Jaccard Similarity
- Pearson Correlation
- Handles empty inputs and zero vectors

### Candidate Generator
- Collaborative Filtering
- Content-Based Filtering
- Popularity-Based Recommendations
- Hybrid Recommendation Strategy
- Cold-start user support

### Recommendation Scorer
- Multiple scoring functions
- Weighted score calculation
- Candidate ranking
- Recommendation explanations

### Recommendation Evaluator
- Precision@K
- Recall@K
- NDCG@K
- Overall evaluation metrics

### Testing
- Automated test cases for all modules
- Edge case handling
- Modular and reusable implementation

---

# Project Structure

```
Recommendation-Engine-Core-Components_HiDevs/
│
├── similarity.py        # Similarity calculation methods
├── candidate_gen.py     # Candidate generation strategies
├── scorer.py            # Recommendation scoring & ranking
├── evaluator.py         # Evaluation metrics
├── test.py              # Test cases
└── README.md
```

---

# Module Description

## similarity.py

Implements commonly used similarity metrics in recommendation systems.

### Methods

- cosine_similarity(vec1, vec2)
- jaccard_similarity(set1, set2)
- pearson_correlation(ratings1, ratings2)

### Handles

- Empty vectors
- Empty sets
- Zero vectors
- Invalid input lengths

---

## candidate_gen.py

Generates recommendation candidates using different recommendation strategies.

### Methods

- collaborative_candidates()
- content_based_candidates()
- popularity_candidates()
- hybrid_candidates()

### Features

- Cold-start handling
- Duplicate removal
- Configurable result limits

---

## scorer.py

Ranks recommendation candidates using weighted scoring.

### Supports

- Multiple scoring functions
- Weighted score calculation
- Recommendation explanations
- Top-N ranking

Example scoring factors:

- Relevance
- Popularity
- Recency

---

## evaluator.py

Evaluates recommendation quality using standard information retrieval metrics.

### Metrics

- Precision@K
- Recall@K
- NDCG@K

Returns evaluation metrics as a dictionary.

---

## test.py

Contains simple automated tests for all project modules.

Tests include:

- Similarity calculations
- Candidate generation
- Recommendation scoring
- Evaluation metrics

---

# Requirements

- Python 3.8 or later

No external libraries are required.

This project uses only Python's standard library.

---

# Installation

Clone the repository:

```bash
git clone https://github.com/BasutkarSony/Recommendation-Engine-Core-Components_HiDevs.git
```

Navigate to the project folder:

```bash
cd Recommendation-Engine-Core-Components_HiDevs
```

---

# Running the Project

Run each module individually:

```bash
python similarity.py
```

```bash
python candidate_gen.py
```

```bash
python scorer.py
```

```bash
python evaluator.py
```

Run all tests:

```bash
python test.py
```

---

# Sample Output

```
Running Recommendation Engine Tests...

Similarity tests passed.
Candidate Generator tests passed.
Scorer tests passed.
Evaluator tests passed.

All tests passed successfully!
```

---

# Recommendation Pipeline

```
User Data
      │
      ▼
Similarity Calculator
      │
      ▼
Candidate Generator
      │
      ▼
Recommendation Scorer
      │
      ▼
Top Ranked Recommendations
      │
      ▼
Recommendation Evaluator
```

---

# Evaluation Metrics

| Metric | Description |
|----------|-------------|
| Precision@K | Measures the proportion of relevant recommendations in the top-K results. |
| Recall@K | Measures how many relevant items are successfully recommended. |
| NDCG@K | Evaluates ranking quality by considering the position of relevant recommendations. |

---

# Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- Standard Python Library
- Recommendation Algorithms

---

# Learning Outcomes

This project demonstrates practical implementation of:

- Recommendation System Fundamentals
- Similarity Calculations
- Candidate Generation Strategies
- Recommendation Ranking
- Evaluation Metrics
- Object-Oriented Programming
- Python Problem Solving

---

# Future Enhancements

Possible improvements include:

- Matrix Factorization
- User-Based Collaborative Filtering
- Item-Based Collaborative Filtering
- Hybrid Machine Learning Models
- Real-world Dataset Integration
- Streamlit Dashboard
- REST API Integration
- Database Support
- Personalized Recommendation Models
