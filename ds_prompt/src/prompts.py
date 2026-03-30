# ============================================================
# prompts.py — Six different prompting strategies
# Each function takes sample_data (list of dicts) and returns
# a prompt string to send to the AI model.
# ============================================================


def prompt1(sample_data):
    """
    STRATEGY 1: Zero-Shot EDA
    Simple, direct instruction — no role, no examples.
    """
    return f"""
    Analyze this dataset sample:
    {sample_data}

    GIVE:
    - Insights about the data
    - Data types of each column
    - Missing values in the dataset
    """


def prompt2(sample_data):
    """
    STRATEGY 2: Role-Based Prompting
    Assign a persona to get more expert-level analysis.
    """
    return f"""
    ROLE: You are a Senior Data Scientist with 10+ years of experience
    in exploratory data analysis and machine learning.

    TASK: Perform a thorough Exploratory Data Analysis (EDA) on the
    dataset sample provided below.

    DATA:
    {sample_data}

    PROVIDE:
    - Statistical summary of numeric columns
    - Distribution insights
    - Correlations or patterns you notice
    - Potential data quality issues
    - Top 3 business insights
    """


def prompt3(sample_data):
    """
    STRATEGY 3: Chain-of-Thought Prompting
    Ask the model to reason step by step before concluding.
    """
    return f"""
    You are a data analyst. Think step by step before giving your final answer.

    DATASET SAMPLE:
    {sample_data}

    STEP-BY-STEP ANALYSIS:
    Step 1: Identify the columns and their data types.
    Step 2: Check for missing or null values.
    Step 3: Describe the distribution of numerical columns.
    Step 4: Identify any obvious outliers or anomalies.
    Step 5: Summarize the key findings and business implications.

    Work through each step carefully, then provide your final summary.
    """


def prompt4(sample_data):
    """
    STRATEGY 4: Structured Output Prompting
    Ask for a specific formatted response for downstream processing.
    """
    return f"""
    ROLE: Act as a senior web developer and data analyst.

    TASK: Suggest development stages for a data pipeline project
    based on the dataset below.

    DATASET SAMPLE:
    {sample_data}

    OUTPUT FORMAT: Provide the development stages in a structured format,
    including a summary of key findings. Use the following structure:

    ## Stage 1: Data Ingestion
    [description]

    ## Stage 2: Data Cleaning
    [description]

    ## Stage 3: EDA & Visualization
    [description]

    ## Stage 4: Feature Engineering
    [description]

    ## Stage 5: Modeling & Evaluation
    [description]

    ## Key Findings Summary
    [3-5 bullet points]
    """


def prompt5(sample_data):
    """
    STRATEGY 5: Instruction-Following with Constraints
    Give the model specific constraints to follow.
    """
    return f"""
    Give suggestions for cleaning the dataset, including handling
    missing values, correcting data types, removing duplicates,
    and fixing inconsistencies.

    DATASET SAMPLE:
    {sample_data}

    CONSTRAINTS:
    - Keep your response under 300 words
    - Use bullet points for each suggestion
    - Prioritize by impact (high / medium / low)
    - Do NOT suggest deleting rows unless absolutely necessary
    """


def prompt6(sample_data):
    """
    STRATEGY 6: Few-Shot Prompting
    Provide an example before asking for the real analysis.
    """
    example_input = [
        {"name": "Alice", "age": 30, "salary": 70000, "dept": "HR"},
        {"name": "Bob", "age": None, "salary": 85000, "dept": "Engineering"},
    ]
    example_output = """
    - Columns: name (string), age (numeric, 1 missing), salary (numeric), dept (categorical)
    - Missing values: 1 in 'age' column
    - Insight: Engineering has higher salary than HR on average
    - Action: Impute missing age with median
    """

    return f"""
    You are a data analyst. Below is an EXAMPLE of how to analyze a dataset,
    followed by the REAL dataset you should analyze in the same style.

    --- EXAMPLE INPUT ---
    {example_input}

    --- EXAMPLE OUTPUT ---
    {example_output}

    --- REAL DATASET TO ANALYZE ---
    {sample_data}

    Now provide the same style of analysis for the real dataset above.
    """