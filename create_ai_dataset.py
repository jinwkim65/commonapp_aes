import pandas as pd
from openai import OpenAI
import time
import os

key = os.getenv("OPENAI_API_KEY")
if not key:
    raise ValueError("Missing OPENAI_API_KEY environment variable")

client = OpenAI(api_key=key)
df = pd.read_csv("asyncdata_clean.csv")

# Define a function to truncate to just the essay
def extract_essay_only(document_content, index, total):
    try:
        print(f"[{index+1}/{total}] Extracting essay...")
        response = client.responses.create(
            model="gpt-4o",
            instructions=(
                "You are a helpful assistant that receives the full text of a student document and extracts ONLY the student's essay. Ignore all feedback, comments, or extra text."
            ),
            input=document_content
        )
        return response.output_text.strip()
    
    except Exception as e:
        print(f"❌ Error at row {index}: {e}")
        return ""

# Apply it with progress
essays = []
total_rows = len(df)

for idx, row in df.iterrows():
    document_content = row['Document Content']
    essay = extract_essay_only(document_content, idx, total_rows)
    essays.append(essay)

# Replace the column
df['Essay Content'] = essays

# Save the result
df.to_csv("only_essays.csv", index=False)
print("✅ Saved just the student essays to 'only_essays.csv'.")