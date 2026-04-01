import pandas as pd
import os
import time
from src.config import get_client
from src.prompts import prompt1, prompt2, prompt3, prompt4, prompt5, prompt6

# ─────────────────────────────────────────────
# Base path setup
# ─────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "products.csv")

PROMPT_MAP = {
    1: (prompt1, "Zero-Shot EDA"),
    2: (prompt2, "Role-Based Prompting"),
    3: (prompt3, "Chain-of-Thought"),
    4: (prompt4, "Structured Output"),
    5: (prompt5, "Instruction with Constraints"),
    6: (prompt6, "Few-Shot Prompting"),
}


def generate_eda_report(file_path, prompt_number=1):
    df = pd.read_csv(file_path)
    sample_data = df.head(10).to_dict(orient="records")

    prompt_fn, strategy_name = PROMPT_MAP.get(prompt_number, (prompt1, "Zero-Shot EDA"))
    prompt = prompt_fn(sample_data)

    print(f"\n{'='*60}")
    print(f"  PROMPT STRATEGY {prompt_number}: {strategy_name}")
    print(f"{'='*60}")
    print(f"Sending request to Groq...\n")

    # Call Groq API
    client = get_client()
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content


def run_all_prompts(file_path):
    results = {}

    for num in range(1, 7):
        result = generate_eda_report(file_path, prompt_number=num)
        results[num] = result
        print(result)
        print("\n")
        time.sleep(3)  # small delay between requests

    # Save all results
    output_path = os.path.join(BASE_DIR, "eda_results.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        for num, text in results.items():
            _, strategy_name = PROMPT_MAP[num]
            f.write(f"\n{'='*60}\n")
            f.write(f"PROMPT {num}: {strategy_name}\n")
            f.write(f"{'='*60}\n")
            f.write(text)
            f.write("\n\n")

    print(f"\n✅ All results saved to: {output_path}")
    return results


if __name__ == "__main__":
    print("\n🚀 Starting EDA with 6 Prompt Engineering Strategies")
    print(f"📄 Dataset: {file_path}\n")
    run_all_prompts(file_path)