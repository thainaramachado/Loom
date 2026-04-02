import pandas as pd


def read_clients(execel_file): 
    """Reads and validates the Excel file"""
    df = pd.read_excel(execel_file)
    df.columns = df.columns.str.lower()
    
    if 'email' not in df.columns or 'cliente' not in df.columns:
        return None, "Invalid file: required columns 'Email' and 'Cliente' not found."
    
    return df, None

def read_bounces(csv_file):
    """Reads and validates the Locaweb bounce CSV"""
    df = pd.read_csv(csv_file)
    df.columns = df.columns.str.lower()

    if 'destinatário' not in df.columns or 'motivo do bounce' not in df.columns:
        return None, "Invalid file: required columns 'Destinário' and 'Motivo do bounce' not found."
    
    return df, None