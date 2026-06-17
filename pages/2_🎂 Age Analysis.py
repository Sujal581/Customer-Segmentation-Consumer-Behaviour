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

page_header("Age Analysis","Customer Segmentation & Consumer Behaviour","🎂",)

#---Kpis---
section_header("📈 Key Customer Metrics")
kpis=calculate_kpis(df)

c1,c2,c3=st.columns(3)
kpi_card(c1, "Average Age", f"{kpis['avg_age']:.1f} Years", icon="🎂", color="brown")
kpi_card(c2, "Young Customers", kpis["young_customers"], icon="🚀", color="#8B5CF6")
kpi_card(c3, "Oldest Customers", kpis["oldest_customers"], icon="👴🏻",color="#049019")

c4,c5,c6=st.columns(3)
kpi_card(c4, "Most Common Age", kpis["most_common"], icon="⭐",color="#7ACC2C")
kpi_card(c5, "High Spenders", kpis["high_spenders"], icon="🛍️", color="#0D7D58")
kpi_card(c6, "High Income Customers", kpis["high_income_customers"], icon="💰", color="#2B0474")

age_bins = [0, 20, 30, 40, 50, 60, 100]
age_labels = ["0-20","21-30","31-40","41-50","51-60","60+"]
df["Age Group"]=pd.cut(df["Age"],bins=age_bins,labels=age_labels)

#---Visualization---
c1,c2=st.columns(2)
with c1:
    section_header("👥 Customer Distribution by Age Group")
    chart_label("Age Group Segmentation","Breakdown of customers across predefined age categories.")
    fig=px.histogram(df,x="Age Group",color="Age Group")
    fig.update_layout(xaxis_title="Age Group (Years)",yaxis_title="Number of Customers",
                    xaxis=dict(title_font=dict(size=14, color="#374151"),tickfont=dict(size=12, color="#6B7280")),
                    yaxis=dict(title_font=dict(size=14, color="#374151"),tickfont=dict(size=12, color="#6B7280")))
    apply_plot_layout(fig)
    st.plotly_chart(fig,use_container_width=True)
    chart_note("Age group segmentation helps identify the most valuable customer demographics and enables age-specific marketing strategies.")

with c2:
    spending_age=df.groupby("Age Group")["Spending Score (1-100)"].mean().reset_index()
    section_header("🛒 Average Spending Score by Age Group")
    chart_label("Age Group Spending Analysis","Average spending score across different customer age segments.")
    fig=px.bar(spending_age,x="Age Group",y="Spending Score (1-100)",color="Age Group")
    fig.update_layout(xaxis_title="Age Group",yaxis_title="Average Spending Score",
                      xaxis=dict(title_font=dict(size=14, color="#374151"),tickfont=dict(size=12, color="#6B7280")),
                      yaxis=dict(title_font=dict(size=14, color="#374151"),tickfont=dict(size=12, color="#6B7280")))
    apply_plot_layout(fig)
    st.plotly_chart(fig,use_container_width=True)
    chart_note("Comparing spending scores across age groups helps identify which customer segments are most engaged and likely to generate higher revenue.")

c3,c4=st.columns(2)
with c3:
    income_age=df.groupby("Age Group")["Annual Income (k$)"].mean().reset_index()
    section_header("💰 Average Income by Age Group")
    chart_label("Age Group Income Analysis","Average annual income across different customer age segments.")
    fig=px.bar(income_age,x="Age Group",y="Annual Income (k$)",color="Age Group")
    fig.update_layout(xaxis_title="Age Group",yaxis_title="Average Annual Income",
                      xaxis=dict(title_font=dict(size=14, color="#374151"),tickfont=dict(size=12, color="#6B7280")),
                      yaxis=dict(title_font=dict(size=14, color="#374151"),tickfont=dict(size=12, color="#6B7280")))
    apply_plot_layout(fig)
    st.plotly_chart(fig,use_container_width=True)
    chart_note("Income levels across age groups provide insights into customer purchasing power and help identify high-value demographic segments.")

with c4:
    section_header("🛒 Age vs Spending Score")
    chart_label("Customer Spending Behavior","Relationship between customer age and spending score across identified segments.")
    fig=px.scatter(df,x="Age",y="Spending Score (1-100)",color="Clusters")
    fig.update_traces(marker=dict(size=10, opacity=0.8))
    fig.update_layout(xaxis_title="Age (Years)",yaxis_title="Spending Score (1-100)",
                      xaxis=dict(title_font=dict(size=14, color="#374151"),tickfont=dict(size=12, color="#6B7280")),
                      yaxis=dict(title_font=dict(size=14, color="#374151"),tickfont=dict(size=12, color="#6B7280")))
    apply_plot_layout(fig)
    st.plotly_chart(fig,use_container_width=True)
    chart_note("This scatter plot highlights spending patterns across different age groups and customer segments.")

section_header("💰 Age vs Annual Income")
chart_label("Income Distribution by Age","Relationship between customer age and annual income across different segments.")
fig=px.scatter(df,x="Age",y="Annual Income (k$)",color="Clusters")
fig.update_traces(marker=dict(size=10, opacity=0.8))
fig.update_layout(xaxis_title="Age (Years)",yaxis_title="Spending Score (1-100)",
                      xaxis=dict(title_font=dict(size=14, color="#374151"),tickfont=dict(size=12, color="#6B7280")),
                      yaxis=dict(title_font=dict(size=14, color="#374151"),tickfont=dict(size=12, color="#6B7280")))
apply_plot_layout(fig)
st.plotly_chart(fig,use_container_width=True)
chart_note("This visualization highlights how customer income varies across age groups and reveals distinct income-based customer segments.")

section_header("💡 Key Insights & Findings")
largest_group = df["Age Group"].value_counts().idxmax()
largest_count = df["Age Group"].value_counts().max()
top_group = income_age.loc[income_age["Annual Income (k$)"].idxmax(),"Age Group"]
top_income = income_age["Annual Income (k$)"].max()
top_group = spending_age.loc[spending_age["Spending Score (1-100)"].idxmax(),"Age Group"]
top_score = spending_age["Spending Score (1-100)"].max()
insight_card(f"The {largest_group} segment is the largest age category with {largest_count} customers, indicating the primary target audience for products and marketing campaigns.",kind="info")
insight_card(f"The {top_group} age group has the highest average spending score ({top_score:.1f}/100), making it a key target segment for premium products and marketing campaigns.",kind="success")
insight_card(f"The {top_group} age group has the highest average annual income (${top_income:.1f}k), indicating strong purchasing potential and suitability for premium offerings.",kind="success")
insight_card("Distinct customer clusters indicate varying spending behaviors, helping identify high-value and low-engagement customer groups for targeted marketing.",kind="warning")
insight_card("Customers with similar income levels tend to form natural clusters, helping identify high-income target segments and opportunities for personalized marketing.",kind="info")

#---Footer---
footer()