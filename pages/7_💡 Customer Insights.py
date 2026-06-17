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


page_header("Customer Insights","Discover key customer behaviour patterns and business opportunities.","💡")

df["Age Group"] = pd.cut(df["Age"],bins=[0, 25, 35, 45, 55, 100],labels=["18-25","26-35","36-45","46-55","55+"])
top_age_group = (df.groupby("Age Group")["Spending Score (1-100)"].mean().idxmax())
top_segment = (df.groupby("Segment")["Spending Score (1-100)"].mean().idxmax())
highest_income_segment = (df.groupby("Segment")["Annual Income (k$)"].mean().idxmax())
premium_count = len(df[df["Segment"] == "Premium Customers"])

#--- KPIs---
section_header("📈 Key Performance")
c1, c2, c3, c4 = st.columns(4)
kpi_card(c1, "Top Spending Age Group", top_age_group, "🛒",color="red")
kpi_card(c2, "Best Performing Segment", top_segment, "🏆",color="blue")
kpi_card(c3, "Highest Income Segment", highest_income_segment, "💰",color="purple")
kpi_card(c4, "Premium Customers", premium_count, "💎",color="green")

#--- AGE GROUP INSIGHTS---
section_header("🎂 Spending Behaviour by Age Group")
chart_label("Average Spending Score by Age Group")
age_spending = (df.groupby("Age Group")["Spending Score (1-100)"].mean().reset_index())
fig = px.bar(age_spending,x="Age Group",y="Spending Score (1-100)",text_auto=".1f",color="Age Group")
apply_plot_layout(fig)
st.plotly_chart(fig,use_container_width=True)
chart_note("Identifies which age groups contribute the highest spending.")

#---SEGMENT PERFORMANCE---
section_header("🏆 Segment Performance")
chart_label("Average Spending Score by Segment")
segment_performance = (df.groupby("Segment")[["Annual Income (k$)","Spending Score (1-100)"]].mean().round(2).reset_index())
fig = px.bar(segment_performance,x="Segment",y="Spending Score (1-100)",color="Segment",text_auto=".1f")
apply_plot_layout(fig)
st.plotly_chart(fig,use_container_width=True)
chart_note("Shows which customer segments generate the strongest spending behaviour.")

#--- GENDER INSIGHTS---
section_header("🚻 Spending by Gender")
chart_label("Average Spending Score by Gender")
gender_spending = (df.groupby("Gender")["Spending Score (1-100)"].mean().reset_index())
fig = px.pie(gender_spending,names="Gender",values="Spending Score (1-100)",hole=0.5)
apply_plot_layout(fig)
st.plotly_chart(fig,use_container_width=True)
chart_note("Compares customer spending patterns by gender.")

#--- INCOME VS SPENDING---
section_header("💰 Income vs Spending Behaviour")
chart_label("Income vs Spending Score")
fig = px.scatter(df,x="Annual Income (k$)",y="Spending Score (1-100)",color="Segment",size="Age",hover_data=["Gender"])
apply_plot_layout(fig)
st.plotly_chart(fig,use_container_width=True)
chart_note("Shows how customer spending changes across income levels.")

#--- KEY BUSINESS FINDINGS---
section_header("💡 Key Business Findings")
highest_spending_age = age_spending.loc[age_spending["Spending Score (1-100)"].idxmax(),"Age Group"]
highest_segment = segment_performance.loc[segment_performance["Spending Score (1-100)"].idxmax(),"Segment"]
insight_card(f"Customers aged {highest_spending_age} exhibit the highest average spending behaviour and represent a valuable target audience.")
insight_card(f"{highest_segment} generate the strongest spending performance and should be prioritized in customer retention strategies.")
insight_card("High-income customers do not always spend the most, highlighting opportunities for personalized marketing campaigns.")
insight_card("Customer behaviour varies significantly across age groups, genders, and segments, reinforcing the value of targeted marketing.")
insight_card("Segment-specific promotions can increase customer engagement and improve overall revenue generation.")

#--- QUESTIONS ANSWERED---
section_header("❓ Questions Answered")

st.markdown("""
✅ Which age group spends the most?
            
✅ Which customer segment performs best?
            
✅ Do higher-income customers always spend more?
            
✅ Which gender spends more on average?
            
✅ Which customer group should marketing focus on?
            
✅ What business opportunities exist within each segment?
""")