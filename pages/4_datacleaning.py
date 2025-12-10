"""
Data Cleaning & Feature Engineering Page
"""

import streamlit as st
import sys
sys.path.append('..')

from config import CUSTOM_CSS
from utils.data_loader import get_data_with_sidebar_controls

# Apply custom CSS
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# Load data with sidebar controls
df = get_data_with_sidebar_controls()

# Page header
st.markdown('<div class="main-header">🧹 Data Cleaning & Feature Engineering</div>', unsafe_allow_html=True)

st.markdown("---")

st.markdown("""
This section covers data quality checks and feature engineering steps to prepare the dataset for modeling.
Feature engineering is critical for improving model performance, especially with weak individual feature correlations.
""")

st.markdown("---")

# Data Cleaning Section
st.markdown("### 🔍 Data Quality Assessment")
st.markdown("[Your detailed data cleaning process here]")

with st.expander("Missing Values Analysis"):
    st.markdown("[Your missing values analysis here]")
    # st.image('image/image_1.png', use_column_width=True)  # TODO: Replace 'image_1.png' with 'missing_values_analysis.png'

with st.expander("Duplicate Detection"):
    st.markdown("[Your duplicate detection analysis here]")
    # st.image('image/image_1.png', use_column_width=True)  # TODO: Replace 'image_1.png' with 'duplicate_detection.png'

with st.expander("Outlier Detection"):
    st.markdown("[Your outlier detection analysis here]")
    # st.image('image/image_1.png', use_column_width=True)  # TODO: Replace 'image_1.png' with 'outlier_detection.png'

st.markdown("---")

# Feature Engineering Section
st.markdown("### 🔧 Feature Engineering")
st.markdown("[Your feature engineering overview here]")

with st.expander("Temporal Features"):
    st.markdown("""
    **Created Features:**
    - hour, day, dayofweek
    - is_weekend
    - time_of_day (morning/afternoon/evening/night)
    
    [Your detailed temporal feature engineering here]
    """)
    # st.image('image/image_1.png', use_column_width=True)  # TODO: Replace 'image_1.png' with 'temporal_features.png'

with st.expander("Aggregation Features"):
    st.markdown("""
    **Created Features:**
    - ip_count, app_count, device_count, channel_count
    - ip_app_count (interaction feature)
    
    [Your detailed aggregation feature engineering here]
    """)
    # st.image('image/image_1.png', use_column_width=True)  # TODO: Replace 'image_1.png' with 'aggregation_features.png'

with st.expander("Time-Series Features"):
    st.markdown("""
    **Created Features:**
    - Lag features (previous values)
    - Rolling averages (moving windows)
    - Time differences
    
    [Your detailed time-series feature engineering here]
    """)
    # st.image('image/image_1.png', use_column_width=True)  # TODO: Replace 'image_1.png' with 'timeseries_features.png'

st.markdown("---")

# Train/Val/Test Split
st.markdown("### ✂️ Train/Validation/Test Split")
st.markdown("""
[Your train/validation/test split strategy here]

**Split Strategy:** Temporal split to prevent data leakage
- Training: 60%
- Validation: 20%
- Test: 20%
""")
# st.image('image/image_1.png', use_column_width=True)  # TODO: Replace 'image_1.png' with 'train_test_split.png'

st.markdown("---")

# Footer
st.markdown("""
<div style='text-align: center; color: #7f8c8d; padding: 1rem 0;'>
    <p>🧹 Data Cleaning | Click Fraud Detection Analysis</p>
</div>
""", unsafe_allow_html=True)