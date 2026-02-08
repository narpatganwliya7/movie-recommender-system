# 🎬 Movie Recommender System

A content-based movie recommendation system built using machine learning techniques and deployed as an interactive web application using Streamlit.

🔗 **Live Demo**: https://mrs-campusx-49a2591eec81.herokuapp.com/

---

## 📌 Project Overview

This project recommends movies similar to a user-selected movie by analyzing textual features such as:
- Genres
- Overview
- Cast
- Crew
- Keywords

Cosine similarity is used to compute similarity between movies based on vectorized text features.

The application is optimized for performance by storing only the **top-N most similar movies** per movie instead of a full similarity matrix.

---

## 🧠 How It Works

1. Movie metadata is cleaned and merged from TMDB datasets
2. Text features are combined into a single tag column
3. Text is vectorized using **CountVectorizer**
4. Cosine similarity is calculated
5. Only top similar movies are stored for fast inference
6. A Streamlit app provides an interactive UI

---

## 🗂️ Project Structure

```text
movie-recommender-system/
│
├── app.py                 # Streamlit application
├── data/                  # Raw TMDB datasets
├── models/
│   ├── movies.pkl         # Processed movie dataframe
│   └── top_similar.pkl    # Optimized similarity data
├── notebooks/
│   └── mrs_system.ipynb   # Data cleaning & model building
├── scripts/
│   └── build_top_similar.py
├── screenshots/           # UI screenshots
├── requirements.txt
├── Procfile               # Heroku deployment config
└── README.md
