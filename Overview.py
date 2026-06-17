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
df=add_clusters(df, labels) 
summary = cluster_summary(df)
segment_map = assign_segment_name(summary)
df["Segment"] = df["Clusters"].map(segment_map)
df=get_filtered_data(df)


page_header("Executive Overview","Customer Segmentation & Consumer Behaviour","📰",)

#---Kpis---
section_header("📈 Key Customer Metrics")
kpis=calculate_kpis(df)

c1,c2,c3,c4,c5=st.columns(5)
kpi_card(c1, "Total Customers", f"{len(df):,}", icon="👥", color="red")
kpi_card(c2, "Average Age", f"{kpis['avg_age']:.1f} Years", icon="🎂", color="brown")
kpi_card(c3, "Average Income", f"${kpis['avg_income']:.1f}k", icon="💰", color="orange")
kpi_card(c4, "Average Spending Score", f"{kpis['avg_spending']:.1f}/100", icon="🛒", color="green")
kpi_card(c5, "Customer Segments", f"{df['Clusters'].nunique()}", icon="🎯", color="purple")

c6, c7, c8, c9, c10 = st.columns(5)
kpi_card(c6, "Male Customers", kpis["male_count"], icon="👨", color="#2563EB")
kpi_card(c7, "Female Customers", kpis["female_count"], icon="👩", color="#EC4899")
kpi_card(c8, "High Income Customers", kpis["high_income_customers"], icon="💎", color="#F59E0B")
kpi_card(c9, "High Spenders", kpis["high_spenders"], icon="🛍️", color="#10B981")
kpi_card(c10, "Young Customers", kpis["young_customers"], icon="🚀", color="#8B5CF6")

#---Visualization---
c1,c2=st.columns(2)
with c1:
    section_header("🚻 Gender Distribution")
    chart_label("Customer Gender Analysis","Visual representation of customer composition across gender categories.")
    fig=px.pie(df,names="Gender",hole=0.5)
    apply_plot_layout(fig)
    st.plotly_chart(fig,use_container_width=True)
    chart_note("Understanding gender demographics enables businesses to design personalized products, campaigns, and customer engagement strategies.")

with c2:
    section_header("🎂 Age Distribution")
    chart_label("Customer Age Analysis","Distribution of customers across different age groups.")
    fig=px.histogram(df,x="Age",nbins=20,color_discrete_sequence=["#8B5CF6"])
    fig.update_traces(marker_line_width=1,marker_line_color="white")
    fig.update_layout(xaxis_title="Age (Years)",yaxis_title="Number of Customers",
                    xaxis=dict(title_font=dict(size=14, color="#374151"),tickfont=dict(size=12, color="#6B7280")),
                    yaxis=dict(title_font=dict(size=14, color="#374151"),tickfont=dict(size=12, color="#6B7280")))
    apply_plot_layout(fig)
    st.plotly_chart(fig,use_container_width=True)
    chart_note("The age distribution helps identify the dominant customer age groups and supports age-targeted marketing strategies.")

c3,c4=st.columns(2)
with c3:
    section_header("💰 Income Distribution")
    chart_label("Customer Income Analysis","Distribution of customers across annual income ranges.")
    fig = px.histogram(df,x="Annual Income (k$)",nbins=20,color_discrete_sequence=["#3B82F6"])
    fig.update_traces(marker_line_width=1,marker_line_color="white")
    fig.update_layout(xaxis_title="Annual Income (k$)",yaxis_title="Number of Customers",
        xaxis=dict(title_font=dict(size=14, color="#374151"),tickfont=dict(size=12, color="#6B7280")),
        yaxis=dict(title_font=dict(size=14, color="#374151"),tickfont=dict(size=12, color="#6B7280")))
    apply_plot_layout(fig)
    st.plotly_chart(fig, use_container_width=True)
    chart_note("Income distribution highlights customer purchasing power and helps identify premium and budget-oriented segments.")

with c4:
    section_header("🛒 Spending Score Distribution")
    chart_label("Customer Spending Analysis","Distribution of customer spending behavior scores.")
    fig = px.histogram(df,x="Spending Score (1-100)",nbins=20,color_discrete_sequence=["#EF4444"])
    fig.update_traces(marker_line_width=1,marker_line_color="white")
    fig.update_layout(
        xaxis_title="Spending Score (1-100)",yaxis_title="Number of Customers",
        xaxis=dict(title_font=dict(size=14, color="#374151"),tickfont=dict(size=12, color="#6B7280")),
        yaxis=dict(title_font=dict(size=14, color="#374151"),tickfont=dict(size=12, color="#6B7280")))
    apply_plot_layout(fig)
    st.plotly_chart(fig, use_container_width=True)
    chart_note("Spending scores reveal customer engagement and purchasing behavior, helping identify high-value customer groups.")

#---Insights---
section_header("💡 Key Insights & Findings")
male_pct = (df["Gender"].value_counts(normalize=True) * 100).round(1)
insight_card(f"🚻 {male_pct.index[0]} customers represent {male_pct.iloc[0]}% of the customer base, indicating a relatively balanced gender distribution.",kind="success")
insight_card(f"🥮 The average customer age is {df['Age'].mean():.1f} years, with the highest concentration of customers in the 25–40 age range.",kind="purple")
insight_card(f"💰 Customers have an average annual income of ${df['Annual Income (k$)'].mean():.1f}k, with most customers concentrated in the middle-income segment.",kind="success")
insight_card(f"🛒 The average spending score is {df['Spending Score (1-100)'].mean():.1f}/100, indicating a mix of highly engaged and budget-conscious customers.",kind="purple")

#---Footer---
footer()