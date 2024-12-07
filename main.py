import os
import sys
import matplotlib
matplotlib.use('Agg')  # Use a non-GUI backend for Matplotlib
from flask import Flask, render_template, request, redirect, url_for, send_file
from src.utils import fetch_incidents, extract_incidents, createdb, populatedb
from src.visualizations import create_bar_chart, create_clustering, create_custom_visualization

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
STATIC_FOLDER = "static"
DB_NAME = os.path.join(STATIC_FOLDER, "normanpd.db")

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(STATIC_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file uploaded", 400
    file = request.files['file']
    if file:
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)

        # Process the uploaded file
        pdf_content = fetch_incidents(file_path)
        incidents = extract_incidents(pdf_content)
        createdb(DB_NAME)
        populatedb(DB_NAME, incidents)

        return redirect(url_for('visualize'))
    return "File upload failed", 500

@app.route('/visualize')
def visualize():
    return render_template('visualize.html')

@app.route('/visualize/bar')
def bar_chart():
    create_bar_chart(DB_NAME)
    return send_file(os.path.join(STATIC_FOLDER, "bar_chart.png"), mimetype="image/png")

@app.route('/visualize/cluster')
def clustering():
    create_clustering(DB_NAME)
    return send_file(os.path.join(STATIC_FOLDER, "clustering.png"), mimetype="image/png")

@app.route('/visualize/custom')
def custom_chart():
    create_custom_visualization(DB_NAME)
    return send_file(os.path.join(STATIC_FOLDER, "custom_visualization.png"), mimetype="image/png")

if __name__ == '__main__':
    app.run(debug=True, port=8000, host='0.0.0.0')
    app.run(debug=True, port=8000)
