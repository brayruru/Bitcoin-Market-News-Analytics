
import sqlite3
import logging
from datetime import datetime

import os
os.makedirs("logs", exist_ok=True)

# Configuración de logging
logging.basicConfig(filename='logs/pipeline.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def save_to_db(df, table_name, db_path='db/bitcoin.db'):
    conn = sqlite3.connect(db_path)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.close()
    

def log_and_print(msg):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    full_msg = f"[{timestamp}] {msg}"
    print(full_msg)
    logging.info(full_msg)
