#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from pyspark.sql import SparkSession
from pyspark.ml.recommendation import ALS
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.feature import StringIndexer
from pyspark.sql.functions import col

def collaborative_filtering(data_path):
    spark = SparkSession.builder.appName("CollaborativeFiltering").getOrCreate()
    
    df = spark.read.csv(data_path, header=True, inferSchema=True)
    
    indexer_user = StringIndexer(inputCol='CustomerID', outputCol='userIndex')
    indexer_item = StringIndexer(inputCol='StockCode', outputCol='itemIndex')
    
    df = indexer_user.fit(df).transform(df)
    df = indexer_item.fit(df).transform(df)
    
    als = ALS(maxIter=10, regParam=0.1, userCol='userIndex', itemCol='itemIndex', ratingCol='Quantity', coldStartStrategy="drop")
    model = als.fit(df)
    
    # Predictions
    predictions = model.transform(df)
    
    evaluator = RegressionEvaluator(metricName="rmse", labelCol="Quantity", predictionCol="prediction")
    rmse = evaluator.evaluate(predictions)
    print(f"Root Mean Squared Error (RMSE): {rmse}")
    
    # Recommendations to users
    user_recommendations = model.recommendForAllUsers(10)
    user_recommendations.show()
    
    spark.stop()

if __name__ == "__main__":
    processed_data_path = "data/processed/processed_data.csv"
    collaborative_filtering(processed_data_path)

