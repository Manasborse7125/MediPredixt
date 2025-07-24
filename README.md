# MediPredixt

![MediPredixt Logo](https://upload.wikimedia.org/wikipedia/commons/c/cf/New_Power_BI_Logo.svg)

## AI-Powered Health Risk Detection

MediPredixt is a machine learning-based project designed to predict health risks with a current focus on **Cancer** and **Diabetes**. This tool helps users understand their potential risk by analyzing relevant data, and it generates detailed PDF reports for easy sharing and record-keeping.

---

## About the Diseases

### Cancer

Cancer is a group of diseases characterized by uncontrolled growth and spread of abnormal cells. It occurs due to mutations in the DNA of cells, which can instruct cells to grow rapidly, avoid normal growth checks, and evade repair mechanisms. These changes can accumulate due to factors like genetics, environmental exposures, lifestyle choices, or infections.

![Cancer Cells](https://upload.wikimedia.org/wikipedia/commons/0/0f/Cancer_cells_PHIL_4066_lores.jpg)

*Cancer is a complex disease with many types and causes, and early detection is key to effective treatment.*

### Diabetes

Diabetes is a chronic disease that results from the pancreas producing insufficient insulin or the body failing to effectively use the insulin produced. This disease causes high blood sugar levels, leading to severe health complications over time if unmanaged.

There are different types of diabetes:
- **Type 1 Diabetes:** An autoimmune condition where the body attacks insulin-producing cells.
- **Type 2 Diabetes:** The body resists insulin or doesn't produce enough.

Common complications include cardiovascular disease, nerve damage, and kidney problems.

![Diabetes Illustration](https://upload.wikimedia.org/wikipedia/commons/3/3a/Diabetes_growth.svg)

*Managing diabetes involves monitoring blood sugar levels, maintaining a healthy lifestyle, and medications as needed.*

---

## Project Overview

MediPredixt currently integrates:

- Two predictive Machine Learning models:
  - **Cancer Risk Prediction Model**
  - **Diabetes Risk Prediction Model**

- Detailed **PDF report generation** presenting the prediction results and analysis.

- Plans to add more disease prediction models in future updates.

---

## Features

- User-friendly interface powered by **Streamlit**.
- Accurate risk predictions using trained models based on medical datasets.
- PDF generation for comprehensive health reports.
- Modular architecture for easy expansion.

---

## Technologies & Tools Used

<p align="left">
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="Python" width="40" height="40"/>
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/scikitlearn/scikitlearn-original.svg" alt="Scikit-learn" width="40" height="40"/>
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/tensorflow/tensorflow-original.svg" alt="TensorFlow" width="40" height="40"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/streamlit/streamlit-original.svg" alt="Streamlit" width="40" height="40"/>
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/postgresql/postgresql-original.svg" alt="PostgreSQL" width="40" height="40"/>
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/git/git-original.svg" alt="Git" width="40" height="40"/>
  <img src="https://upload.wikimedia.org/wikipedia/commons/c/cf/New_Power_BI_Logo.svg" alt="Power BI" width="40" height="40"/>
  <img src="https://scikit-learn.org/stable/_static/scikit-learn-logo-small.png" alt="Scikit-learn" width="40" height="40"/>
</p>

---

## Installation

1. Clone the repository:
  git clone https://github.com/Manasborse7125/MediPredixt.git
  cd MediPredixt

3. Create and activate a virtual environment (recommended):
  python -m venv venv
  ##On macOS/Linux
  source venv/bin/activate
  ##On Windows
  venv\Scripts\activate

4. Install dependencies:
   pip install -r requirements.txt

## Usage

Run the Streamlit app:
streamlit run app.py
