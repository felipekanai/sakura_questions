import csv
import json


def convert_json_to_csv(json_file, csv_file):
    """
    Convert a JSON file to a CSV file.

    Args:
        json_file (str): Path to the input JSON file.
        csv_file (str): Path to the output CSV file.
    """
    with open(json_file, "r") as f:
        data = json.load(f)

    questions = data["questions"]

    with open(csv_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["question_id", "question", "correct_answer"])

        for question in questions:
            writer.writerow(
                [
                    question["question_id"],
                    question["question"],
                    str(question["correct_answer"]),
                ]
            )


# Example usage
convert_json_to_csv("karimen.json", "output.csv")
