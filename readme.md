NormanPD Incident Data Visualization

Project Overview
This project is a web-based application that visualizes incident data from the Norman Police Department (NormanPD). Users can upload PDF files containing incident data, which the application processes to generate meaningful visualizations. The visualizations include:
1. Bar Chart: Comparison of incidents by type.
2. Clustering Visualization: Grouping of records using k-means clustering.
3. Custom Scatter Plot: Visualization of incidents by time and location.

The application is built using Flask, Matplotlib, and SQLite, and is styled for better user experience with Bootstrap.

Features
- File Upload: Users can upload NormanPD-style PDF files.
- Data Processing: Extracts incident data from PDFs and stores it in an SQLite database.
- Interactive Visualizations:
  - Bar Chart: Shows the frequency of different incident types.
  - Clustering Visualization: Groups data using clustering algorithms.
  - Custom Scatter Plot: Displays relationships between incident times and locations.

  
Project Structure
cise6930fa24-project3/
├── COLLABORATORS # List of collaborators and their contributions
├── LICENSE # Project licensing information 
├── README.md # This file 
├── Pipfile # Python dependencies
├── Pipfile.lock # Locked dependencies 
├── main.py # Main Flask application
├── resources/ 
│ └── normanpd.db # SQLite database for incident data
├── static/ # Static files for storing visualizations 
  ├── bar_chart.png 
  ├── clustering.png 
  └── custom_visualization.png 
├── src/ │
      ├── init.py # Initialization file 
      ├── utils.py # Functions for processing PDFs and database management
      └── visualizations.py # Functions to generate visualizations 
├── templates/ # HTML templates for the web interface 
       │ ├── index.html # Upload page 
       │ ├── visualize.html # Visualization selection page 
       │ ├── bar_chart.html # Bar chart display page 
       │ ├── clustering.html # Clustering visualization display page 
       │ └── custom_visualization.html # Custom scatter plot display page 
└── uploads/ # Folder for uploaded PDFs

RUN:
step1- creating virtual environment
        python3 -m venv venv
        source venv/bin/activate

step2- Install depndencies
        pip install pipenv
        pipenv install    

step3- Run the application
        python3 main.py

step4- access the application
        http://127.0.0.1:8000
        
step5- upload normanpd pdf

step6- visualize charts
        
Dependencies
The project uses the following libraries:

Flask: Web framework for the application.
SQLite: Lightweight database for storing incident data.
Matplotlib: Library for creating visualizations.
pypdf: For extracting text data from PDF files.
Scikit-learn: Used for clustering algorithms.
Bootstrap: For styling the web pages.

Future Improvements
Add more customization options for visualizations.
Improve error handling for improperly formatted PDFs.
Enhance clustering by using more relevant features (e.g., incident location coordinates).
Add user authentication for secured access.