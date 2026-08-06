# 🎵 Spotify Genre Segmentation & Recommendation System

## 📌 Project Overview

The **Spotify Genre Segmentation & Recommendation System** is a Machine Learning web application developed using **Python**, **Streamlit**, and **K-Means Clustering**. The application groups Spotify songs into different clusters based on their audio features and recommends similar songs from the same cluster.

This project demonstrates the use of **Unsupervised Machine Learning** for music recommendation and genre segmentation.

---

## 🎯 Objectives

- Cluster Spotify songs using K-Means Clustering.
- Recommend songs with similar characteristics.
- Visualize genre and cluster distributions.
- Build an interactive web application using Streamlit.
- Demonstrate the practical application of Unsupervised Learning.

---

## 🚀 Features

- 🎵 Spotify-inspired user interface
- 🔍 Search songs by name
- 🎯 Recommend similar songs
- 📊 Dashboard with dataset statistics
- 📈 Genre Distribution Chart
- 📊 Cluster Distribution Chart
- 🔥 Top Popular Songs
- 📂 Dataset Explorer
- 📥 Download Recommended Songs
- 🌙 Responsive Dark Theme

---

## 🛠 Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- K-Means Clustering

---

## 📂 Project Structure

```
SpotifyGenreSegmentation/

│── app.py
│── Spotify_Clustered_Results.csv.csv
│── scaler.pkl
│── kmeans_model.pkl
│── requirements.txt
│── README.md
│── spotify_logo.png (optional)

```

---

## 📊 Dataset

Dataset: **Spotify Songs Dataset**

The dataset contains information such as:

- Track Name
- Artist
- Genre
- Popularity
- Audio Features
- Cluster Label

---

## 🤖 Machine Learning Algorithm

### K-Means Clustering

K-Means is an Unsupervised Machine Learning algorithm used to divide data into K clusters.

### Workflow

```
Spotify Dataset
       │
       ▼
Data Cleaning
       │
       ▼
Feature Selection
       │
       ▼
Feature Scaling
       │
       ▼
K-Means Clustering
       │
       ▼
Cluster Generation
       │
       ▼
Song Recommendation
       │
       ▼
Streamlit Web Application
```

---

## ⚙ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/spotify-genre-segmentation.git
```

### 2. Move to Project Folder

```bash
cd spotify-genre-segmentation
```

### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
streamlit run app.py
```

---

## 📸 Application Screens

The application includes:

- Dashboard
- Song Recommendation
- Genre Analysis
- Cluster Analysis
- Dataset Explorer

---

## 📈 Output

The application displays:

- Selected Song Details
- Recommended Songs
- Song Popularity
- Genre Distribution
- Cluster Distribution
- Dataset Statistics

---

## 💡 Future Enhancements

- Spotify API Integration
- Album Cover Display
- Artist Search
- Playlist Recommendation
- Mood-Based Recommendation
- Audio Preview
- Similarity Score
- PCA Cluster Visualization

---

## 👨‍💻 Developed By

**Tanvi Lad**

Final Year Machine Learning Project

---

## 📚 References

- Spotify Songs Dataset
- Streamlit Documentation
- Scikit-learn Documentation
- Pandas Documentation
- NumPy Documentation

---

## 📄 License

This project is developed for **educational and academic purposes**.

---

## ⭐ Acknowledgement

I would like to express my sincere gratitude to my project guide, faculty members, and institution for their valuable guidance and support throughout the development of this project. I also acknowledge the open-source community and the developers of Python, Streamlit, Pandas, NumPy, and Scikit-learn for providing excellent tools and resources that made this project possible.
