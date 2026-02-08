# 🎬 Movie Recommender System

A production-ready **content-based movie recommendation system** built using Machine Learning and deployed as a web application using **Streamlit**.

🔗 Live Demo: https://mrs-campusx-49a2591eec81.herokuapp.com/

---

## 📌 Project Overview

This project recommends movies similar to a selected title by analyzing movie metadata such as:
- Genres
- Overview
- Cast
- Crew
- Keywords

The system is optimized for **low memory usage and fast inference**, making it suitable for real-world deployment and scalable environments.

---

## 🧠 Recommendation Methodology

- Recommendation Type: Content-Based Filtering  
- Text Vectorization: CountVectorizer  
- Similarity Metric: Cosine Similarity  

To reduce memory consumption, the system stores **only the top similar movies per title** instead of a full similarity matrix.

---

## 🗂️ Project Structure

movie-recommender-system  
│  
├── app.py                     Streamlit web application  
│  
├── data  
│   ├── tmdb_5000_movies.csv  
│   └── tmdb_5000_credits.csv  
│  
├── models  
│   ├── movies.pkl             Processed movie metadata  
│   └── top_similar.pkl        Optimized similarity results  
│  
├── notebooks  
│   └── mrs_system.ipynb       Data cleaning & model building  
│  
├── scripts  
│   └── build_top_similar.py   Script to generate optimized similarity model  
│  
├── screenshots  
│   └── app_ui.png             Application screenshot  
│  
├── requirements.txt  
├── Procfile  
└── README.md  

---

## 🖼️ Application Preview

![Movie Recommender System](screenshots/app_ui.png)
![Movie Recommender System Screenshot](screenshots/image_3.png)
---

## ⚙️ Tech Stack

- Programming Language: Python  
- Libraries: Pandas, NumPy, Scikit-learn  
- Web Framework: Streamlit  
- Deployment: Heroku  
- Version Control: Git & GitHub  

---

## 🚀 Run Locally

Clone the repository and run the application locally:

git clone https://github.com/narpatganwliya7/movie-recommender-system.git  
cd movie-recommender-system  
pip install -r requirements.txt  
streamlit run app.py  

---

## 📊 Dataset

- Source: TMDB 5000 Movies & Credits Dataset  
- Used for educational and portfolio demonstration purposes only  

---

## ⭐ Key Highlights

- Memory-optimized similarity computation  
- Clean and modular project structure  
- End-to-end machine learning workflow  
- Deployed and publicly accessible application  
- Recruiter-friendly documentation  

---

## 👨‍💻 Author

Narpat Ganwliya  

GitHub: https://github.com/narpatganwliya7  
LinkedIn: https://www.linkedin.com/

---

If you find this project useful, feel free to ⭐ the repository.
