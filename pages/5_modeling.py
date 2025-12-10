"""
Modeling & Results Page
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
st.markdown('<div class="main-header">Modeling & Results</div>', unsafe_allow_html=True)

st.markdown("---")

st.markdown("""
This section presents the modeling approaches and experimental results for click fraud detection.
Multiple models are evaluated to identify the best performing approach for this highly imbalanced dataset.
""")

st.markdown("---")

# ========== METHODOLOGY ==========
st.markdown("## Methodology")

# Data Cleaning
st.markdown("### 1.1 Data Cleaning and Preprocessing")
st.markdown("""
We remove the single duplicate row detected in the data and ensure that `click_time` is parsed into a proper 
datetime object. No missing values are present in any column. The feature `attributed_time` is excluded because 
it is only available for positive cases, which would cause data leakage if used as a predictor.

Since the original features (`ip`, `app`, `device`, `os`, `channel`) are categorical ID-like integers, they are 
stored in numeric form without one-hot encoding. For logistic regression models, these features are standardized 
using a `ColumnTransformer`. For tree-based models, preprocessing simply passes the numeric features through, 
as boosting and bagging methods naturally handle unscaled integer inputs.

The target variable `is_attributed` is extremely imbalanced (0.23% positives), so class weights are computed 
during training. For logistic regression, we use `class_weight="balanced"`; for XGBoost, we compute 
`scale_pos_weight = (negatives/positives) ≈ 438.55` based on the training split.
""")

st.markdown("---")

# Feature Engineering
st.markdown("### 1.2 Feature Engineering")
st.markdown("""
To enrich the raw identifiers with temporal and behavioral information, we construct two categories of 
engineered features.

**Time-based features:**
- Extract `hour`, `day`, and `weekday` from `click_time`, reflecting that user click behaviors vary across 
  the day and week
- Compute a temporal gap feature, `next_click`, which measures the number of seconds until the next click 
  from the same IP after sorting each IP's history
- Short intervals often indicate automated activity
- Missing intervals (final click per IP) are filled with 24 hours (86,400 seconds)

**Count-based behavior features:**
- Compute high-frequency interaction statistics:
  - `ip_count` (total clicks per IP)
  - `ip_app_count` (clicks per IP and app)
  - `ip_app_os_count` (clicks per IP, app, and OS)
- These features capture repeated or unusually frequent click patterns, which can be used as indicators 
  of fraudulent behavior

We prepared two final feature sets for our experiments:
- **RAW_FEATURES:** Contains only the five original features
- **FE_FEATURES:** Contains all original fields plus the engineered time, count, and `next_click` features
""")

st.markdown("---")

# Modeling Methods
st.markdown("### 1.3 Modeling Methods")
st.markdown("""
We evaluate a sequence of models that gradually increase in representational complexity and incorporate 
different strategies for addressing class imbalance:

1. **Baseline Logistic Regression:** Trained on raw features, using feature scaling and class weighting 
   to compensate for severe imbalance

2. **Logistic Regression with Feature Engineering:** Uses the full set of engineered features with 
   standardization through a `ColumnTransformer`

3. **Random Forest Classifier:** Captures nonlinear relationships and interactions among engineered 
   variables with class weighting

4. **XGBoost:** Gradient-boosted tree ensemble using histogram-based splits, with `scale_pos_weight` 
   equal to the ratio of negative to positive samples, configured with 400 estimators and maximum depth of 6

5. **XGBoost with Undersampling:** Trained on undersampled dataset (1:5 ratio, 182 positives and 910 negatives) 
   with `scale_pos_weight=1`, evaluated on original imbalanced test set
""")

with st.expander("View Code Snippet: XGBoost Configuration"):
    st.code("""
# XGBoost with Imbalance Weighting
from xgboost import XGBClassifier

