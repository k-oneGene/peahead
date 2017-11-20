import os
import sqlite3

# Config related

file_loc = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
file_db = os.path.join(file_loc, 'selfdata_01.db')

# =====================

conn = sqlite3.connect(file_db, check_same_thread=False)
c = conn.cursor()


