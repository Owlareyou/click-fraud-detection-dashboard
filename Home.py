"""
Click Fraud Detection Analysis Dashboard
Main entry point for the multi-page Streamlit application.

Team: Ching Chuang, Yu-Chieh Chen, Jia-Ning Hu
"""

import streamlit as st
from config import PAGE_CONFIG, CUSTOM_CSS, PROJECT_TITLE, TEAM_STRING
from utils.data_loader import get_data_with_sidebar_controls

# MUST be the first Streamlit command
st.set_page_config(**PAGE_CONFIG)

# Apply custom CSS
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# ===== DEFINE HOME PAGE CONTENT AS A FUNCTION =====
def home_page():
    # Main page content
    st.markdown(f'<div class="main-header">{PROJECT_TITLE}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="team-info">{TEAM_STRING}</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Load data with sidebar controls
    df = get_data_with_sidebar_controls()
    
    # Header image placeholder
    # st.image('image/image_1.png', use_column_width=True)  # TODO: Replace 'image_1.png' with actual header/banner image filename
    
    # Brief Introduction
    st.markdown("""
    ## Project Overview
    
    We want to examine the challenge of click fraud in mobile app advertising using TalkingData's extensive ad tracking dataset. We will analyze click patterns, user behavior, and device characteristics to identify fraudulent ad traffic that generates clicks without genuine user interest. The most important part of this analysis will be assessing how temporal patterns, channel characteristics, and user engagement metrics distinguish legitimate app downloads from fraudulent clicks. This in return could also reveal which advertising channels and user segments are most vulnerable to fraud. Combining this with feature engineering and machine learning models, we can develop predictive tools to protect advertisers from wasted ad spend and improve the integrity of mobile advertising ecosystems.
    """)
        
    # Expandable detailed background
    with st.expander("Detailed Project Background", expanded=False):
        st.markdown("""
    ### Problem Definition
    
    Mobile app advertisers lose billions of dollars annually to click fraud, where bots or malicious actors generate fake ad clicks that never result in actual app downloads. TalkingData, processes 3 billion clicks per day, with approximately 90% potentially fraudulent. Current fraud detection methods rely primarily on IP blacklists, but fraudsters continuously evolve their tactics.
    
    ### Prediction Task
                
    Given a mobile ad click event with associated features (IP address, device, OS, channel, timestamp), predict whether the user will download the app or if the click is fraudulent.
    
    An accurate fraud detection enables advertisers to optimize ad spend by blocking fraudulent traffic sources in real-time, improving return on investment and allowing legitimate publishers to demonstrate their value. For TalkingData's clients, even a 1 percent improvement in fraud detection accuracy could save millions in wasted advertising expenditure.

    ### Related Work
    
    Click fraud detection relies heavily on machine learning due to its significant financial impact on advertisers. The challenge lies in the imbalanced nature of fraud datasets, where fraudulent clicks typically represent less than 1 percent of total traffic [1]. Balancing techniques like SMOTE and ADASYN can substantially improve model performance, particularly in increasing recall rates [1]. Tree-based ensemble methods such as Random Forest and XGBoost consistently outperform other approaches, achieving high precision and recall even with highly imbalanced datasets [1][3]. These models are preferred over neural networks because they provide interpretable decision rules critical for legal and regulatory compliance [1]. Behavioral features—including browsing session duration, pages viewed, and click patterns—serve as strong indicators distinguishing bot activity from legitimate user behavior [3]. The global cost remains substantial, with North America losing \$180,000 per minute and Asia Pacific \$147,000 per minute to fraudulent ad spending [2], underscoring the urgent need for effective automated detection systems.            

        """)
    
    st.markdown("---")
    
    # Quick statistics
    st.markdown("### Dataset Quick Stats")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Current Sample Size", f"{len(df):,}")
    
    with col2:
        st.metric("Total Features", len(df.columns))
    
    with col3:
        fraud_rate = df['is_attributed'].mean() * 100
        st.metric("Fraud Rate", f"{fraud_rate:.3f}%")
    
    with col4:
        date_span = (df['click_time'].max() - df['click_time'].min()).days
        st.metric("Date Range", f"{date_span} days")
    
    st.info("""
    Note: These statistics are based on your current sample size. 
    Adjust the sample size in the sidebar to explore different data subsets.
    """)
    
    st.markdown("---")
    
    # Footer
    st.markdown("""
    <div style='text-align: center; color: #7f8c8d; padding: 1rem 0;'>
        <p>Click Fraud Detection Analysis | USC Applied Data Science</p>
    </div>
    """, unsafe_allow_html=True)

# ===== NAVIGATION SECTION =====
home = st.Page(home_page, title="Project Overview", default=True)
dataset = st.Page("pages/2_datasetdetails.py", title="Dataset Details")
eda = st.Page("pages/3_EDA.py", title="Exploratory Analysis")
# cleaning = st.Page("pages/4_datacleaning.py", title="Data Cleaning")
modeling = st.Page("pages/5_modeling.py", title="Modeling")
conclusion = st.Page("pages/6_conclusion.py", title="Conclusions")
references = st.Page("pages/7_references.py", title="References")

pg = st.navigation([home, dataset, eda, modeling, conclusion, references])
pg.run()