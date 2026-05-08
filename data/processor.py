import pandas as pd

def process_bounces(clients_df, bounces_df):
    try:
        clients_df = clients_df.copy()
        bounces_df = bounces_df.copy()
        merged = pd.merge(clients_df, bounces_df, left_on='Email', right_on='Destinatário')

        if merged.empty:
            return None, "No bounces found."

        return merged, None
    except Exception as e:
        return None, f"Error processing data: {e}"