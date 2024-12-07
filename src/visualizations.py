import matplotlib.pyplot as plt
import sqlite3
import numpy as np
from sklearn.cluster import KMeans

STATIC_FOLDER = "static"

def get_data_from_db(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("SELECT nature, COUNT(*) FROM incidents GROUP BY nature")
    data = cursor.fetchall()
    conn.close()
    return data

def create_bar_chart(db_name):
    data = get_data_from_db(db_name)
    labels = [item[0] for item in data]
    values = [item[1] for item in data]

    plt.figure()
    plt.bar(labels, values, color='blue')
    plt.xticks(rotation=45, ha='right')
    plt.title("Offenses by Count")
    plt.xlabel("Offense Type")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(f"{STATIC_FOLDER}/bar_chart.png")
    plt.close()  # Close the figure to free memory

def create_clustering(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("SELECT incident_time, nature FROM incidents")
    data = cursor.fetchall()
    conn.close()

    if data:
        X = np.array([[len(item[0]), len(item[1])] for item in data])  # Example: lengths as features
        kmeans = KMeans(n_clusters=3)
        labels = kmeans.fit_predict(X)

        plt.figure()
        plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
        plt.title("Clustering of Offenses")
        plt.xlabel("Time Length")
        plt.ylabel("Nature Length")
        plt.tight_layout()
        plt.savefig(f"{STATIC_FOLDER}/clustering.png")

def create_custom_visualization(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("SELECT incident_time, incident_location FROM incidents")
    data = cursor.fetchall()
    conn.close()

    times = [len(item[0]) for item in data]
    locations = [len(item[1]) for item in data]

    plt.figure()
    plt.scatter(times, locations, alpha=0.6)
    plt.title("Incidents by Time and Location")
    plt.xlabel("Time (Length)")
    plt.ylabel("Location (Length)")
    plt.tight_layout()
    plt.savefig(f"{STATIC_FOLDER}/custom_visualization.png")
