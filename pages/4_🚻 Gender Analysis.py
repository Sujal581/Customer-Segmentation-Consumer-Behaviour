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

page_header("Gender Analysis","Customer Segmentation & Consumer Behaviour","🚻",)

#---Kpis---
section_header("📈 Key Performance Indicator")
kpis=calculate_kpis(df)

avg_spend_gender = df.groupby("Gender")["Spending Score (1-100)"].mean()
top_gender = avg_spend_gender.idxmax()
top_score = avg_spend_gender.max()

c1,c2,c3=st.columns(3)
kpi_card(c1,"Highest Spending Gender",f"{top_gender} ({top_score:.1f})",icon="🚻",color="#6B7280")
kpi_card(c2,"Males Customers",kpis["male_count"],icon="🚹",color="#0C6A73")
kpi_card(c3,"Females Customers",kpis["female_count"],icon="🚺",color="#1A4DB3")

#---Visualization---
c1,c2=st.columns(2)
with c1:
    section_header("🚻 Gender Distribution")
    chart_label("Customer Gender Distribution","Proportion of male and female customers in the dataset.")
    gender_dist=df["Gender"].value_counts().reset_index()
    gender_dist.columns=["Gender","Count"]
    fig=px.pie(gender_dist,names="Gender",values="Count",hole=0.5)
    apply_plot_layout(fig)
    st.plotly_chart(fig,use_container_width=True)
    dominant_gender = gender_dist.iloc[0]["Gender"]
    chart_note(f"The customer base is led by {dominant_gender} customers, providing insights into the primary audience for marketing and customer engagement strategies.")

with c2:
    section_header("🛒 Spenfding Score by Gender")
    chart_label("Average Spending Score by Gender","Comparison of spending behavior between male and female customers.")
    spending_gender=df.groupby("Gender")["Spending Score (1-100)"].mean().reset_index()
    fig=px.bar(spending_gender,x="Gender",y="Spending Score (1-100)",color="Gender")
    apply_plot_layout(fig)
    st.plotly_chart(fig,use_container_width=True)
    top_gender = spending_gender.loc[spending_gender["Spending Score (1-100)"].idxmax(),"Gender"]
    chart_note(f"{top_gender} customers have the highest average spending score, indicating stronger purchasing activity and customer engagement.")

c3,c4=st.columns(2)
with c3:
    section_header("💸 Income by Gender")
    chart_label("Average Income by Gender","Comparison of annual income levels between genders.")
    income_gender=df.groupby("Gender")["Annual Income (k$)"].mean().reset_index()
    fig=px.bar(income_gender,x="Gender",y="Annual Income (k$)",color="Annual Income (k$)")
    apply_plot_layout(fig)
    st.plotly_chart(fig,use_container_width=True)
    highest_income_gender = income_gender.loc[income_gender["Annual Income (k$)"].idxmax(),"Gender"]
    chart_note(f"{highest_income_gender} customers have the highest average annual income, reflecting greater purchasing capacity and potential value.")

with c4:
    section_header("🧩 Segment Breakdown by Gender")
    chart_label("Customer Segments by Gender","Distribution of customer segments across male and female customers.")
    seg_gender=df.groupby(["Gender","Segment"]).size().reset_index(name="Count")
    fig=px.bar(seg_gender,x="Segment",y="Count",color="Gender",barmode="group")
    apply_plot_layout(fig)
    st.plotly_chart(fig,use_container_width=True)
    chart_note("This chart highlights how customer segments are distributed across genders, helping identify demographic trends and opportunities for targeted marketing strategies.")


#---Insights---
section_header("📌 Business Insights")

top_segment_gender = (df.groupby(["Gender", "Segment"]).size().reset_index(name="Count").sort_values("Count", ascending=False).iloc[0])
insight_card(f"{top_gender} customers spend the most on average, making them a key target for loyalty programs and premium product offerings.",kind="success")
insight_card("Gender distribution is relatively balanced, suggesting marketing campaigns should address both customer groups effectively.",kind="info")
insight_card("Customer segments vary across genders, indicating opportunities for targeted promotions and personalized customer experiences.",kind="warning")
insight_card(f"The largest segment is {top_segment_gender['Segment']} among {top_segment_gender['Gender']} customers, containing {top_segment_gender['Count']} customers.",kind="info")

#---Footer---
footer()