import pandas as pd
from essay_scoring import client, calculate_pst, calculate_specificity, calculate_pace, calculate_vspice, calculate_creativity

def score_essays(df):
    # Ensure the dataframe has an 'Essay Content' column
    if "Essay Content" not in df.columns:
        raise ValueError("DataFrame must contain a column named 'Essay Content'")
    
    # Initialize empty lists to store scores
    pst_scores = []
    specificity_scores = []
    pace_scores = []
    vspice_scores = []
    creativity_scores = []
    
    for essay in df["Essay Content"]:
        # Defensive: skip if essay is missing
        if pd.isnull(essay) or essay.strip() == "":
            pst_scores.append(None)
            specificity_scores.append(None)
            pace_scores.append(None)
            vspice_scores.append(None)
            creativity_scores.append(None)
            continue
        
        try:
            pst = calculate_pst(essay, client)
            specificity = calculate_specificity(essay, client)
            pace = calculate_pace(essay, client)
            vspice = calculate_vspice(essay, client)
            creativity = calculate_creativity(essay, client)
        except Exception as e:
            print(f"Error scoring an essay: {e}")
            pst, specificity, pace, vspice, creativity = (None, None, None, None, None)
        
        pst_scores.append(pst)
        specificity_scores.append(specificity)
        pace_scores.append(pace)
        vspice_scores.append(vspice)
        creativity_scores.append(creativity)
    
    # Add new columns to the DataFrame
    df["PST Score"] = pst_scores
    df["Specificity Score"] = specificity_scores
    df["Pace Score"] = pace_scores
    df["VSPICE Score"] = vspice_scores
    df["Creativity Score"] = creativity_scores
    
    return df

df = pd.read_csv("only_essays.csv")
scored_df = score_essays(df)

# Save the result
scored_df.to_csv("scored_essays.csv", index=False)
print("✅ Saved just the student essays to 'scored_essays.csv'.")