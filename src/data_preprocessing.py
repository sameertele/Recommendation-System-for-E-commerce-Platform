#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
from sklearn.model_selection import train_test_split
import os

def load_data(file_path):
    data = pd.read_csv(file_path, encoding='unicode_escape')
    return data

def preprocess_data(data):
    data.dropna(subset=['CustomerID'], inplace=True)
    
    data['CustomerID'] = data['CustomerID'].astype(int)
    data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'])
    
    data = data[data['Quantity'] > 0]
    
    return data

def save_processed_data(data, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    data.to_csv(os.path.join(output_dir, 'processed_data.csv'), index=False)

if __name__ == "__main__":
    raw_data_path = "data/raw/Ecommerce.csv"
    processed_data_path = "data/processed"
    
    data = load_data(raw_data_path)
    data = preprocess_data(data)
    save_processed_data(data, processed_data_path)

