
import streamlit as st
import pandas as pd
from utils.Loader import load_dataset
from utils.data_summary import get_dataset_summary
from utils.DataQuality import check_data_quality
from utils.Ai import generate_ai_response

st.set_page_config(
    page_title="ML Risk Auditor",
    page_icon="📊",
    layout="wide"
)

st.title("📊 ML Risk Auditor")

uploaded_file = st.file_uploader(
    "Upload your dataset",
    type=["csv", "json", "parquet", "xlsx", "xls", "tsv"]
)

if uploaded_file is not None:
    try:
        df = load_dataset(uploaded_file)

        st.success(f"✅ {uploaded_file.name} loaded successfully!")

        # Preview
        st.subheader("Dataset Preview")
        st.dataframe(df)

        # Basic info
        st.subheader("Dataset Information")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Rows", df.shape[0])
        with col2:
            st.metric("Columns", df.shape[1])

        # -----------------------------
        # Dataset Summary Section
        # -----------------------------
        summary = get_dataset_summary(df)

        st.subheader("Dataset Summary")

        c1, c2, c3, c4 = st.columns(4)
        with c1:
            st.metric("Total Missing", int(summary.get("total_missing", 0)))
        with c2:
            st.metric("Duplicate Rows", int(summary.get("total_duplicated", 0)))
        with c3:
            st.metric("Numeric Columns", len(summary.get("numeric_cols", [])))
        with c4:
            st.metric("Categorical Columns", len(summary.get("categorical_cols", [])))

        with st.expander("Column Type Details"):
            st.write("**Numeric columns:**", summary.get("numeric_cols", []))
            st.write("**Categorical columns:**", summary.get("categorical_cols", []))
            st.write("**Boolean columns:**", summary.get("boolean_cols", []))
            st.write("**Date columns:**", summary.get("date_cols", []))

        with st.expander("Missing values by column"):
            missing_series = summary.get("missing_data", pd.Series(dtype=int))
            # keep only columns with missing > 0
            missing_df = (
                missing_series[missing_series > 0]
                .sort_values(ascending=False)
                .reset_index()
            )
            missing_df.columns = ["column", "missing_count"]
            if missing_df.empty:
                st.info("No missing values found.")
            else:
                st.dataframe(missing_df, use_container_width=True)

        # -----------------------------
        # Data Quality Section
        # -----------------------------
        quality = check_data_quality(df)

        st.subheader("Data Quality Report")

        # Duplicates
        st.markdown("### Duplicates")
        dup = quality.get("duplicates", {})
        d1, d2, d3 = st.columns(3)
        with d1:
            st.metric("Duplicated Rows", int(dup.get("duplicated_count", 0)))
        with d2:
            st.metric("Duplicate %", f'{dup.get("duplicated_percentage", 0)}%')
        with d3:
            st.metric("Severity", dup.get("severity", "N/A"))
        if dup.get("recommendation"):
            st.caption(f"Recommendation: {dup.get('recommendation')}")

        # Missing report table
        st.markdown("### Missing Values (Per Column)")
        missing_report = quality.get("missing", {})
        missing_rows = []
        for col, info in missing_report.items():
            if info.get("missing_count", 0) > 0:
                missing_rows.append({
                    "column": col,
                    "missing_count": info.get("missing_count", 0),
                    "missing_percentage": info.get("missing_percentage", 0),
                    "severity": info.get("severity", ""),
                    "recommendation": info.get("recommendation", "")
                })

        if missing_rows:
            st.dataframe(
                pd.DataFrame(missing_rows).sort_values(
                    by="missing_percentage", ascending=False
                ),
                use_container_width=True
            )
        else:
            st.info("No missing values detected.")

        # Constant columns
        st.markdown("### Constant Columns")
        constant_cols = quality.get("constant_columns", {})
        if constant_cols:
            const_df = pd.DataFrame.from_dict(constant_cols, orient="index").reset_index()
            const_df = const_df.rename(columns={"index": "column"})
            st.dataframe(const_df, use_container_width=True)
        else:
            st.info("No constant columns found.")

        # High cardinality
        st.markdown("### High Cardinality Columns")
        high_card = quality.get("high_cardinality_columns", {})
        if high_card:
            hc_df = pd.DataFrame.from_dict(high_card, orient="index").reset_index()
            hc_df = hc_df.rename(columns={"index": "column"})
            hc_df = hc_df.sort_values(by="unique_percentage", ascending=False)
            st.dataframe(hc_df, use_container_width=True)
        else:
            st.info("No high-cardinality columns found.")

        # Identifier-like columns
        st.markdown("### Identifier-like Columns")
        identifiers = quality.get("identifiers", {})
        if identifiers:
            id_df = pd.DataFrame.from_dict(identifiers, orient="index").reset_index()
            id_df = id_df.rename(columns={"index": "column"})
            st.dataframe(id_df, use_container_width=True)
        else:
            st.info("No likely identifier columns detected.")

        # Empty columns
        st.markdown("### Empty Columns")
        empty_cols = quality.get("empty_columns", {})
        if empty_cols:
            empty_df = pd.DataFrame.from_dict(empty_cols, orient="index").reset_index()
            empty_df = empty_df.rename(columns={"index": "column"})
            st.dataframe(empty_df, use_container_width=True)
        else:
            st.info("No fully empty columns found.")

        # Full JSON (debug / transparency)
        with st.expander("View full quality report (JSON)"):
            st.json(quality)

        # -----------------------------
        # AI Chatbot integration
        # -----------------------------
        st.markdown("---")
        st.subheader("🤖 AI Chatbot")

        st.write(
            "Ask the AI about the dataset, for example: 'Which columns should I drop before training?' "
            "or 'Suggest preprocessing steps for missing values and high-cardinality features.'"
        )

        user_question = st.text_area(
            "Ask a question about the dataset or request suggestions",
            value="",
            height=120,
        )

        if st.button("Ask AI"):
            if not user_question.strip():
                st.warning("Please type a question for the AI.")
            else:
                with st.spinner("Querying AI — this may take a few seconds..."):
                    try:
                        response = generate_ai_response(summary, quality, user_question)
                    except Exception as e:
                        response = f"ERROR: Exception while calling AI: {e}"

                if isinstance(response, str) and response.startswith("ERROR:"):
                    st.error(response)
                else:
                    st.subheader("AI Response")
                    st.write(response)

    except Exception as e:
        st.error(f"❌ {e}")
