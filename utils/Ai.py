import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()


def create_prompt(summary, quality_report, user_question):

    prompt = f"""
You are a Senior Machine Learning Engineer.

Analyze the dataset using the information below.

==========================
DATASET SUMMARY

Rows: {summary["rows"]}
Columns: {summary["cols"]}

Numeric Columns:
{summary["numeric_cols"]}

Categorical Columns:
{summary["categorical_cols"]}

Boolean Columns:
{summary["boolean_cols"]}

Date Columns:
{summary["date_cols"]}

==========================
DATA QUALITY REPORT

{quality_report}

==========================
USER QUESTION

{user_question}

==========================

Instructions:

- Explain the problem clearly.
- Give practical recommendations.
- Suggest preprocessing techniques.
- Provide Python code if required.
- Keep the answer concise and professional.
"""

    return prompt


def ask_ai(prompt):

    client = Groq(
        api_key=os.getenv("GROQ_API_KEY")
    )

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]

    )

    return response.choices[0].message.content


def generate_ai_response(summary, quality_report, user_question):

    prompt = create_prompt(
        summary,
        quality_report,
        user_question
    )

    response = ask_ai(prompt)

    return response


