import streamlit as st
import plotly.express as px
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
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

page_header("Customer Segment Predictor","Predict Customer Segments and Receive Marketing Recommendation.","🤖",)


df_model=df.copy()
df_model["Gender"]=df_model["Gender"].map({"Male":0,"Female":1})
le=LabelEncoder()
df_model["Segment_Label"]=le.fit_transform(df_model["Segment"])
x=df_model[["Gender","Age","Annual Income (k$)","Spending Score (1-100)"]]
y=df_model["Segment_Label"]
model=RandomForestClassifier(n_estimators=200,random_state=42)
model.fit(x,y)

section_header("👨🏻 Customer Details")
c1,c2=st.columns(2)
with c1:
    gender=st.selectbox("Gender",["Male","Female"])
    age=st.slider("Age",min_value=18,max_value=80,value=30)

with c2:
    income=st.slider("Annual Income (k$)",min_value=0,max_value=150,value=50)
    spending=st.slider("Spending Score (1-100)",min_value=1,max_value=100,value=50)

predicted_segment = "Not Predicted"
if st.button("🚀 Predict Customer Segment"):

    gender_encoded = 0 if gender == "Male" else 1

    prediction = model.predict(
        [[gender_encoded, age, income, spending]]
    )[0]

    predicted_segment = le.inverse_transform([prediction])[0]

    # ==========================
    # PREDICTION RESULT
    # ==========================

    section_header("🎯 Prediction Result")

    icons = {
        "Premium Customers": "💎",
        "Careful Customers": "🎯",
        "Budget Customers": "💰",
        "Impulse Customers": "🛍️",
        "Average Customers": "👥"
    }

    st.markdown(
        f"""
        <div style="
            background: linear-gradient(135deg,#DCEAFE,#DBEAFE);
            padding:25px;
            border-radius:16px;
            border-left:6px solid #2563EB;
            margin-bottom:15px;
            box-shadow:0 4px 12px rgba(37,99,235,0.12);
        ">
            <h3 style="margin:0;color:#1E3A8A;">
                {icons.get(predicted_segment,'👥')} Predicted Segment
            </h3>
            <h2 style="margin-top:10px;color:#1E293B;">
                {predicted_segment}
            </h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    #---Customer Profile---
    section_header("📋 Customer Profile")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Gender", gender)
    c2.metric("Age", age)
    c3.metric("Income", f"${income}k")
    c4.metric("Spending Score", spending)

    #---Insights---
    section_header("💡 Business Insights")
    if predicted_segment == "Premium Customers":
        st.success("This customer has high purchasing power and high spending behavior.")
        st.info("A high-value customer who contributes significantly to revenue.")
    elif predicted_segment == "Careful Customers":
        st.warning("This customer earns well but spends conservatively.")
        st.info("Strong opportunity for upselling and personalized campaigns.")
    elif predicted_segment == "Budget Customers":
        st.warning("This customer shows lower income and lower spending patterns.")
        st.info("Focus on affordability, discounts, and value-driven offers.")
    elif predicted_segment == "Impulse Customers":
        st.success("This customer spends frequently despite moderate income.")
        st.info("Responds well to flash sales and limited-time promotion.")
    else:
        st.info("This customer demonstrates balanced purchasing behavior.")
        st.success("Maintain engagement through personalized recommendations.")

    #---Recommendation---
    section_header("🚀 Marketing Recommendations")
    recommendations = {
        "Premium Customers": [
            "VIP Membership Programs",
            "Premium Product Launches",
            "Exclusive Events",
            "Reward Points"
        ],
        "Careful Customers": [
            "Personalized Promotions",
            "Product Bundles",
            "Cross-Selling",
            "Upselling Campaigns"
        ],
        "Budget Customers": [
            "Discount Coupons",
            "Seasonal Sales",
            "Value Packs",
            "Budget-Friendly Offers"
        ],
        "Impulse Customers": [
            "Flash Sales",
            "Limited-Time Deals",
            "Trending Products",
            "Social Media Campaigns"
        ],
        "Average Customers": [
            "Loyalty Rewards",
            "Email Campaigns",
            "Product Recommendations",
            "Customer Engagement Programs"
        ]
    }
    for rec in recommendations[predicted_segment]:
        st.markdown(f"✅ {rec}")

    section_header("📊 Prediction Drivers")
    chart_label("Feature Importance Analysis","Shows the relative contribution of each customer attribute in predicting customer segments.")
    importance = pd.DataFrame({"Feature": x.columns,"Importance": model.feature_importances_}).sort_values(by="Importance",ascending=False)
    fig = px.bar(importance,x="Importance",y="Feature",orientation="h",text_auto=".2f",color="Feature")
    apply_plot_layout(fig)
    st.plotly_chart(fig,use_container_width=True)
    top_feature = importance.iloc[0]["Feature"]
    top_importance = importance.iloc[0]["Importance"]
    chart_note(f"{top_feature} is the most influential feature in the prediction model with an importance score of {top_importance:.2f}. Higher feature importance indicates a stronger impact on determining customer segments.")

#---Footer---
footer()