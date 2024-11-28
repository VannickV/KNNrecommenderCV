# KNN-Based Book Recommender System

## Overview
This project implements a book recommender system using the K-Nearest Neighbors (KNN) algorithm. By analyzing user ratings and book metadata, the system provides personalized book recommendations. The primary goal is to identify similar users or items to predict user preferences.

## Approach
1. **Dataset Preparation**:
   - Merged datasets of books, users, and ratings.
   - Preprocessed the data to handle missing values and reduce dimensionality.

2. **Model Implementation**:
   - Converted the dataset into a sparse matrix for efficient computation.
   - Used the Nearest Neighbors algorithm to calculate item-based similarity.

3. **Evaluation**:
   - Tested the recommender system by querying for similar books based on user preferences.

## Requirements
- Python 3.12 or higher
- Libraries:
  - `pandas`
  - `matplotlib`
  - `seaborn`
  - `scikit-learn`
  - `scipy`

Install the requirements with:
```bash
pip install -r requirements.txt
