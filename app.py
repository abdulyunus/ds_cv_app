import streamlit as st
import plotly.express as px
import pandas as pd
import os


# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="Abdul Yunus | Data Scientist",
    page_icon="📊",
    layout="wide"
)

# ---------------- HEADER ----------------
st.markdown("""
    <h1 style='text-align: center; font-size: 3rem; margin-bottom: 0.2em;'>Abdul Yunus</h1>
""", unsafe_allow_html=True)

st.markdown("""
    <h3 style='text-align: center; font-weight: normal; margin-top: -1em;'>Lead Data Scientist | Advanced Analytics | Supply Chain & Retail</h3>
""", unsafe_allow_html=True)

col_contact1, col_contact2 = st.columns(2)
with col_contact1:
    st.markdown("<div style='text-align: left; font-size: 1.1rem;'>📍106, Reliance Jubilee, Kohesar colony <br> Shaikhpet <br> Hyderabad, India</div>", unsafe_allow_html=True)
with col_contact2:
    st.markdown("""
        <div style='text-align: right; font-size: 1.1rem;'>
            📞 +91-9886251763, +91- 7020668859 <br>
            📧 abdul.yg@gmail.com  <br>
            <a href='https://github.com/abdulyunus' target='_blank' style='text-decoration: underline; color: #1976d2; font-weight: bold;'>
                <img src='https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png' alt='GitHub' style='width: 22px; height: 22px; vertical-align: middle; margin-right: 6px; border-radius: 4px;'/> https://github.com/abdulyunus
            </a>
        </div>
    """, unsafe_allow_html=True)

st.divider()

# ---------------- DOWNLOAD CV ----------------
st.markdown("### 📄 Download CV")

cv_file = None
cv_filename = None
cv_mime = None

# Auto-detect CV file
if os.path.exists("Abdul_Yunus_CV.pdf"):
    cv_file = "Abdul_Yunus_CV.pdf"
    cv_filename = "Abdul_Yunus_Data_Scientist.pdf"
    cv_mime = "application/pdf"

elif os.path.exists("Abdul_Yunus_CV.docx"):
    cv_file = "Abdul_Yunus_CV.docx"
    cv_filename = "Abdul_Yunus_Data_Scientist.docx"
    cv_mime = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"

if cv_file:
    with open(cv_file, "rb") as file:
        st.download_button(
            label="⬇️ Download CV",
            data=file,
            file_name=cv_filename,
            mime=cv_mime
        )
else:
    st.warning("CV file not found. Please upload a PDF or DOCX resume.")


# ---------------- CAREER SUMMARY ----------------
st.header("🚀 Career Summary")

st.markdown(
    """
Data Science and Advanced Analytics professional with **10+** years of experience delivering statistical modeling, machine learning, and forecasting solutions as a hands-on contributor. 
Known for owning analytical problem statements end-to-end, 
collaborating with cross-functional teams, and supporting stakeholders with data-driven insights, clear narratives, and practical recommendations across Retail, CPG, and Supply Chain domains.

Strong at translating complex data into **actionable business insights**, building
**production-grade ML solutions**, and collaborating with global stakeholders.
"""
)

# ---------------- SKILLS ----------------
st.header("🧠 Core Skills")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**Machine Learning**")
    st.markdown(
        """
        - Regression (Linear, Logistic, Ridge, LASSO)  
        - Tree Models (DT, RF, XGBoost)  
        - Clustering (K-Means, DBSCAN)  
        - PCA, Naïve Bayes, SVM  
        - Time Series Forecasting  
        """
    )

with col2:
    st.markdown("**Analytics & Domain**")
    st.markdown(
        """
        - Anomaly Detection & RCA  
        - Exploratory Data Analysis  
        - Demand Forecasting  
        - Retail & CPG Analytics  
        - Supply Chain Analytics  
        """
    )

with col3:
    st.markdown("**Tech Stack**")
    st.markdown(
        """
        - Python, R, PySpark  
        - Snowflake, SQL Server  
        - Kafka, Azure Functions  
        - Streamlit, Docker  
        """
    )

# ---------------- EXPERIENCE METRICS ----------------
st.header("📊 Experience Snapshot")

metrics = st.columns(3)
metrics[0].metric("Years Experience", "10+", "📈")
metrics[1].metric("Industry worked / Domain", "Retail | Supply Chain")
metrics[2].metric("Team Size Led", "7")

# ---------------- EXPERIENCE ----------------
st.header("💼 Professional Experience")

with st.expander("🔹 Lead Software Engineer – Data Science | Blue Yonder (2019–Present)"):
    st.markdown(
        """
- Built **Anomaly Detection systems** using clustering, EDA, and Root Cause Analysis  
- Designed **microservices-based analytics applications** (Supplier Insights, Store Insights etc) on Stratosphere SaaS  
- Processed **5M+ records** using optimized pipelines  
- Developed **Alerts & Narratives engine** monitoring 50+ KPIs across 5 BY apps  
- Contributed to **customer & supplier scoring models**  
- Contributed to the development of **Data Doctor**, a data validation and monitoring tool used across BY applications
- Led mentoring, customer demos, documentation, and production releases  
"""
    )

with st.expander("🔹 Senior Data Analyst | EPAM Systems (2017–2019)"):
    st.markdown(
        """
- Developed **Regional Event Demand Forecasting** model  for large food chains in North America  
- Built **Limited Time Offer & promotional forecasts** using time-series models
- Conducted **trend, seasonality, and EDA** to improve forecast accuracy  
- Collaborated cross-functionally to refine business assumptions  
"""
    )

