import schedule
import time
from pyspark.sql import SparkSession
import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

# Create a Spark session
spark = SparkSession.builder.appName("HouseListings").getOrCreate()
data_path = "CLUSTER_URL_HERE"



def read_data() -> pd.DataFrame:
    with st.spinner("Loading data..."):
        df = spark.read.csv(data_path, header=True, inferSchema=True)
        return df.toPandas()


def generate_kpis_and_charts(df: pd.DataFrame):

    buffer = []
    placeholder = st.empty()
    col1, col2 = st.columns([1, 2])

    with col1:
        state_filter = st.selectbox("Select the State", pd.unique(df["state"]), key=f"state_filter2_{time.time()}")
        
    df_filtered = df[df["state"] == state_filter]
    avg_price = np.mean(df_filtered["price"])
    
    count_type = df_filtered[df_filtered["type"] == "apartment"]["type"].count()

    buffer.append(avg_price)

    if len(buffer) > 20:
        buffer.pop(0)

    avg_price_buffer = np.mean(buffer)
    sqfeet = np.mean(df_filtered["sqfeet"])

    with placeholder.container():
        kpi1, kpi2, kpi3 = st.columns(3)

        kpi1.metric(
            label=f"Avg rent price in {state_filter} 💰",
            value=f"{round(avg_price_buffer)}$",
        )

        kpi2.metric(
            label=f"# Apartments listed in {state_filter} 🏢",
            value=count_type,
        )

        kpi3.metric(
            label=f"Average sq.feet per property in {state_filter} 📏",
            value=f"{round(sqfeet, 2)} sqft",
        )
        
        with st.expander("View Charts"):
            st.markdown("### Price Analysis by State")
            df_state_price = df.groupby("state")["price"].mean()
            fig = px.bar(df_state_price, x=df_state_price.index, y="price", labels={"x": "State", "y": "Average Price"})
            st.plotly_chart(fig)

            st.markdown("### Property Type Analysis")
            df_property_type = df["type"].value_counts()
            fig2 = px.pie(df_property_type, values=df_property_type.values, names=df_property_type.index, labels={"value": "Count", "name": "Property Type"})
            st.plotly_chart(fig2)

            st.markdown("### Square Footage Analysis")
            df_sqfeet_stats = df["sqfeet"].describe()
            fig3 = px.histogram(df_sqfeet_stats, x="sqfeet", nbins=20, labels={"x": "Square Footage"})
            st.plotly_chart(fig3)

        st.markdown("### Detailed Data View")
        with st.expander("View Charts"):
            st.dataframe(df_filtered)

    time.sleep(2)


def run_app():

    st.set_page_config(
        page_title="Real-Time Big Data Dashboard",
        page_icon="✅",
        layout="wide",
    )
    st.title("Real-Time / House Data")

    df = read_data()
    
    generate_kpis_and_charts(df)
    
    schedule.every(10).minutes.do(generate_kpis_and_charts, df)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    run_app()