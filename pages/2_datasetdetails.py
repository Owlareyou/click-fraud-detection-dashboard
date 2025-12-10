"""
Dataset Details Page - Comprehensive data documentation
"""

import streamlit as st
import pandas as pd
import sys
sys.path.append('..')

from config import CUSTOM_CSS
from utils.data_loader import get_data_with_sidebar_controls

# Apply custom CSS
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# Load data with sidebar controls
df = get_data_with_sidebar_controls()

# Page header
st.markdown('<div class="main-header">Dataset Details</div>', unsafe_allow_html=True)

st.markdown("---")

# Overview Section
st.markdown("### Dataset Overview")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Records", f"{len(df):,}")
with col2:
    st.metric("Features", len(df.columns))
with col3:
    st.metric("Fraud Rate", f"{df['is_attributed'].mean()*100:.3f}%")
with col4:
    st.metric("Date Range", f"{(df['click_time'].max() - df['click_time'].min()).days} days")

st.markdown("---")

# Data Dictionary
st.markdown("### Data Dictionary")

schema_data = {
    "Feature": ["ip", "app", "device", "os", "channel", "click_time", "attributed_time", "is_attributed"],
    "Type": ["int", "int", "int", "int", "int", "datetime", "datetime", "int"],
    "Description": [
        "IP address ID of the click",
        "Application ID for marketing",
        "Device type ID of user mobile phone",
        "Operating system version ID of user mobile phone",
        "Channel ID of mobile ad publisher",
        "Timestamp of click (UTC)",
        "Timestamp of app download (if attributed)",
        "Target variable: 1 = app download attributed, 0 = not attributed"
    ]
}
st.table(pd.DataFrame(schema_data))

st.markdown("---")

# Dataset Source
st.markdown("### Dataset Information")
st.markdown(f"""
- **Source:** TalkingData Click Fraud Detection Dataset
- **Size:** ~{len(df):,} records (sample)
- **Period:** {df['click_time'].min().date()} to {df['click_time'].max().date()}
- **Format:** CSV
- **Features:** 8 columns (6 categorical IDs, 2 datetime, 1 binary target)
- **Full Dataset:** ~7GB (184+ million records)
""")

st.markdown("---")

# Quick Stats
st.markdown("### Quick Statistics")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Categorical Features:**")
    stats_data = []
    for col in ['ip', 'app', 'device', 'os', 'channel']:
        stats_data.append({
            'Feature': col.upper(),
            'Unique Values': df[col].nunique(),
            'Most Common': df[col].value_counts().index[0],
            'Most Common Count': df[col].value_counts().values[0]
        })
    st.dataframe(pd.DataFrame(stats_data), use_container_width=True)

with col2:
    st.markdown("**Missing Values:**")
    missing_data = pd.DataFrame({
        'Feature': df.columns,
        'Missing Count': df.isnull().sum(),
        'Missing %': (df.isnull().sum() / len(df) * 100).round(2)
    })
    st.dataframe(missing_data, use_container_width=True)

st.markdown("---")

# Sample Data
st.markdown("### Sample Data Preview")
st.dataframe(df.head(20), use_container_width=True)

st.markdown("---")

# Footer
st.markdown("""
<div style='text-align: center; color: #7f8c8d; padding: 1rem 0;'>
    <p>Dataset Details | Click Fraud Detection Analysis</p>
</div>
""", unsafe_allow_html=True)