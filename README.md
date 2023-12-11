# Rental Price Prediction Using Big Data Tools

This project aims to predict the rental price of properties based on their characteristics. It utilizes Apache Spark and other big data tools to process and analyze a large dataset of USA rental listings scraped from Craigslist (https://www.kaggle.com/datasets/austinreese/usa-housing-listings).  

A linear regression machine learning model is trained to predict prices using property information like square footage, number of bedrooms/bathrooms, location, etc. The model is evaluated and persists on HDFS for low-latency, streaming predictions as new listing data arrives.

## Tools/Technologies

* Apache Spark - Cluster computing engine for large-scale data processing  
* Spark MLlib - Spark's machine learning library    
* PySpark - Python API for Spark  
* Apache Kafka - High throughput message broker
* HDFS - Distributed file storage system  
* Streamlit - Framework for creating web apps    

## Contents

The repository contains:

- Source code for data ingestion, preprocessing, model training and evaluation, Kafka streaming, and monitoring dashboard    
- Trained regression model
 

## Usage  

Instructions for running the code and replicating the analysis are contained in the README files in sub-directories. The `app.py` script will launch the real-time monitoring dashboard.   

Let me know if you would like any changes or have additional information to include!
