import streamlit as st
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

df=load_data("Mall_Customers.csv")
df=clean_data(df)
scaled_data = scale_feature(df)
model, labels = perform_clustering(scaled_data)
df = add_clusters(df, labels) 
summary = cluster_summary(df)
segment_map = assign_segment_name(summary)
df["Segment"] = df["Clusters"].map(segment_map)
df=get_filtered_data(df)

page_header("Customer Segmentation","Customer Segmentation & Consumer Behaviour","👥",)

#---Kpis---
section_header("📈 Key Performance Indicator")
kpis=calculate_kpis(df)

premium = len(df[df["Segment"] == "Premium Customers"])
high_potential = len(df[df["Segment"] == "Careful Customers"])
budget = len(df[df["Segment"] == "Budget Customers"])
at_risk = len(df[df["Segment"] == "Impulse Customers"])

c1,c2,c3,c4,c5=st.columns(5)
kpi_card(c1, "Total Customers", f"{len(df):,}", icon="👥", color="red")
kpi_card(c2, "Average Age", f"{kpis['avg_age']:.1f} Years", icon="🎂", color="brown")
kpi_card(c3, "Average Income", f"${kpis['avg_income']:.1f}k", icon="💰", color="orange")
kpi_card(c4, "Average Spending Score", f"{kpis['avg_spending']:.1f}/100", icon="🛒", color="green")
kpi_card(c5, "Customer Segments", f"{df['Clusters'].nunique()}", icon="🎯", color="purple")

c6,c7,c8,c9=st.columns(4)
kpi_card(c6, "Premium Customers",premium,icon="💎",color="grey")
kpi_card(c7, "High Potential Customers",high_potential,icon="💡",color="black")
kpi_card(c8, "Budget Customers",budget,icon="🧮",color="brown")
kpi_card(c9, "At Risk Customers",at_risk,icon="⚠️",color="red")

#---Visualization---
c1,c2=st.columns(2)
with c1:
    section_header("📍 Customer Segments (Income vs Spending)")
    chart_label("Customer Segmentation Distribution","Scatter plot showing customer groups based on Annual Income and Spending Score.")
    fig=px.scatter(df,x="Annual Income (k$)",y="Spending Score (1-100)",color="Segment",hover_data=["Age","Gender"])
    fig.update_layout(xaxis_title="Annual Income (k$)",yaxis_title="Spending Score (1-100)",
                      xaxis=dict(title_font=dict(size=14, color="#374151"),tickfont=dict(size=12, color="#6B7280")),
                      yaxis=dict(title_font=dict(size=14, color="#374151"),tickfont=dict(size=12, color="#6B7280")))
    apply_plot_layout(fig)
    st.plotly_chart(fig,use_container_width=True)
    chart_note("This chart visualizes customer segments based on income and spending behavior, helping identify premium, careful, and budget-conscious customer groups.")

with c2:
    section_header("🧩 Segment Distribution")
    chart_label("Customer Segment Composition","Distribution of customers across the identified behavioral segments.")
    seg_dist=df["Segment"].value_counts().reset_index()
    seg_dist.columns=["Segment","Count"]
    fig=px.pie(seg_dist,names="Segment",values="Count",hole=0.5)
    apply_plot_layout(fig)
    st.plotly_chart(fig,use_container_width=True)
    largest_segment = seg_dist.iloc[0]["Segment"]
    largest_count = seg_dist.iloc[0]["Count"]
    chart_note("This donut chart shows the proportion of customers in each segment, helping identify the dominant customer groups and overall segment balance.")

c3,c4=st.columns(2)
with c3:
    section_header("🛒 Average Income by Spender")
    chart_label("Average Annual Income by Customer Segment","Comparison of average income levels across different customer segments.")
    income_seg=df.groupby("Segment")["Annual Income (k$)"].mean().reset_index()
    fig=px.bar(income_seg,x="Segment",y="Annual Income (k$)",text_auto=".1f",color="Annual Income (k$)")
    apply_plot_layout(fig)
    st.plotly_chart(fig,use_container_width=True)
    highest_income_seg = income_seg.loc[income_seg["Annual Income (k$)"].idxmax(), "Segment"]    
    chart_note(f"The {highest_income_seg} segment has the highest average annual income, indicating strong purchasing power and potential for premium product offerings.")

with c4:
    section_header("🧩 Average Spending by Segment")
    chart_label("Average Spending Score by Customer Segment","Comparison of average spending behavior across customer groups.")
    spending_seg=df.groupby("Segment")["Spending Score (1-100)"].mean().reset_index()
    fig=px.bar(spending_seg,x="Segment",y="Spending Score (1-100)",text_auto=".1f",color="Segment")
    apply_plot_layout(fig)
    st.plotly_chart(fig,use_container_width=True)
    highest_spending_seg = spending_seg.loc[spending_seg["Spending Score (1-100)"].idxmax(), "Segment"]
    chart_note(f"The {highest_spending_seg} segment records the highest average spending score, making it a key target group for customer retention and personalized marketing campaigns.")

segment_profile=df.groupby("Segment").agg({"Age":"mean","Annual Income (k$)":"mean","Spending Score (1-100)":"mean"}).round(1)
section_header("📋 Segment Profile")
chart_label("Customer Segment Characteristics","Average age, income, and spending score for each customer segment.")
st.table(segment_profile)
chart_note("This table summarizes the demographic and spending behavior of each customer segment, helping identify high-value and growth-opportunity groups.")

#---Insights---
section_header("🏢 Business Insight")
insight_card("Premium Customers generate highest revenue and should be targeted with loyalty program.",kind="success")
insight_card("Careful Customers have high income but low spending - ideal for marketing compaigns.",kind="info")
insight_card("Budget Customers are price sensitive and respond to disounts.",kind="warning")
insight_card("At - Risk Customers need retention strategies to prevent churn.",kind="error")

#---Footer---
footer()