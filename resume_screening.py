import os
import re
import json

class ResumeParser:
    def __init__(self, file_path):
        self.file_path = file_path
        self.text = ""

    def load_resume(self):
        with open(self.file_path, "r", encoding="utf-8") as file:
            self.text = file.read()

    def extract_name(self):
        match = re.search(r"Name:\s*(.*)", self.text)
        return match.group(1) if match else "Unknown"

    def extract_email(self):
        match = re.search(r"[\w\.-]+@[\w\.-]+", self.text)
        return match.group(0) if match else "Not found"

    def extract_skills(self):
        match = re.search(r"Skills:\s*(.*)", self.text)
        if match:
            return [skill.strip() for skill in match.group(1).split(",")]
        return []

    def extract_experience(self):
        match = re.search(r"(\d+)\s+years", self.text)
        return int(match.group(1)) if match else 0

    def parse(self):
        self.load_resume()
        return {
            "name": self.extract_name(),
            "email": self.extract_email(),
            "skills": self.extract_skills(),
            "experience": self.extract_experience()
        }

class JobMatcher:
    def __init__(self, job_file):
        with open(job_file, "r") as file:
            self.job = json.load(file)

    def calculate_score(self, resume):
        required = self.job["required_skills"]
        preferred = self.job["preferred_skills"]

        skill_matches = len(set(resume["skills"]) & set(required))
        preferred_matches = len(set(resume["skills"]) & set(preferred))

        skill_score = (skill_matches / len(required)) * 70
        preferred_score = (preferred_matches / len(preferred)) * 20 if preferred else 0

        exp_score = 10 if resume["experience"] >= self.job["min_experience"] else 5

        total = skill_score + preferred_score + exp_score
        return round(total, 2)

    def recommendation(self, score):
        if score >= 80:
            return "Highly Recommended"
        elif score >= 60:
            return "Recommended"
        elif score >= 40:
            return "Consider"
        else:
            return "Not Recommended"

class ReportGenerator:
    def __init__(self):
        self.results = []

    def add(self, resume, score, recommendation):
        self.results.append({
            "name": resume["name"],
            "email": resume["email"],
            "score": score,
            "recommendation": recommendation
        })

    def print_report(self):
        print("\n===== Resume Screening Report =====\n")
        for r in self.results:
            print("Name:", r["name"])
            print("Email:", r["email"])
            print("Match Score:", r["score"])
            print("Recommendation:", r["recommendation"])
            print("----------------------------")

    def save(self, filename):
        with open(filename, "w") as file:
            json.dump(self.results, file, indent=4)

def process_resumes(resume_folder, job_file, output_file):
    matcher = JobMatcher(job_file)
    report = ReportGenerator()

    for file in os.listdir(resume_folder):
        if file.endswith(".txt"):
            parser = ResumeParser(os.path.join(resume_folder, file))
            data = parser.parse()

            score = matcher.calculate_score(data)
            rec = matcher.recommendation(score)

            report.add(data, score, rec)

    report.print_report()
    report.save(output_file)

if __name__ == "__main__":
    process_resumes("resumes", "job_requirements.json", "results.json")