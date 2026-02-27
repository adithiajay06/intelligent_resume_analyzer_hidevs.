# Intelligent Resume Analyzer

## Overview

The Intelligent Resume Analyzer is a Python-based application designed to automate the resume screening process. It parses resumes, extracts important candidate information such as name, email, skills, and experience, and compares them with job requirements. The system calculates a match score (0–100) and generates hiring recommendations. This helps recruiters save time and make accurate, data-driven hiring decisions.

---

## Key Features

* Automatic resume parsing from text files
* Extracts candidate details:

  * Name
  * Email
  * Skills
  * Years of experience
* Matches candidate skills with job requirements
* Calculates match score (0–100)
* Generates hiring recommendations:

  * Highly Recommended
  * Recommended
  * Consider
  * Not Recommended
* Saves results in JSON format
* Clean and modular Python code
* Error handling for missing or invalid data

---

## Project Structure

```
intelligent_resume_analyzer_hidevs
│
├── resumes/
│   └── resume1.txt
│
├── resume_screening.py
├── job_requirements.json
├── results.json
└── README.md
```

---

## Setup Guide

### Step 1: Clone or Download the Project

Download the project folder or clone from GitHub.

### Step 2: Add Resume Files

Place resume files inside the `resumes` folder in `.txt` format.

Example:

```
Name: Adithi Sharma
Email: adithi@email.com

Skills: Python, SQL, Machine Learning, Git

Experience: 2 years
```

---

### Step 3: Configure Job Requirements

Edit the `job_requirements.json` file:

```
{
  "job_title": "Machine Learning Engineer",
  "required_skills": ["Python", "Machine Learning", "SQL", "Git"],
  "preferred_skills": ["Deep Learning", "TensorFlow"],
  "min_experience": 2
}
```

---

### Step 4: Run the Program

Open Command Prompt and run:

```
python resume_screening.py
```

---

### Step 5: View Results

The system will:

* Display results in the terminal
* Save results in `results.json`

Example output:

```
Name: Adithi A
Match Score: 80.0
Recommendation: Highly Recommended
```

---

## How the Matching Algorithm Works

Match score is calculated based on:

* Required skills match – 70%
* Preferred skills match – 20%
* Experience match – 10%

Total score ranges from 0 to 100.

---

## Outcome

This project successfully automates resume screening by:

* Parsing resumes
* Matching candidates with job requirements
* Generating match scores
* Providing hiring recommendations
* Saving structured reports

---

## Demo Video



---

## Author

Adithi A
B.Tech CSE (AI & ML)
Reva University

---

## License

This project is created for educational purposes.
