#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
from src.collaborative_filtering import collaborative_filtering
from src.content_based_filtering import content_based_filtering

def train_models():
    processed_data_path = "data/processed/processed_data.csv"
    
    collaborative_filtering(processed_data_path)
    
    content_based_filtering(processed_data_path)

if __name__ == "__main__":
    train_models()

