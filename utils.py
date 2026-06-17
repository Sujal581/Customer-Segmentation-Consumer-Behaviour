import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

@st.cache_data
def load_data(file):
    df=pd.read_csv(file)
    df.columns=df.columns.str.strip()
    return df

@st.cache_data
def clean_data(df):
    df=df.copy()
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)
    return df

@st.cache_data
def scale_feature(df):
    features=["Age","Annual Income (k$)","Spending Score (1-100)"]
    scaler=StandardScaler()
    scaled_data=scaler.fit_transform(df[features])
    return scaled_data

@st.cache_data
def calculate_wcss(scaled_data):
    wcss=[]
    for k in range(1,11):
        model=KMeans(n_clusters=k,random_state=42,n_init=10)
        model.fit(scaled_data)
        wcss.append(model.inertia_)
    return wcss

@st.cache_data
def perform_clustering(scaled_data,k=5):
    model=KMeans(n_clusters=k,random_state=42,n_init=10)
    labels=model.fit_predict(scaled_data)
    return model,labels

@st.cache_data
def add_clusters(df,labels):
    df=df.copy()
    df["Clusters"]=labels
    return df


@st.cache_data
def calculate_kpis(df):
    metrics = {
        "total_customers": len(df),
        "avg_age": round(df["Age"].mean(), 1),
        "avg_income": round(df["Annual Income (k$)"].mean(), 1),
        "avg_spending": round(df["Spending Score (1-100)"].mean(), 1),
        "male_count": len(df[df["Gender"] == "Male"]),
        "female_count": len(df[df["Gender"] == "Female"]),
        "young_customers": len(df[df["Age"] < 30]),
        "oldest_customers": df["Age"].max(),
        "high_income_customers": len(df[df["Annual Income (k$)"] > 70]),
        "high_spenders": len(df[df["Spending Score (1-100)"] > 70]),
        "max_income": df["Annual Income (k$)"].max(),
        "max_spending": df["Spending Score (1-100)"].max(),
        "most_common":df["Age"].mode()[0],
    }
    return metrics

@st.cache_data
def cluster_summary(df):
    summary=(df.groupby("Clusters").agg({"Age":"mean","Annual Income (k$)":"mean","Spending Score (1-100)":"mean","CustomerID":"count"})
             .rename(columns={"CustomerID":"Customer Count"}).round(2).reset_index())
    return summary

@st.cache_data
def assign_segment_name(summary):
    segment_name={}
    for _,row in summary.iterrows():
        cluster=row["Clusters"]
        income=row["Annual Income (k$)"]
        spending=row["Spending Score (1-100)"]
        if income>65 and spending>60:
            segment_name[cluster]="Premium Customers"
        elif income>65 and spending<=60:
            segment_name[cluster]="Careful Customers"           
        elif income<=40 and spending<=40:
            segment_name[cluster]="Budget Customers"
        elif income<=45 and spending>60:
            segment_name[cluster]="Impulse Customers"
        else:
            segment_name[cluster]="Average Customers"
    return segment_name 

def apply_filters(
    df,
    gender="All",
    segment="All",
    age_range=None,
    income_range=None
):

    filtered_df = df.copy()

    if gender != "All":
        filtered_df = filtered_df[
            filtered_df["Gender"] == gender
        ]

    if segment != "All":
        filtered_df = filtered_df[
            filtered_df["Segment"] == segment
        ]

    if age_range:
        filtered_df = filtered_df[
            filtered_df["Age"].between(
                age_range[0],
                age_range[1]
            )
        ]

    return filtered_df

def get_filtered_data(df):
    defaults = {
        "gender_filter": "All",
        "segment_filter": "All",
        "age_filter": (
            int(df["Age"].min()),
            int(df["Age"].max())
        ),
        "income_filter": (
            int(df["Annual Income (k$)"].min()),
            int(df["Annual Income (k$)"].max())
        )
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

    st.sidebar.markdown("## 🔍 Filters")

    gender_filter = st.sidebar.selectbox(
        "Gender",
        ["All", "Male", "Female"],
        key="gender_filter"
    )

    segment_filter = st.sidebar.selectbox(
        "Segment",
        ["All"] + sorted(df["Segment"].unique().tolist()),
        key="segment_filter"
    )

    age_filter = st.sidebar.slider(
        "Age Range",
        min_value=int(df["Age"].min()),
        max_value=int(df["Age"].max()),
        key="age_filter"
    )

    st.sidebar.markdown("---")

    if st.sidebar.button(
        "🔄 Reset Filters",
        use_container_width=True
    ):

        st.session_state.clear()

        st.rerun()

    filtered_df = apply_filters(
        df,
        gender=gender_filter,
        segment=segment_filter,
        age_range=age_filter,
    )

    return filtered_df