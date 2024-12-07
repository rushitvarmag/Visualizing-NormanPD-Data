import sqlite3
import os
from io import BytesIO
from pypdf import PdfReader


def fetch_incidents(file_path):
    return BytesIO(open(file_path, 'rb').read())


def extract_incidents(file_content):
    reader = PdfReader(file_content)
    text_data = [page.extract_text(extraction_mode="layout") for page in reader.pages]
    incidents = []

    for page_text in text_data:
        lines = page_text.split('\n')
        for line in lines:
            fields = line.split('  ')
            if len(fields) >= 5:
                date_time, incident_number, location, nature, ori = map(str.strip, fields[:5])
                incidents.append({
                    'incident_time': date_time,
                    'incident_number': incident_number,
                    'incident_location': location,
                    'nature': nature,
                    'incident_ori': ori,
                })
    return incidents


def createdb(db_name):
    os.makedirs(os.path.dirname(db_name), exist_ok=True)
    with sqlite3.connect(db_name) as conn:
        conn.execute('DROP TABLE IF EXISTS incidents')
        conn.execute('''
            CREATE TABLE incidents (
                incident_time TEXT,
                incident_number TEXT,
                incident_location TEXT,
                nature TEXT,
                incident_ori TEXT
            )
        ''')


def populatedb(db_name, data):
    with sqlite3.connect(db_name) as conn:
        conn.executemany(
            'INSERT INTO incidents VALUES (?, ?, ?, ?, ?)',
            [(d['incident_time'], d['incident_number'], d['incident_location'], d['nature'], d['incident_ori']) for d in data]
        )
