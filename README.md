# E-commerce Recommendation System Deployment

This project involves designing, implementing, and deploying a recommendation system for an e-commerce platform. The recommendation system uses **collaborative filtering** and **content-based filtering** techniques to provide personalized product recommendations. The model is trained using **Scikit-Learn** and **Spark MLlib** and deployed on **AWS EC2**, with the model files stored on **S3**.

## Project Overview

- **Modeling Techniques:** 
  - Collaborative Filtering
  - Content-Based Filtering
- **Modeling Libraries:** 
  - Scikit-Learn 
  - Spark MLlib
- **Deployment Services:** 
  - AWS EC2 
  - S3 
  - SSH with Paramiko

## Dataset

The dataset used in this project can be downloaded from [Kaggle's E-Commerce Dataset](https://www.kaggle.com/datasets). After downloading, place the raw data files in the `data/raw` directory.

### Columns:

- **`user_id`**: Unique identifier for each user.
- **`product_id`**: Unique identifier for each product.
- **`ratings`**: User's rating for the product (used for collaborative filtering).
- **`product_category`**: Category of the product (used for content-based filtering).
- **`product_description`**: Description of the product for content-based filtering.
