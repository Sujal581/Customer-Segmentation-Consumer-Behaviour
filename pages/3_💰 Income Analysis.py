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

page_header("Income Analysis","Customer Segmentation & Consumer Behaviour","💰",)

#---Kpis---
section_header("📈 Key Performance Indicator")
kpis=calculate_kpis(df)

c1,c2,c3=st.columns(3)
kpi_card(c1, "Average Income", f"${kpis['avg_income']:.1f}k", icon="💰", color="orange")
kpi_card(c2, "High Income Customers", kpis["high_income_customers"], icon="💎", color="#876325")
kpi_card(c3, "High Income", f"{df['Annual Income (k$)'].max():.1f}k", icon="📈", color="#F59E0B")

#---Visualization---
c1,c2=st.columns(2)
with c1:
    section_header("💰 Income Distribution")
    chart_label("Customer Income Distribution","Distribution of customers across different annual income levels.")
    fig=px.histogram(df,x="Annual Income (k$)",nbins=20)
    fig.update_traces(marker_line_width=1,marker_line_color="white")
    fig.update_layout(xaxis_title="Annual Income",yaxis_title="Number of Customers",
                    xaxis=dict(title_font=dict(size=14, color="#374151"),tickfont=dict(size=12, color="#6B7280")),
                    yaxis=dict(title_font=dict(size=14, color="#374151"),tickfont=dict(size=12, color="#6B7280")))
    apply_plot_layout(fig)
    st.plotly_chart(fig,use_container_width=True)
    chart_note("This histogram shows how customers are distributed across income levels, helping identify the most common income ranges and potential target markets.")

with c2:
    section_header("🛒 Income vs Spending Score")
    chart_label("Income vs Spending Behavior","Relationship between customer income levels and spending patterns.")
    fig=px.scatter(df,x="Annual Income (k$)",y="Spending Score (1-100)",color="Segment",hover_data=["Age","Gender"])
    apply_plot_layout(fig)
    st.plotly_chart(fig,use_container_width=True)
    chart_note("This scatter plot reveals customer spending behavior across income levels. Distinct clusters help identify premium, careful, impulse, and budget-conscious customer segments.")

c3,c4=st.columns(2)
with c3:
    section_header("🧩 Average Income by Segment")
    chart_label("Average Income by Customer Segment","Comparison of average annual income across different customer groups.")
    income_seg=df.groupby("Segment")["Annual Income (k$)"].mean().reset_index()
    fig=px.bar(income_seg,x="Segment",y="Annual Income (k$)",text_auto=".1f",color="Segment")
    apply_plot_layout(fig)
    st.plotly_chart(fig,use_container_width=True)
    highest_income_segment = income_seg.loc[income_seg["Annual Income (k$)"].idxmax(),"Segment"]
    chart_note(f"The {highest_income_segment} segment has the highest average annual income, indicating strong purchasing power and potential for premium offerings.")


with c4:
    section_header("💸 Income Categories")
    chart_label("Customer Income Category Distribution","Proportion of customers across low, medium, and high income groups.")
    df["Income Category"]=pd.cut(df["Annual Income (k$)"],bins=[0,40,70,120],labels=["Low","Medium","High",])
    income_cat=df["Income Category"].value_counts().reset_index()
    income_cat.columns=["Income Category","Count"]
    fig=px.pie(income_cat,names="Income Category",values="Count",hole=0.5)
    apply_plot_layout(fig)
    st.plotly_chart(fig,use_container_width=True)
    largest_category = income_cat.iloc[0]["Income Category"]
    chart_note(f"The {largest_category} income category represents the largest share of customers, helping identify the primary target market and customer purchasing capacity.")


section_header("🧠 Business Decision Panel")
highest_income=df[(df["Annual Income (k$)"]>=70) & (df["Spending Score (1-100)"]<=40)]
lowest_income=df[(df["Annual Income (k$)"]<=40) & (df["Spending Score (1-100)"]>=60)]
premium_target=df[(df["Annual Income (k$)"]>=70) & (df["Spending Score (1-100)"]>=60)]

c1,c2,c3=st.columns(3)
kpi_card(c1, "High Income Customers",len(highest_income), icon="💎", color="#876325")
kpi_card(c2, "Low Income Customers",len(lowest_income), icon="📉", color="#373023")
kpi_card(c3, "High Income Customers",len(premium_target), icon="👑", color="#CF8301")

#---Insight---
section_header("📌 Key Business Insights")
insight_card("Premium customers (high income, high spending) should be targeted with VIP programs, exclusive memberships, personalized recommendations, and premium offers to maximize customer lifetime value.",kind="success")
insight_card("High-income but low-spending customers represent the strongest upselling opportunity. Personalized marketing campaigns and targeted product recommendations can help increase their spending.",kind="info")
insight_card("Low-income but high-spending customers are highly responsive to discounts, flash sales, loyalty rewards, and value-driven promotional campaigns.",kind="warning")
insight_card("Low-income and low-spending customers contribute limited revenue. Focus on cost-effective retention strategies rather than high marketing expenditure.",kind="error")

#---Footer---
footer()