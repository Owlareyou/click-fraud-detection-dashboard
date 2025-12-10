"""
Data loading and processing utilities for the Click Fraud Detection dashboard.
This module contains shared functions used across all pages.
"""

import pandas as pd
import streamlit as st


@st.cache_data
def load_data(sample_size=None):
    """
    Load and prepare the dataset with optional sampling.
    
    Args:
        sample_size (int, optional): Number of records to sample. If None, loads full dataset.
        
    Returns:
        pd.DataFrame: Processed dataframe with temporal features
    """
    # Load data
    df = pd.read_csv('data/train_sample.csv')  # Note: Full training data is 7GB, using sample
    
    # Convert click_time to datetime
    df['click_time'] = pd.to_datetime(df['click_time'])
    df['attributed_time'] = pd.to_datetime(df['attributed_time'])
    
    # Extract temporal features
    df['hour'] = df['click_time'].dt.hour
    df['day'] = df['click_time'].dt.day
    df['dayofweek'] = df['click_time'].dt.dayofweek
    df['date'] = df['click_time'].dt.date
    
    # Apply sampling if requested
    if sample_size and sample_size < len(df):
        df = df.sample(n=sample_size, random_state=42)
    
    return df


def get_viz_sample(df, max_size=5000):
    """
    Return a sample for visualization if dataset is too large.
    
    Args:
        df (pd.DataFrame): Input dataframe
        max_size (int): Maximum size for visualization
        
    Returns:
        pd.DataFrame: Sampled dataframe if needed, otherwise original
    """
    if len(df) > max_size:
        return df.sample(n=max_size, random_state=42)
    return df


def get_data_with_sidebar_controls():
    """
    Create sidebar controls for data sampling and return the loaded data.
    This function should be called at the top of each page.
    
    Returns:
        pd.DataFrame: Loaded and potentially sampled dataframe
    """
    # st.sidebar.markdown("---")
    st.sidebar.markdown("### Data Settings")
    st.sidebar.markdown("*Full dataset: ~7GB, using sample*")
    
    use_sample = st.sidebar.checkbox(
        "Use sample data", 
        value=True, 
        help="Recommended for faster performance"
    )
    
    if use_sample:
        sample_size = st.sidebar.slider(
            "Sample size", 
            min_value=1000, 
            max_value=100000, 
            value=10000, 
            step=1000,
            help="Smaller = faster, larger = more comprehensive"
        )
        df = load_data(sample_size)
        st.sidebar.info(f"📊 Using {len(df):,} records")
    else:
        df = load_data()
        st.sidebar.info(f"📊 Using full dataset: {len(df):,} records")
    
    st.sidebar.markdown("---")
    
    return df