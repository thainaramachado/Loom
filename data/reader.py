import pandas as pd


def read_clients(excel_file): 
    """Reads and validates the Excel file"""
    df = pd.read_excel(excel_file)
    
    if 'Email' not in df.columns or 'Cliente' not in df.columns:
        return None, "Invalid file: required columns 'Email' and 'Cliente' not found."
    
    return df, None

def read_bounces(csv_file):
    """Reads and validates the bounce CSV"""
    df = pd.read_csv(csv_file)

    if 'Destinatário' not in df.columns or 'Motivo do bounce' not in df.columns:
        return None, "Invalid file: required columns 'Destinário' and 'Motivo do bounce' not found."
    
    return df, None