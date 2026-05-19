# ==================================================
# AI ASSISTANT FOR AIRCRAFT MAINTENANCE
# Advanced Student Version
# ==================================================

import datetime


print("     AI ASSISTANT FOR AIRCRAFT MAINTENANCE")

# Aircraft Maintenance Knowledge Base

maintenance_database = {

    "engine": {
        "keywords": ["overheat", "temperature", "smoke", "engine"],
        "severity": "HIGH",
        "solutions": [
            "Inspect turbine airflow",
            "Check lubrication system",
            "Verify cooling mechanism",
            "Perform engine diagnostics"
        ]
    },

    "fuel": {
        "keywords": ["fuel", "pressure", "leak"],
        "severity": "HIGH",
        "solutions": [
            "Inspect fuel pump",
            "Check fuel lines",
            "Verify pressure valves",
            "Inspect leakage points"
        ]
    },

    "battery": {
        "keywords": ["battery", "power", "voltage"],
        "severity": "MEDIUM",
        "solutions": [
            "Inspect battery terminals",
            "Check charging system",
            "Replace damaged battery",
            "Test voltage stability"
        ]
    },

    "landing gear": {
        "keywords": ["gear", "landing", "hydraulic"],
        "severity": "HIGH",
        "solutions": [
            "Inspect hydraulic system",
            "Check actuator alignment",
            "Verify landing gear sensors"
        ]
    },

    "navigation": {
        "keywords": ["navigation", "gps", "sensor", "radar"],
        "severity": "MEDIUM",
        "solutions": [
            "Restart navigation module",
            "Check sensor calibration",
            "Update navigation software"
        ]
    },

    "brakes": {
        "keywords": ["brake", "stopping"],
        "severity": "HIGH",
        "solutions": [
            "Inspect brake pads",
            "Verify hydraulic pressure",
            "Check brake fluid levels"
        ]
    }
}


# ==================================================
# Function to Analyze Issue
# ==================================================

def analyze_issue(user_issue):

    user_issue = user_issue.lower()

    for system, data in maintenance_database.items():

        for keyword in data["keywords"]:

            if keyword in user_issue:

                return {
                    "system": system,
                    "severity": data["severity"],
                    "solutions": data["solutions"]
                }

    return None


# ==================================================
# Maintenance Log File
# ==================================================

log_file = "maintenance_log.txt"


# ==================================================
# Main Program Loop
# ==================================================

while True:

    print("\nExample Issues:")
    print("- Engine overheating detected")
    print("- Fuel pressure leak")
    print("- Battery voltage failure")
    print("- Navigation sensor issue")

    user_input = input("\nEnter Aircraft Issue (or type 'exit'): ")

    if user_input.lower() == "exit":

        print("\nClosing AI Maintenance Assistant...")
        print("Session Ended.")
        break

    result = analyze_issue(user_input)

    current_time = datetime.datetime.now()

    if result:

        print("\n================================================")
        print("         AIRCRAFT MAINTENANCE REPORT")
        print("================================================")

        print(f"Detected System : {result['system'].upper()}")
        print(f"Severity Level  : {result['severity']}")

        print("\nRecommended Actions:")

        for index, solution in enumerate(result["solutions"], start=1):
            print(f"{index}. {solution}")

        # Save logs
        with open(log_file, "a") as file:

            file.write(f"\nTime: {current_time}")
            file.write(f"\nIssue: {user_input}")
            file.write(f"\nDetected System: {result['system']}")
            file.write(f"\nSeverity: {result['severity']}")
            file.write("\n-----------------------------------")

        print("\nMaintenance report saved successfully.")

    else:

        print("\nIssue not recognized.")
        print("Please consult aircraft maintenance personnel.")