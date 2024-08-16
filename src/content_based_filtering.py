#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import pandas as pd

def content_based_filtering(data_path):
    data = pd.read_csv(data_path)
    
    #Vectorization
    tfidf = TfidfVectorizer(stop_words='english')
    data['Description'] = data['Description'].fillna('')
    tfidf_matrix = tfidf.fit_transform(data['Description'])
    
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    
    indices = pd.Series(data.index, index=data['StockCode']).drop_duplicates()
    
    def recommend_products(stock_code, num_recommendations=10):
        idx = indices[stock_code]
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:num_recommendations+1]
        
        product_indices = [i[0] for i in sim_scores]
        return data['StockCode'].iloc[product_indices]
    
    #Recommendations based on similar products
    recommendations = recommend_products(stock_code='85123A')
    print("Recommended products:", recommendations)

if __name__ == "__main__":
    processed_data_path = "data/processed/processed_data.csv"
    content_based_filtering(processed_data_path)

