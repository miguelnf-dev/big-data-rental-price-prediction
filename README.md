# Rental Price Prediction Using Big Data Tools

This project aims to predict the rental price of properties based on their characteristics. It utilizes Apache Spark and other big data tools to process and analyze a large dataset of USA rental listings scraped from Craigslist (https://www.kaggle.com/datasets/austinreese/usa-housing-listings).  

A Linear Regression and Random Forest machine learning models are trained to predict prices using property information like square footage, number of bedrooms/bathrooms, location, etc. The models are evaluated and persist on Hadoop Distributed File System (HDFS) for low-latency, streaming predictions as new listing data arrives.

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

## Usage  

Instructions for running the code and replicating the analysis are contained in the README files in sub-directories. The `app.py` script will launch the real-time monitoring dashboard.   

## Contributing

Contributions to this project are welcome! If you have any suggestions or improvements, please feel free to open an issue or create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