with st.expander("🔹 Senior Executive – Data Science | Nielsen (2015–2017)"):
    st.markdown(
        """
- Led **retail universe estimation** (numeric & volumetric)  - Market Research Project
- Built **predictive sales & category forecasting models**  
- Designed **stratified sampling & clustering-based samples**  
- Presented insights to global stakeholders across **MENA**  
"""
    )

with st.expander("🔹 Senior Business Analyst | TCS (2012–2015)"):
    st.markdown(
        """
- Translated business problems into analytical solutions  
- Designed **market segmentation & estimation models**  
- Delivered insights using **data visualization & storytelling**  
"""
    )

# ---------------- PROJECTS ----------------
st.header("📈 Project Worked On")
st.markdown("""
- Development of Shopper Insights, Exploratory Data Analysis and Anomaly detection on python, used micro service architecture and deployed on the platform.
- Contributed to the design and implementation of customer and supplier scoring models, applying analytical and statistical techniques to support data-driven evaluation and prioritization.
- Designed and developed a Python-based Alerts and Narratives system for Blue Yonder’s industry solutions, supporting 5 BY applications and monitoring 50+ KPIs to deliver proactive insights.
- Designed and Development of Customer scoring algorithm in python as a part of POC for Tech Mahindra. This algorithm uses, Clustering, Principal component Analysis and XG Boost, Random Forest ML Algorithms.
- Contributed to the development, testing, and real-time implementation of Data Doctor, Blue Yonder’s data validation and monitoring tool used across JDA applications to ensure data quality and reliability.
- Developed Data Doctor data quality summary reports supporting both real-time and batch processing modes, providing visibility into data health across Blue Yonder applications.
- Developed Outlier computation module, metadata computation module which use basic descriptive stats.
- Delivered a Python-based Order Lead Time Profiling solution for a Tech Mahindra POC, applying statistical analysis and time-series forecasting to improve lead time estimation.
- Developed Demand confidence band algorithm in Python. This algorithm uses basic statistics to compute the demand confidence band.
""")

# ---------------- SKILLS VISUAL ----------------
st.header("📈 Skill Distribution")

skills_df = pd.DataFrame({
    "Skill Area": [
        "Machine Learning",
        "Forecasting",
        "Python",
        "Snowflake",
        "streamlit",
        "Data Engineering"
    ],
    "Strength": [8.0, 7.5, 8.0, 7.5, 6.0, 6.5]
})

# Use a color map for more vibrant, supportive colors
color_map = px.colors.qualitative.Plotly
bar_colors = [color_map[i % len(color_map)] for i in range(len(skills_df))]

# Create a slimmer bar chart with sharper axis values
fig = px.bar(
    skills_df,
    x="Skill Area",
    y="Strength",
    text="Strength",
    title="Data Science Skill Strength",
    color="Skill Area",
    color_discrete_sequence=bar_colors
)
fig.update_traces(
    textfont_size=16,
    marker_line_color='#222',
    marker_line_width=2,
    width=0.4
)
fig.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font=dict(size=16),
    legend=dict(title='', orientation='h', yanchor='bottom', y=1.02, xanchor='center', x=0.5),
    bargap=0.35,
    xaxis=dict(
        tickfont=dict(size=10, color='#222', family='Arial Black'),
        title_font=dict(size=17, color='#111', family='Arial Black'),
        tickangle=0,
        showline=True,
        linewidth=2,
        linecolor='#222',
        mirror=True
    ),
    yaxis=dict(
        tickfont=dict(size=10, color='#222', family='Arial Black'),
        title_font=dict(size=17, color='#111', family='Arial Black'),
        showline=True,
        linewidth=2,
        linecolor='#222',
        mirror=True,
        gridcolor='#bbb',
        gridwidth=1
    )
)

st.plotly_chart(fig, use_container_width=True)
st.markdown("</div>", unsafe_allow_html=True)

# ---------------- STREAMLIT PROJECT LINKS ----------------
st.header("🔗 Online Demo Projects")
st.markdown(
    """
- [Data Analysis Tool](https://genai-data-analysis-test.streamlit.app//) – A Streamlit app performing data analysis on csv data.
- [Exploratory Data Analysis](https://eda-healthcare-mohk.streamlit.app//) –  A Streamit app to perform exploratory data analysis.
- [Classification Model - Iris data ](https://iris-ml-system-profile-1.streamlit.app//) – A Streamlit app that perform the classification on the Iris dataset.

**R Programming - Old codes**
- [Bike Sharing Assignment](https://rpubs.com/abdul_yunus/Bike_Renting_Assignment) - Analyzing bike sharing data using R.
- [Clustering ](https://rpubs.com/abdul_yunus/Kmeans_Clustering) - Clustering analysis using K-means algorithm.
"""
)

# ---------------- EDUCATION ----------------
st.header("🎓 Education")
st.markdown(
    """
- **MBA (Marketing)** – North Maharashtra University
- **M.Sc. Physics (Material Science)** – SRTM University, Nanded
- **B.Sc. Mathematics** – Amravati University
"""
)

# ---------------- CERTIFICATIONS ----------------
st.header("📜 Certifications")
st.markdown(
    """
- **Machine Learning** – Cornell University (Issued April 2023)
- **Gen AI workshop** – Indian Institute of Technology, Hyderabad (Issued April 2025)
"""
)

# ---------------- FOOTER ----------------
st.divider()
st.caption("📊 Built with Streamlit | Data Science Portfolio CV")











