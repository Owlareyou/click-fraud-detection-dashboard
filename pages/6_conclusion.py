"""
Conclusion Page - Key Findings and Insights
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
st.markdown('<div class="main-header">Conclusion & Insights</div>', unsafe_allow_html=True)

st.markdown("---")

st.markdown("## Observation and Conclusion")

st.markdown("""
Linear models, even with balanced class weights and engineered features, cannot capture the nonlinear 
and interaction-heavy patterns associated with fraudulent click behavior. In contrast, tree-based models, 
especially XGBoost, successfully leverage count-based and temporal signals to achieve significant 
improvements in PR–AUC, the metric most aligned with rare-event prediction.

The engineered features significantly enhance model performance by encoding click frequency patterns 
and inter-click timing, both of which correlate strongly with automated or deceptive activity. XGBoost 
with imbalance-aware weighting provides the best trade-off between precision and recall when tested on 
the true distribution, whereas undersampling shifts the model toward aggressive recall at the cost of 
many false alarms.

Overall, our results indicate that combining feature engineering with gradient-boosted tree models is 
an effective strategy for highly imbalanced fraud detection. Future work may explore alternative 
imbalance strategies (e.g., SMOTE), sequential models that analyze click order, or anomaly detection 
methods to further reduce false positives.
""")

st.markdown("---")

# Footer
st.markdown("""
<div style='text-align: center; color: #7f8c8d; padding: 1rem 0;'>
    <p>Conclusion | Click Fraud Detection Analysis</p>
</div>
""", unsafe_allow_html=True)