model = XGBClassifier(
    n_estimators=400,
    max_depth=6,
    scale_pos_weight=438.55,  # Ratio of negatives to positives
    random_state=42
)
model.fit(X_train, y_train)
    """, language='python')

st.markdown("---")

# ========== EXPERIMENTAL RESULTS ==========
st.markdown("## Experimental Results")

st.markdown("""
The data is split into 80% training and 20% testing sets with stratification, resulting in 182 positives 
in the training set and 45 in the testing set. Each model is evaluated using predicted probabilities to 
compute ROC-AUC and PR-AUC, and classification metrics are additionally reported at a threshold of 0.5.
""")

st.markdown("---")

# Results Table
st.markdown("### Model Performance Comparison")

results_data = {
    "Model": [
        "Logistic Regression (Raw)",
        "Logistic Regression (FE)",
        "Random Forest (FE)",
        "XGBoost (FE)",
        "XGBoost (Undersampled)"
    ],
    "ROC-AUC": [0.8486, 0.8810, 0.9157, 0.9353, 0.9382],
    "PR-AUC": [0.0213, 0.0232, 0.3682, 0.3639, 0.2764],
    "Precision": ["-", "-", "-", 0.4231, 0.1057],
    "Recall": ["-", "-", "-", 0.4889, 0.8222]
}

import pandas as pd
st.dataframe(pd.DataFrame(results_data), use_container_width=True)

st.markdown("---")

# Analysis
st.markdown("### Analysis of Results")

st.markdown("""
**Baseline Models:**
- The baseline logistic regression performs poorly, with ROC-AUC of 0.8486 and PR-AUC of only 0.0213
- This suggests the model struggles to accurately identify rare fraud cases
- Adding feature engineering improves ROC-AUC to 0.8810 and PR-AUC to 0.0232, but remains inadequate 
  for separating the positive class

**Tree-Based Methods:**
- Tree-based methods show substantial gains
- Random Forest achieves ROC-AUC of 0.9157 and PR-AUC of 0.3682
- **XGBoost obtains the strongest overall performance** with ROC-AUC of 0.9353 and PR-AUC of 0.3639
- XGBoost achieves balanced threshold-level precision (0.4231) and recall (0.4889), indicating effective 
  ranking and moderately effective detection

**Undersampling Approach:**
- Produces a different error profile
- Achieves ROC-AUC of 0.9382, but PR-AUC drops to 0.2764
- Recall increases dramatically (0.8222), while precision decreases substantially (0.1057)
- Reflects a model optimized for sensitivity at the expense of many false positives on the original distribution
""")

st.markdown("---")

# PR Curves
st.markdown("### Precision-Recall Curves")
st.markdown("""
The Precision-Recall (PR) curve is particularly important for imbalanced datasets as it focuses on the 
performance of the positive (minority) class. Unlike ROC-AUC, PR-AUC is more informative when the 
positive class is rare.
""")

# Placeholder for PR curve image
st.image('image/image_1.png', caption='Precision-Recall Curves for All Models', use_container_width=True)

st.info("""
**Key Observation:** The PR curves clearly show that tree-based models (Random Forest and XGBoost) 
significantly outperform linear models. XGBoost with imbalance weighting provides the best balance 
between precision and recall across different thresholds.
""")

st.markdown("---")

# Feature Importance
st.markdown("### Feature Importance Analysis")
st.markdown("""
Feature importance analysis reveals which features contribute most to the model's predictions. 
This helps understand what patterns the model uses to identify fraudulent clicks.
""")

# Placeholder for feature importance image
st.image('image/feature_importance.png', caption='Feature Importance from XGBoost Model', use_container_width=True)

st.markdown("""
**Key Findings:**
- `app`, `ip_app_count`, `ip_count`, and `ip_app_os_count` are the strongest predictors
- `channel`, `device`, and time-related features such as `next_click` and `weekday` provide additional signal
- Behavioral repetition patterns (count-based features) dominate fraud signal detection
- Temporal features capture automated clicking patterns
""")

st.markdown("---")

# Model Comparison
st.markdown("### Model Selection Recommendation")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**Best Overall**")
    st.success("XGBoost (FE)")
    st.markdown("""
    - Highest PR-AUC (0.3639)
    - Balanced precision/recall
    - Robust to imbalance
    """)

with col2:
    st.markdown("**High Recall**")
    st.warning("XGBoost (Undersampled)")
    st.markdown("""
    - Catches 82% of fraud
    - Many false positives
    - Use when missing fraud is costly
    """)

with col3:
    st.markdown("**Feature Engineering**")
    st.info("Random Forest (FE)")
    st.markdown("""
    - Strong performance
    - Good interpretability
    - Competitive alternative
    """)

st.markdown("---")

# Footer
st.markdown("""
<div style='text-align: center; color: #7f8c8d; padding: 1rem 0;'>
    <p>Modeling & Results | Click Fraud Detection Analysis</p>
</div>
""", unsafe_allow_html=True)