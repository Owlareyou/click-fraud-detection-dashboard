"""
References Page - Citations and Resources
"""

import streamlit as st
import sys
sys.path.append('..')

from config import CUSTOM_CSS

# Apply custom CSS
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# Page header
st.markdown('<div class="main-header">References</div>', unsafe_allow_html=True)

st.markdown("---")

st.markdown("### References")
st.markdown("""
[1] A. Ravaglia, "Imbalanced classification in Fraud Detection," *Data Reply IT | DataTech*, May 31, 2022. https://medium.com/data-reply-it-datatech/imbalanced-classification-in-fraud-detection-8f63474ff8c7

[2] "Click Fraud Statistics 2026: Global Costs & Key Trends," *Trafficguard.ai*, 2025. https://www.trafficguard.ai/click-fraud-statistics (accessed Dec. 10, 2025).

[3] M. Aljabri and R. M. A. Mohammad, "Click fraud detection for online advertising using machine learning," *Egyptian Informatics Journal*, vol. 24, no. 2, pp. 341–350, Jul. 2023, doi: https://doi.org/10.1016/j.eij.2023.05.006.

[4] "TalkingData AdTracking Fraud Detection Challenge," *@kaggle*, 2025. https://www.kaggle.com/competitions/talkingdata-adtracking-fraud-detection/overview (accessed Dec. 10, 2025).
""")

st.markdown("---")

st.markdown("### Tools & Libraries")
st.markdown("""
- Python 3.x
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Streamlit
- XGBoost
- LightGBM
- scikit-learn
""")

st.markdown("---")

# Footer
st.markdown("""
<div style='text-align: center; color: #7f8c8d; padding: 1rem 0;'>
    <p>References | Click Fraud Detection Analysis</p>
</div>
""", unsafe_allow_html=True)