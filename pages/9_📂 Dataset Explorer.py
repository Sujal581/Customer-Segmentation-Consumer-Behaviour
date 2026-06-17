import streamlit as st
import pandas as pd
import plotly.express as px

from utils import *
from styles import *

st.set_page_config(    
    page_icon="👥",
    page_title="Customer Segmentation & Consumer Behaviour",
    layout="wide",
    initial_sidebar_state="expanded",
)

inject_css()
sidebar_brand()

df = load_data("Mall_Customers.csv")
df = clean_data(df)

page_header("Dataset Explorer","Explore dataset structure, quality, and statistical information.","📂")

#--- KPIs---
missing_values = df.isnull().sum().sum()
duplicates = df.duplicated().sum()

c1, c2, c3, c4 = st.columns(4)
kpi_card(c1, "Rows", len(df), "📄",color="orange")
kpi_card(c2, "Columns", len(df.columns), "📋",color="purple")
kpi_card(c3, "Missing Values", missing_values, "⚠️",color="blue")
kpi_card(c4, "Duplicates", duplicates, "🔁",color="red")

#--- DATASET PREVIEW---
section_header("👀 Dataset Preview")
rows = st.slider("Select Rows",min_value=5,max_value=50,value=10)
st.table(df.head(rows))
chart_note("Preview of customer records from the dataset.")

#--- COLUMN INFORMATION---
section_header("📋 Column Information")
column_info = pd.DataFrame({"Column": df.columns,"Data Type": df.dtypes.astype(str),"Missing Values": df.isnull().sum().values,"Unique Values": [df[col].nunique() for col in df.columns]})
st.table(column_info)

#--- STATISTICAL SUMMARY---
section_header("📈 Statistical Summary")
st.table(df.describe())


#--- DATA TYPES---
section_header("🧩 Data Type Distribution")
dtype_df = (pd.DataFrame(df.dtypes.astype(str).value_counts()).reset_index())
dtype_df.columns = ["Data Type","Count"]
chart_label("Data Type Distribution")
fig = px.pie(dtype_df,names="Data Type",values="Count",hole=0.5)
apply_plot_layout(fig)
st.plotly_chart(fig,use_container_width=True)
chart_note("Distribution of column data types.")


#--- CORRELATION MATRIX---
section_header("🔗 Correlation Analysis")
corr = (df.select_dtypes(include="number").corr())
chart_label("Correlation Matrix")
fig = px.imshow(corr,text_auto=".2f",aspect="auto")
apply_plot_layout(fig)
st.plotly_chart(fig,use_container_width=True)
chart_note("Displays relationships between numerical variables.")


#--- DATASET DESCRIPTION---
section_header("📚 Dataset Description")
st.markdown("""
### Dataset Features

- **CustomerID** → Unique identifier for each customer
- **Gender** → Customer gender
- **Age** → Customer age
- **Annual Income (k$)** → Annual income in thousands of dollars
- **Spending Score (1-100)** → Customer spending behavior score

### Objective
Identify customer segments using K-Means Clustering and generate business recommendations for targeted marketing strategies.
""")

#---Download Dataset---
section_header("⬇️ Download Dataset")
csv = df.to_csv(index=False)
st.download_button(label="Download Dataset",data=csv,file_name="Mall_Customers.csv",mime="text/csv")

#---Insights---
section_header("💡 Key Observations")
insight_card(f"The dataset contains {len(df)} customer records and {len(df.columns)} attributes.",kind="info")
insight_card("Age, Annual Income, and Spending Score are the primary variables used for customer segmentation.",kind="success")
insight_card("The dataset is clean and suitable for clustering analysis after preprocessing.",kind="success")
insight_card("Correlation analysis helps identify relationships between customer demographics and spending behavior.")