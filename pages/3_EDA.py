"""
EDA Page - Exploratory Data Analysis with sub-tabs
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import sys
sys.path.append('..')

from config import CUSTOM_CSS
from utils.data_loader import get_data_with_sidebar_controls, get_viz_sample

# Apply custom CSS
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# Load data with sidebar controls
df = get_data_with_sidebar_controls()

# Page header
st.markdown('<div class="main-header">📊 Exploratory Data Analysis</div>', unsafe_allow_html=True)

################################################################################
view_mode = st.radio(
    "Select View Mode:",
    ["Full Analysis (Static)", "Interactive Analysis (Live Data)"],
    horizontal=True
)
st.markdown("---")
################################################################################

if view_mode == "Full Analysis (Static)":
    st.markdown("## Complete EDA Results")
    
    # Target Distribution
    st.markdown("### 1. Target Variable Distribution")


    col1, col2 = st.columns([3, 1])
    with col1:
        st.image('outputs/01_target_distribution.png', use_container_width=True)
    with col2:
        st.markdown("**Key Findings:**")
        st.markdown("- 99.77% no download")
        st.markdown("- 0.23% download")
        st.markdown("- Severe imbalance")
    st.markdown("""
    The first step of data exploration is understanding the distribution of the target variable, 
    is_attributed, which indicates whether a user downloaded the app after clicking the 
    advertisement (1 = download, 0 = no download).
    
    - The dataset is extremely dominated by negative cases
    - Out of 100,000 click events in train_sample.csv:
        - 99,773, around 99.77% did not lead to an app download
        - Only 227, around 0.23% resulted in a download. This means fewer than 3 downloads per 1,000 clicks.
    """)


    st.divider()
    
    # Numerical Features
    st.markdown("### 2. Univariate Analysis — Numerical Features")
    
    tabs = st.tabs(["IP", "App", "Device", "OS"])  
    with tabs[0]:
        col1, col2 = st.columns([2, 2])
        with col1:
            st.image('outputs/02_ip.png', use_container_width=True)
            st.caption("Right-skewed distribution, most IPs < 150,000")
        with col2:
            st.markdown("**Observations:**")
            st.markdown("""
            * The distribution of ip is highly right-skewed. 
            * Most IPs fall under 150,000, and the histogram shows dense concentration in the lower to mid ranges. A long tail extends up to 350,000+, with relatively few occurrences in the higher range.
            """)
    
    with tabs[1]:
        col1, col2 = st.columns([2, 2])
        with col1:
            st.image('outputs/02_app.png', use_container_width=True)
            st.caption("Value cluster's under 40")
        with col2:
            st.markdown("**Observations:**")
            st.markdown("""
            * The app feature is extremely concentrated around a small set of app IDs.
            * The mean and median are both 12, and most values cluster tightly under 40.
            * A few outlier app IDs appear above 100–500 but occur rarely.
            """)
    
    with tabs[2]:
        col1, col2 = st.columns([2, 2])
        with col1:
            st.image('outputs/02_device.png', use_container_width=True)
            st.caption("Extreme skewed distribution with a few outliers")
        with col2:
            st.markdown("**Observations:**")
            st.markdown("""
            * The device distribution is extremely skewed
            * Nearly all rows have device ID = 1. 
            * A few outlier device IDs (hundreds or thousands) appear with extremely low frequency.
            """)

    with tabs[3]:
        col1, col2 = st.columns([2, 2])
        with col1:
            st.image('outputs/02_os.png', use_container_width=True)
            st.caption("Similar to Deivice's Distribution")
        with col2:
            st.markdown("**Observations:**")
            st.markdown("""
            * The distribution of OS is similar to device: very concentrated in the low-value OS versions (0–30). 
            * A few large OS values (200–700 range) appear rarely and create a long tail.
            """)
    
    st.markdown("**Variable Boxplot**")
    st.image('outputs/03_boxplots_outliers.png', use_container_width=True)

    #Temporal Analsyis
    st.markdown("### 3. Temporal Analysis")
    
    tabs = st.tabs(["Clicks by Hour of Day", "Clicks by Date", "Clicks by Day of Week", "Attribution Rate by Hour"]) 
    with tabs[0]:
        st.image('outputs/04_byhourofday.png', use_container_width=True)
        st.caption("")
        st.markdown("""
        **Observation:**
        * Click activity remains high and stable from 0:00 to around 15:00, with counts between ~4,500 and 6,000 clicks per hour. 
        * After 16:00, there is a sharp decline—clicks drop dramatically from ~3,800 to fewer than 1,000 between 17:00–22:00. 
        * Activity rises again slightly at 23:00.

        """)
    with tabs[1]:
        st.image('outputs/04_bydate.png', use_container_width=True)
        st.caption("")
        st.markdown("""
        **Observation:**
        * Traffic increases from Nov 6 → Nov 7 → Nov 8, then slightly decreases on Nov 9.
        * The highest click volume occurs on Nov 8, with over 34,000 clicks.
        * A strong upward trend may indicate: 
            * A new campaign launch
            * ncreased ad exposure from publishers
            * Or possibly a surge in automated traffic.

        """)
    with tabs[2]:
        st.image('outputs/04_bydayofweek.png', use_container_width=True)
        st.caption("")
        st.markdown("""
        **Observation:**
        * Most clicks come from Tuesday, Wednesday, and Thursday. 
        * Monday has significantly fewer clicks- less than 5000 , mostly because the dataset begins late on Monday. 
        * Friday–Sunday have no data in this sample.

        """)
    with tabs[3]:
        st.image('outputs/04_byhour.png', use_container_width=True)
        st.caption("")
        st.markdown("""
        **Observation:**
        * Attribution rate fluctuates between 0.15% and 0.34% across hours.
        * Conversion rate stays relatively stable during the high-click hours.
        * There is a noticeable drop in conversions around 17–20, which aligns with the drop in total clicks.
        * A small spike occurs again around 21–23.
        """)


################################################################################
else:

    # Sub-tabs
    eda_tab1, eda_tab2, eda_tab3, eda_tab4 = st.tabs([
        "Target Analysis",
        "Categorical Features",
        "Temporal Patterns",
        "Correlations & Relationships"
    ])

    # ========== SUB-TAB 1: TARGET ANALYSIS ==========
    with eda_tab1:
        st.markdown("### Target Variable Distribution")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            # Pie chart
            fraud_counts = df['is_attributed'].value_counts()
            fig = px.pie(
                values=fraud_counts.values,
                names=['Legitimate (0)', 'Fraud (1)'],
                title='Click Attribution Distribution',
                color_discrete_sequence=['#2ecc71', '#e74c3c']
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Statistics table
            fraud_stats = pd.DataFrame({
                'Category': ['Legitimate Clicks', 'Fraudulent Clicks', 'Total Clicks'],
                'Count': [
                    fraud_counts[0],
                    fraud_counts[1],
                    len(df)
                ],
                'Percentage': [
                    f"{(fraud_counts[0]/len(df))*100:.2f}%",
                    f"{(fraud_counts[1]/len(df))*100:.2f}%",
                    "100.00%"
                ]
            })
            st.table(fraud_stats)
        
        st.info(f"""
        **Key Insight:** Severe class imbalance detected with only {fraud_counts[1]} fraud cases 
        ({df['is_attributed'].mean()*100:.3f}%) out of {len(df):,} total records. This will require 
        specialized techniques like SMOTE, class weighting, or adjusted evaluation metrics.
        """)

    # ========== SUB-TAB 2: CATEGORICAL FEATURES ==========
    with eda_tab2:
        st.markdown("### Categorical Feature Distributions")
        
        categorical_features = ['app', 'device', 'os', 'channel']
        
        for feature in categorical_features:
            st.markdown(f"#### {feature.upper()} Distribution")
            
            col1, col2 = st.columns([3, 1])
            
            with col1:
                # Top 20 values bar chart
                top_values = df[feature].value_counts().head(20)
                
                fig = px.bar(
                    x=top_values.index.astype(str),
                    y=top_values.values,
                    labels={'x': f'{feature.upper()} ID', 'y': 'Frequency'},
                    title=f'Top 20 {feature.upper()} IDs by Click Frequency',
                    color=top_values.values,
                    color_continuous_scale='Blues'
                )
                fig.update_layout(showlegend=False)
                st.plotly_chart(fig, use_container_width=True)
            
            with col2:
                # Statistics
                stats_df = pd.DataFrame({
                    'Metric': ['Unique Values', 'Most Common ID', 'Most Common Count', 'Concentration %'],
                    'Value': [
                        df[feature].nunique(),
                        df[feature].value_counts().index[0],
                        df[feature].value_counts().values[0],
                        f"{(df[feature].value_counts().values[0]/len(df))*100:.2f}%"
                    ]
                })
                st.table(stats_df)
                
                # Top 10 concentration
                top10_conc = df[feature].value_counts().head(10).sum() / len(df) * 100
                st.metric("Top 10 Concentration", f"{top10_conc:.1f}%")
            
            st.markdown("---")
        
        # Box plots
        st.markdown("#### Distribution Comparison - Box Plots")
        
        fig = go.Figure()
        for feature in ['app', 'device', 'os', 'channel']:
            fig.add_trace(go.Box(y=df[feature], name=feature.upper()))
        fig.update_layout(title='APP, DEVICE, OS, CHANNEL Distribution', yaxis_title='Value')
        st.plotly_chart(fig, use_container_width=True)

        # col1, col2 = st.columns(2)
        
        # with col1:
        #     fig = go.Figure()
        #     for feature in ['app', 'device']:
        #         fig.add_trace(go.Box(y=df[feature], name=feature.upper()))
        #     fig.update_layout(title='APP and DEVICE Distribution', yaxis_title='Value')
        #     st.plotly_chart(fig, use_container_width=True)
        
        # with col2:
        #     fig = go.Figure()
        #     for feature in ['os', 'channel']:
        #         fig.add_trace(go.Box(y=df[feature], name=feature.upper()))
        #     fig.update_layout(title='OS and CHANNEL Distribution', yaxis_title='Value')
        #     st.plotly_chart(fig, use_container_width=True)

    # ========== SUB-TAB 3: TEMPORAL PATTERNS ==========
    with eda_tab3:
        st.markdown("### Temporal Analysis")
        
        # Hourly patterns
        st.markdown("#### Click Distribution by Hour of Day")
        col1, col2 = st.columns(2)
        
        with col1:
            hourly_clicks = df.groupby('hour').size()
            fig = px.line(
                x=hourly_clicks.index,
                y=hourly_clicks.values,
                labels={'x': 'Hour of Day', 'y': 'Number of Clicks'},
                title='Total Clicks by Hour',
                markers=True
            )
            fig.update_traces(line_color='#1f77b4', line_width=3)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            hourly_fraud = df.groupby('hour')['is_attributed'].mean() * 100
            fig = px.line(
                x=hourly_fraud.index,
                y=hourly_fraud.values,
                labels={'x': 'Hour of Day', 'y': 'Fraud Rate (%)'},
                title='Fraud Rate by Hour',
                markers=True
            )
            fig.update_traces(line_color='#e74c3c', line_width=3)
            st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("---")
        
        # Daily patterns
        st.markdown("#### Click Distribution by Day of Month")
        col1, col2 = st.columns(2)
        
        with col1:
            daily_clicks = df.groupby('day').size()
            fig = px.bar(
                x=daily_clicks.index,
                y=daily_clicks.values,
                labels={'x': 'Day of Month', 'y': 'Number of Clicks'},
                title='Total Clicks by Day',
                color=daily_clicks.values,
                color_continuous_scale='Viridis'
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            daily_fraud = df.groupby('day')['is_attributed'].mean() * 100
            fig = px.bar(
                x=daily_fraud.index,
                y=daily_fraud.values,
                labels={'x': 'Day of Month', 'y': 'Fraud Rate (%)'},
                title='Fraud Rate by Day',
                color=daily_fraud.values,
                color_continuous_scale='Reds'
            )
            st.plotly_chart(fig, use_container_width=True)
        
        st.info("""
        **Temporal Insight:** Clear patterns in click timing suggest different behavior between 
        legitimate users and fraudulent activity. Temporal features will be valuable for modeling.
        """)

    # ========== SUB-TAB 4: CORRELATIONS ==========
    with eda_tab4:
        st.markdown("### Feature Correlations & Relationships")
        
        # Correlation heatmap
        st.markdown("#### Correlation Matrix")
        numeric_features = ['ip', 'app', 'device', 'os', 'channel', 'hour', 'day', 'is_attributed']
        correlation_matrix = df[numeric_features].corr()
        
        fig = px.imshow(
            correlation_matrix,
            labels=dict(x="Features", y="Features", color="Correlation"),
            x=numeric_features,
            y=numeric_features,
            color_continuous_scale='RdBu_r',
            aspect="auto",
            title='Feature Correlation Heatmap'
        )
        fig.update_layout(height=600)
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("---")
        
        # Fraud rate by categorical features
        st.markdown("#### Fraud Rate by Feature")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # App vs fraud
            app_fraud = df.groupby('app')['is_attributed'].agg(['mean', 'count']).reset_index()
            app_fraud = app_fraud[app_fraud['count'] >= 10].sort_values('mean', ascending=False).head(15)
            
            fig = px.bar(
                app_fraud,
                x='app',
                y='mean',
                labels={'app': 'App ID', 'mean': 'Fraud Rate'},
                title='Fraud Rate by App (min 10 clicks)',
                color='mean',
                color_continuous_scale='Reds'
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Channel vs fraud
            channel_fraud = df.groupby('channel')['is_attributed'].agg(['mean', 'count']).reset_index()
            channel_fraud = channel_fraud[channel_fraud['count'] >= 10].sort_values('mean', ascending=False).head(15)
            
            fig = px.bar(
                channel_fraud,
                x='channel',
                y='mean',
                labels={'channel': 'Channel ID', 'mean': 'Fraud Rate'},
                title='Fraud Rate by Channel (min 10 clicks)',
                color='mean',
                color_continuous_scale='Oranges'
            )
            st.plotly_chart(fig, use_container_width=True)
        
        st.info("""
        **Correlation Insight:** Weak individual correlations suggest that fraud detection will 
        require feature engineering and interaction effects rather than relying on single features.
        """)

    st.markdown("---")

    # Footer
    st.markdown("""
    <div style='text-align: center; color: #7f8c8d; padding: 1rem 0;'>
        <p>EDA | Click Fraud Detection Analysis</p>
    </div>
    """, unsafe_allow_html=True)