# 🔍 Click Fraud Detection - Multi-Page Streamlit Dashboard

## 📁 Project Structure

```
streamlit_multipage/
├── data/                          # Data files (you need to add)
│   ├── train_sample.csv          # Your sample dataset
│   └── first_1000_rows.csv       # Optional smaller sample
│
├── image/                         # Image files (currently empty)
│   └── (add your images here)
│
├── pages/                         # Auto-discovered by Streamlit
│   ├── 1_Home.py                 # Home page with overview
│   ├── 2_Dataset_Details.py      # Data documentation
│   ├── 3_EDA.py                  # EDA with 4 sub-tabs
│   ├── 4_Data_Cleaning.py        # Preprocessing steps
│   ├── 5_Modeling.py             # ML models & results
│   ├── 6_Conclusion.py           # Key findings
│   └── 7_References.py           # Citations
│
├── utils/                         # Shared utilities
│   ├── __init__.py               # Package initializer
│   └── data_loader.py            # Data loading functions
│
├── config.py                      # Configuration & styling
├── dashboard.py                   # Main entry point
└── requirements.txt               # Python dependencies
```

---

## 🚀 Quick Start

### Step 1: Setup Your Environment

```bash
# Navigate to the streamlit_multipage folder
cd streamlit_multipage

# Install dependencies
pip install streamlit pandas numpy plotly
```

### Step 2: Add Your Data

Place your data file in the `data/` folder:
```bash
# Your file should be at:
data/train_sample.csv
```

### Step 3: Run the Dashboard

```bash
streamlit run dashboard.py
```

The dashboard will automatically open in your browser at `http://localhost:8501`

---

## 📊 How It Works

### Automatic Multi-Page Navigation

Streamlit **automatically** detects files in the `pages/` folder and creates navigation. The naming convention matters:

- `1_Home.py` → Shows as "Home" (number controls order)
- `2_Dataset_Details.py` → Shows as "Dataset Details"
- etc.

### Shared Data Loading

All pages use the **same data loader** from `utils/data_loader.py`:

```python
from utils.data_loader import get_data_with_sidebar_controls

# This function:
# 1. Creates sidebar controls for sampling
# 2. Loads data with caching
# 3. Returns the dataframe
df = get_data_with_sidebar_controls()
```

### Sidebar Controls (Available on Every Page)

```
⚙️ Data Settings
☑ Use sample data
[────●────] 10,000 records

📊 Using 10,000 records
```

Users can adjust sample size from 1,000 to 100,000 records for performance optimization.

---

## 🎨 Pages Overview

### 1. Main Entry (`dashboard.py`)
- Welcome page
- Project overview
- Team information
- Navigation guide

### 2. Home (`pages/1_Home.py`)
- Brief project introduction
- Expandable detailed background
- Quick dataset statistics
- Methodology overview

### 3. Dataset Details (`pages/2_Dataset_Details.py`)
- Dataset overview metrics
- Complete data dictionary
- Feature statistics
- Missing value analysis
- Sample data preview

### 4. EDA (`pages/3_EDA.py`)
Four interactive sub-tabs:
- **🎯 Target Analysis** - Fraud distribution
- **📱 Categorical Features** - App, device, os, channel distributions
- **⏰ Temporal Patterns** - Hourly and daily patterns
- **🔗 Correlations** - Heatmaps and relationships

### 5. Data Cleaning (`pages/4_Data_Cleaning.py`)
- Data quality checks (placeholders)
- Feature engineering sections (placeholders)
- Train/test split strategy (placeholder)
- Image placeholders for visualizations

### 6. Modeling (`pages/5_Modeling.py`)
- Baseline model (Moving Average)
- XGBoost configuration
- LightGBM configuration
- Model comparison
- Code snippets included
- Image placeholders for results

### 7. Conclusion (`pages/6_Conclusion.py`)
- Key findings (placeholder)
- Insights (placeholder)
- Challenges & limitations (placeholder)
- Future work (placeholder)

### 8. References (`pages/7_References.py`)
- Dataset citation
- Academic references
- Tools & libraries
- Additional resources

---

## 🔧 Customization

### Adding New Pages

1. Create a new file in `pages/` folder
2. Name it: `8_Your_Page_Name.py`
3. Streamlit will automatically add it to navigation

Example:
```python
# pages/8_Additional_Analysis.py
import streamlit as st
import sys
sys.path.append('..')

from config import CUSTOM_CSS
from utils.data_loader import get_data_with_sidebar_controls

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)
df = get_data_with_sidebar_controls()

st.title("Additional Analysis")
st.write("Your content here")
```

### Modifying Styles

Edit `config.py` to change:
- Page title and icon
- Custom CSS styling
- Team member names
- Project information

