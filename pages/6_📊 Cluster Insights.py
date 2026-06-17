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
scaled_data = scale_feature(df)
model, labels = perform_clustering(scaled_data)
df = add_clusters(df, labels)
summary = cluster_summary(df)
segment_map = assign_segment_name(summary)
df["Segment"] = df["Clusters"].map(segment_map)
df = get_filtered_data(df)

if df.empty:
    st.warning("⚠️ No customers match the selected filters.")
    st.stop()

page_header("Cluster Insights","Detailed analysis of customer segments and cluster behavior.","📊")

#--- KPIs---
segment_counts = df["Segment"].value_counts()
largest_segment = segment_counts.idxmax()
largest_count = segment_counts.max()
premium = len(df[df["Segment"] == "Premium Customers"])
careful = len(df[df["Segment"] == "Careful Customers"])
budget = len(df[df["Segment"] == "Budget Customers"])
impulse = len(df[df["Segment"] == "Impulse Customers"])

c1, c2, c3, c4 = st.columns(4)
kpi_card(c1, "Largest Segment", largest_segment, "👥",color="red")
kpi_card(c2, "Premium Customers", premium, "💎",color="blue")
kpi_card(c3, "Careful Customers", careful, "🎯",color="green")
kpi_card(c4, "Budget Customers", budget, "💰",color="orange")


#--- SEGMENT DISTRIBUTION---
section_header("📊 Segment Distribution")
segment_dist = (df["Segment"].value_counts().reset_index())
segment_dist.columns = ["Segment","Customers"]
chart_label("Customer Segment Distribution")
fig = px.pie(segment_dist,names="Segment",values="Customers",hole=0.5)
apply_plot_layout(fig)
st.plotly_chart(fig, use_container_width=True)
chart_note("Shows the percentage contribution of each customer segment.")


#--- INCOME VS SPENDING---
section_header("💰 Income vs Spending Score")
chart_label("Income vs Spending by Segment")
fig = px.scatter(df,x="Annual Income (k$)",y="Spending Score (1-100)",color="Segment",size="Age",hover_data=["Gender"])
apply_plot_layout(fig)
st.plotly_chart(fig,use_container_width=True)
chart_note("Visualizes customer purchasing behaviour across different segments.")

#--- SEGMENT-WISE METRICS---
section_header("📈 Segment Performance")
chart_label("Average Spending Score by Segment")
segment_metrics = (df.groupby("Segment").agg({"Age": "mean","Annual Income (k$)": "mean","Spending Score (1-100)": "mean"}).round(2).reset_index())
fig = px.bar(segment_metrics,x="Segment",y="Spending Score (1-100)",color="Segment",text_auto=".1f")
apply_plot_layout(fig)
st.plotly_chart(fig,use_container_width=True)
chart_note("Compares spending behaviour across customer segments.")

#--- CLUSTER SUMMARY TABLE---
section_header("📋 Cluster Summary")
summary_table = (df.groupby("Segment").agg({"Age": "mean","Annual Income (k$)": "mean","Spending Score (1-100)": "mean","CustomerID": "count"}).rename(columns={"CustomerID": "Customer Count"}).round(2))
st.table(summary_table,)

#--- SEGMENT PERSONAS---
section_header("👤 Segment Personas")
c1, c2 = st.columns(2)
with c1:
    insight_card("Premium Customers: High Income + High Spending. These customers generate the highest business value.")
    insight_card("Careful Customers: High Income + Low Spending. Strong potential for upselling and targeted promotions.")
    insight_card("Impulse Customers: Moderate Income + High Spending. Respond well to flash sales and limited-time offers.")

with c2:
    insight_card("Budget Customers: Low Income + Low Spending. Highly price-sensitive customer group.")
    insight_card("Average Customers: Moderate Income + Moderate Spending. Stable customer base with growth potential.")


#--- BUSINESS INSIGHTS---
section_header("💡 Business Insights")
top_segment = (df.groupby("Segment")["Spending Score (1-100)"].mean().idxmax())
top_income_segment = (df.groupby("Segment")["Annual Income (k$)"].mean().idxmax())
insight_card(f"The {top_segment} segment has the highest average spending score and represents the most valuable customer group.")
insight_card(f"The {top_income_segment} segment has the highest average income and offers significant revenue opportunities.")
insight_card("Customer spending behaviour differs significantly across segments, validating the effectiveness of clustering.")
insight_card("Personalized marketing strategies should be developed for each segment to maximize engagement and revenue.")