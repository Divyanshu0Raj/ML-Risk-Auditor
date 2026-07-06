📊 ML Risk Auditor

«AI-powered dataset auditing platform that identifies machine learning risks, evaluates data quality, and provides intelligent preprocessing recommendations before model training.»

---

🚀 Overview

Building a machine learning model starts long before selecting an algorithm.

Poor data quality is one of the biggest reasons why machine learning projects fail. Missing values, duplicate records, identifier leakage, high-cardinality features, and inconsistent datasets can significantly reduce model performance and increase development time.

ML Risk Auditor automates the dataset auditing process by analyzing uploaded datasets, identifying common data quality issues, and generating actionable recommendations. It also integrates an AI-powered assistant capable of answering questions about the uploaded dataset and suggesting preprocessing strategies.

The goal of this project is to help data scientists, machine learning engineers, and students quickly understand whether a dataset is ready for machine learning.

---

🎯 Problem Statement

Before training a machine learning model, developers often spend hours manually checking:

- Missing values
- Duplicate records
- Constant columns
- High-cardinality features
- Identifier columns
- Dataset structure
- Feature types

This manual process is repetitive, error-prone, and time-consuming.

ML Risk Auditor automates these tasks and provides a structured quality report along with AI-generated insights.

---

💡 Key Features

📂 Universal Dataset Loader

Supports multiple dataset formats including:

- CSV
- Excel (.xlsx / .xls)
- JSON
- TSV
- Parquet

---

📈 Dataset Summary

Automatically extracts:

- Total rows
- Total columns
- Numeric features
- Categorical features
- Boolean features
- Date features
- Missing value statistics
- Duplicate row statistics

---

🔍 Data Quality Analysis

Automatically detects:

- Missing Values
- Duplicate Rows
- Constant Columns
- High Cardinality Features
- Identifier-like Columns
- Empty Columns

Every detected issue includes:

- Severity Level
- Percentage
- Recommendation

---

🤖 AI Data Science Copilot

Powered by Groq LLM.

Users can ask natural language questions such as:

- Is this dataset suitable for Linear Regression?
- Which columns should I remove?
- How should I handle missing values?
- Which encoding technique should I use?
- Is my dataset ready for machine learning?
- Suggest preprocessing steps.
- Recommend feature engineering ideas.

The AI uses the generated quality report to provide context-aware recommendations instead of generic responses.

---

⚙️ How It Works

                Upload Dataset
                       │
                       ▼
           Universal Dataset Loader
                       │
                       ▼
            Dataset Structure Analysis
                       │
                       ▼
           Data Quality Detection Engine
                       │
                       ▼
      Missing • Duplicate • Constant
     High Cardinality • Identifiers
                       │
                       ▼
          Dataset Quality Report
                       │
                       ▼
          AI Data Science Copilot
                       │
                       ▼
      Intelligent ML Recommendations

---

🏗️ Project Architecture

ML-Risk-Auditor/

│── app.py
│
├── utils/
│   ├── Loader.py
│   ├── data_summary.py
│   ├── DataQuality.py
│   └── AI.py
│
├── sample_data/
│
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md

---

🧠 Core Modules

Loader.py

Responsible for loading datasets from different file formats into Pandas DataFrames.

Supported formats:

- CSV
- Excel
- JSON
- TSV
- Parquet

---

data_summary.py

Generates a high-level summary of the uploaded dataset including:

- Dataset dimensions
- Column types
- Missing values
- Duplicate rows

---

DataQuality.py

Performs automated dataset auditing by analyzing:

- Missing value percentages
- Duplicate records
- Constant features
- High-cardinality features
- Identifier-like columns
- Empty columns

Each issue is classified by severity and accompanied by preprocessing recommendations.

---

AI.py

Acts as the AI engine of the application.

Responsibilities include:

- Creating structured prompts
- Sending requests to the Groq API
- Returning AI-generated insights and recommendations based on the dataset analysis

---

🛠️ Technology Stack

Category| Technologies
Language| Python
Frontend| Streamlit
Data Processing| Pandas
AI| Groq LLM
Environment| python-dotenv

---

📦 Installation

Clone the repository

git clone https://github.com/Divyanshu0Raj/ML-Risk-Auditor.git

Move into the project

cd ML-Risk-Auditor

Install dependencies

pip install -r requirements.txt

Create a ".env" file

GROQ_API_KEY=YOUR_GROQ_API_KEY

Run the application

streamlit run app.py

---

🎯 Example Workflow

1. Upload a dataset.
2. The application analyzes the dataset structure.
3. Data quality checks are executed automatically.
4. A comprehensive quality report is generated.
5. Ask questions using the AI Data Science Copilot.
6. Receive preprocessing suggestions and ML guidance.
7. Improve the dataset before model training.

---

📌 Current Capabilities

- Multi-format dataset loading
- Automatic dataset summarization
- Missing value detection
- Duplicate detection
- Constant column detection
- High-cardinality analysis
- Identifier detection
- Empty column detection
- AI-powered dataset consultation

---

🔮 Future Roadmap

Version 1.1

- Dataset Health Score
- Improved AI reasoning
- Export quality report
- Enhanced UI

Version 2.0

- Automatic Data Cleaning
- Outlier Detection
- Correlation Analysis
- Data Leakage Detection
- Feature Engineering Suggestions
- ML Readiness Score
- One-click Preprocessing Pipeline
- Download Clean Dataset

---

🤝 Contributions

Contributions, feature requests, and suggestions are welcome.

If you have ideas for improving ML Risk Auditor, feel free to open an issue or submit a pull request.

---

📄 License

This project is licensed under the MIT License.

---

👨‍💻 Author

Divyanshu Singh Nathawat

Aspiring AI & Machine Learning Engineer

Building practical AI applications that solve real-world problems through machine learning, automation, and intelligent systems.
