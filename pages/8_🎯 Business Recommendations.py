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


page_header("Business Recommendations","Strategic actions to improve customer engagement, retention, and revenue.","🎯")


#--- KPIs---
premium = len(df[df["Segment"] == "Premium Customers"])
careful = len(df[df["Segment"] == "Careful Customers"])
impulse = len(df[df["Segment"] == "Impulse Customers"])
budget = len(df[df["Segment"] == "Budget Customers"])

c1, c2, c3, c4 = st.columns(4)

kpi_card(c1, "Premium", premium, "💎",color="red")
kpi_card(c2, "Careful", careful, "🎯",color="orange")
kpi_card(c3, "Impulse", impulse, "🛍️",color="purple")
kpi_card(c4, "Budget", budget, "💰",color="blue")

#--- SEGMENT COUNTS---
section_header("📊 Customer Segment Distribution")
chart_label("Customers by Segment")
segment_dist = (df["Segment"].value_counts().reset_index())
segment_dist.columns = ["Segment","Customers"]
fig = px.bar(segment_dist,x="Segment",y="Customers",color="Segment",text_auto=True)
apply_plot_layout(fig)
st.plotly_chart(fig,use_container_width=True)
chart_note("Shows the size of each customer segment and helps prioritize marketing efforts.")

#--- STRATEGY TABLE---
section_header("📋 Recommended Actions")
recommendations = pd.DataFrame({
    "Customer Segment":[
        "Premium Customers",
        "Careful Customers",
        "Impulse Customers",
        "Budget Customers",
        "Average Customers"
    ],
    "Business Goal":[
        "Retention",
        "Increase Spending",
        "Boost Purchases",
        "Improve Conversion",
        "Increase Engagement"
    ],
    "Recommended Strategy":[
        "VIP Programs & Loyalty Rewards",
        "Personalized Offers & Upselling",
        "Flash Sales & Limited-Time Deals",
        "Discounts & Bundle Offers",
        "Targeted Marketing Campaigns"
    ]
})
st.table(recommendations)

#--- MARKETING PRIORITY---
section_header("🚀 Marketing Priority")
chart_label("Marketing Priority Score")
priority = pd.DataFrame({
    "Segment":["Premium Customers","Careful Customers","Impulse Customers","Average Customers","Budget Customers"],
    "Priority Score":[100,90,85,75,60]})
fig = px.bar(priority,x="Segment",y="Priority Score",color="Segment",text_auto=True)
apply_plot_layout(fig)
st.plotly_chart(fig,use_container_width=True)
chart_note("Higher priority segments offer the greatest business impact.")

#--- RECOMMENDATIONS---
section_header("💡 Strategic Recommendations")
insight_card("Premium Customers should receive loyalty rewards, exclusive offers, and VIP experiences to maximize retention.")
insight_card("Careful Customers have strong purchasing power but lower spending behaviour, making them ideal candidates for upselling campaigns.")
insight_card("Impulse Customers respond well to flash sales, urgency marketing, and limited-time promotions.")
insight_card("Budget Customers are highly price-sensitive and should be targeted using discounts, bundles, and cashback offers.")
insight_card("Average Customers can be nurtured into higher-value segments through personalized engagement campaigns.")

#--- MARKETING ACTION PLAN---
section_header("📣 Marketing Action Plan")
st.markdown("""
### 💎 Premium Customers
- VIP Membership Programs
- Loyalty Rewards
- Exclusive Product Launches
- Personalized Shopping Experiences

### 🎯 Careful Customers
- Upselling Campaigns
- Product Bundles
- Personalized Recommendations
- Premium Product Promotions

### 🛍️ Impulse Customers
- Flash Sales
- Limited-Time Discounts
- Festival Promotions
- Social Media Advertising

### 💰 Budget Customers
- Discount Coupons
- Cashback Offers
- Seasonal Deals
- Value Bundles

### 👥 Average Customers
- Email Marketing
- Customer Retention Programs
- Referral Campaigns
- Product Discovery Initiatives
""")

#--- EXECUTIVE SUMMARY---
section_header("📌 Executive Summary")
st.success("Premium Customers represent the most valuable customer segment and should be prioritized for retention.")
st.info("Careful Customers provide the largest revenue growth opportunity because they have high income but lower spending.")
st.warning("Budget Customers require price-focused strategies to improve engagement and conversion rates.")
st.success("Segment-specific marketing campaigns can significantly improve customer satisfaction and business performance.")