### Adding New Utility Functions

Add functions to `utils/data_loader.py`:
```python
def your_new_function(df):
    # Your code here
    return result
```

Then import in any page:
```python
from utils.data_loader import your_new_function
```

---

## 📝 Filling In Content

All pages with placeholders are marked with:
```
[Your ... here]
```

Search for these in the files and replace with your content.

### Example Locations:
- **Home page:** `[Your detailed research question here]`
- **Data Cleaning:** `[Your missing values analysis here]`
- **Modeling:** `[Your baseline model description and results here]`
- **Conclusion:** `[Your key findings here]`

---

## 🖼️ Adding Images

### Step 1: Add Images to Folder
Place your images in the `image/` folder with suggested names:
- `missing_values_analysis.png`
- `baseline_model_results.png`
- `xgboost_results.png`
- etc.

### Step 2: Uncomment Image Lines
Find commented image lines like:
```python
# st.image('image/image_1.png', use_column_width=True)  # TODO: Replace with 'actual_name.png'
```

Uncomment and update:
```python
st.image('image/baseline_model_results.png', use_column_width=True)
```

---

## ⚙️ Configuration Options

### Data Loading (`utils/data_loader.py`)

**Change default sample size:**
```python
# Line ~68
sample_size = st.sidebar.slider(
    "Sample size", 
    min_value=1000, 
    max_value=100000, 
    value=10000,  # ← Change this default
    step=1000
)
```

**Change data file path:**
```python
# Line ~18
df = pd.read_csv('data/train_sample.csv')  # ← Update path here
```

### Styling (`config.py`)

**Change colors:**
```python
CUSTOM_CSS = """
    <style>
    .main-header {
        color: #1f77b4;  # ← Change header color
    }
    </style>
"""
```

---

## 🐛 Troubleshooting

### Issue: "FileNotFoundError: data/train_sample.csv"
**Solution:** Make sure you're running from the `streamlit_multipage/` folder:
```bash
cd streamlit_multipage
streamlit run dashboard.py
```

### Issue: "ModuleNotFoundError: No module named 'utils'"
**Solution:** The `sys.path.append('..')` should handle this, but if not:
```python
# Add at top of page file
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
```

### Issue: Pages not showing in sidebar
**Solution:** 
1. Restart Streamlit
2. Check file naming (must be in `pages/` folder)
3. Files must have `.py` extension

### Issue: Slow performance
**Solution:** 
1. Reduce sample size in sidebar
2. Clear cache: Settings → Clear cache
3. Use smaller default sample in config

---

## 📊 Performance Tips

### For Development:
- Use 5,000-10,000 records
- Enable sample mode
- Fast iteration

### For Presentation:
- Use 50,000-100,000 records
- Still manageable
- More impressive

### For Final Analysis:
- Uncheck "Use sample data"
- Full dataset analysis
- May be slower

---

## 👥 Team Collaboration

### Working on Different Pages:
1. Each team member works on their assigned page file
2. No merge conflicts since files are separate
3. Pull latest changes before editing

### Sharing Work:
```bash
# Person A works on 3_EDA.py
# Person B works on 5_Modeling.py
# Person C works on 1_Home.py

# No conflicts! 🎉
```

---

## 📦 Dependencies

### Required:
```bash
pip install streamlit pandas plotly
```

### Optional (for modeling):
```bash
pip install xgboost lightgbm scikit-learn
```

---

## 🎯 Next Steps

1. ✅ Copy `train_sample.csv` to `data/` folder
2. ✅ Run `streamlit run dashboard.py`
3. ✅ Navigate through all pages to verify
4. ✅ Fill in placeholder content
5. ✅ Add your images to `image/` folder
6. ✅ Uncomment image display code
7. ✅ Customize styling if needed
8. ✅ Test with different sample sizes

---

## 🆘 Getting Help

### Common Questions:

**Q: How do I change the page order?**
A: Rename files with different numbers: `1_`, `2_`, etc.

**Q: Can I add sub-sub-tabs?**
A: Yes! Use `st.tabs()` inside any page, like in `3_EDA.py`

**Q: How do I share this with my team?**
A: Commit to Git, or zip the entire `streamlit_multipage/` folder

**Q: Can I deploy this online?**
A: Yes! Use Streamlit Cloud, Heroku, or any Python hosting

---

## 📄 License

This project is for educational purposes as part of USC Applied Data Science coursework.

---

## 👥 Team

- **Ching Chuang** - EDA & Feature Engineering
- **Yu-Chieh Chen** - Modeling & Evaluation
- **Jia-Ning Hu** - Dashboard Development

---

**🎉 Your multi-page dashboard is ready! Happy analyzing!**