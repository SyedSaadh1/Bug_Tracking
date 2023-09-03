import random

# Simulated bug reports as dictionaries with description
bug_reports = [
    {"id": 1, "description": "UI button color is incorrect"},
    {"id": 2, "description": "Application crashes when clicking on 'Submit'"},
    {"id": 3, "description": "Performance issue during data retrieval"},
    # Add more bug reports here
]

# Keywords to determine the assignment
keywords_to_developer = {
    "UI": "DeveloperA",
    "crashes": "DeveloperB",
    "Performance": "DeveloperC",
}

def assign_bug_to_developer(bug_report):
    # Look for keywords in the bug report description
    for keyword, developer in keywords_to_developer.items():
        if keyword.lower() in bug_report["description"].lower():
            return developer
    # If no keyword matches, assign to a random developer
    return random.choice(list(keywords_to_developer.values()))

def main():
    for bug_report in bug_reports:
        assigned_developer = assign_bug_to_developer(bug_report)
        print(f"Bug ID {bug_report['id']} assigned to {assigned_developer}")

if __name__ == "__main__":
    main()
