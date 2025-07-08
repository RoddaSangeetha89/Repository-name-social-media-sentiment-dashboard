from datasets import load_dataset
import pandas as pd

def load_data():
    print("📦 Loading healthcare sentiment dataset...")
    dataset = load_dataset("AhmedSSoliman/sentiment-analysis-for-mental-health-Combined-Data")
    df = pd.DataFrame(dataset['train'])

    print("\n🧪 Columns found:", df.columns.tolist())

    # ✅ Rename to 'text' and 'label' so app.py can work
    df = df.rename(columns={
        'statement': 'text',
        'status': 'label'
    })

    # Add a dummy timestamp for trend plotting
    df['timestamp'] = pd.date_range(start='2024-01-01', periods=len(df), freq='D')

    return df
