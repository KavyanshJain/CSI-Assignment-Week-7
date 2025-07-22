# CSI-Assignment-Week-7
## ML Model Deployment with Streamlit

This project demonstrates how to deploy a trained machine learning model using [Streamlit](https://streamlit.io). The app provides an interactive interface where users can input data, receive model predictions, and understand outputs through visualizations.

LIVE LINK - https://kavyansh-adult-census-ml.streamlit.app/

## 📁 Project Structure

```
CSI-Assignment-Week-7/
│
├── data/
|   └── adult.csv       # dataset model was trained
|   └── adult.test.csv       # dataset used for test
|   └── data_description.txt       # data description
├── model/
│   └── trained_model.pkl    # Saved trained model
├── adult_census_income.ipynb       # python notebook for the analysis and work
├── app.py                    # Streamlit web app
├── requirements.txt         # Project dependencies
└── README.md               # Project documentation
```

---

## Features

- Train and save a machine learning model
- Deploy the model via a user-friendly Streamlit app
- Allow user input through interactive sliders
- Display predicted class with confidence
- Real-time prediction updates

---

## 🔧 Setup Instructions

### 1. **Clone the repository**
```bash
git clone https://github.com/KavyanshJain/CSI-Assignment-Week-7.git
cd CSI-Assignment-Week-7
```

### 2. **Install dependencies**
```bash
pip install -r requirements.txt
```

### 3. **Run the Streamlit app**
```bash
streamlit run app.py
```

### 4. **Access the application**
Open your browser and navigate to `http://localhost:8501`

---

## 📊 Model Details

- **Model**: Gradient Boosting
- **Dataset**: Adult Census (from University of California ML repo)
- **Features**: 
  - Age
  - Workclass
  - EducationNum
  - Marital Status
  - Occupation
  - Relationship
  - Gender
  - Capital Gain
  - capital loss
  - Hours per Week
- **Target**: Income
  - <=50K
  - >50k

---

## 📦 Dependencies

To Run Webapp

```txt
streamlit
scikit-learn
joblib
numpy
matplotlib
pandas
```

To Run the notebook

```txt
scikit-learn
joblib
numpy
matplotlib
seaborn
pandas
plotly
```


---

## 📸 Application Preview

<img width="1366" height="1297" alt="app" src="https://github.com/user-attachments/assets/af93e900-bf5d-496f-8ade-bb7062469ec5" />


---

## 🎯 Usage

1. Launch the application using the setup instructions
2. Adjust the feature sliders to input your measurements
3. View the real-time prediction results
4. Explore the notebook for indepth reasearch and analysis
5. Experiment with different input combinations

---

## Creator
Kavyansh Jain

---
