import json


def fix_question_ids(input_file, output_file):
    # Read the JSON file
    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Get the questions array
    questions = data["questions"]

    # Sort questions by their current question_id to maintain relative order
    questions.sort(key=lambda x: x["question_id"])

    # Update question_ids to be sequential starting from 1
    for idx, question in enumerate(questions, 1):
        question["question_id"] = idx

    # Create the output JSON with the fixed question_ids
    output_data = {"questions": questions}

    # Write the updated JSON to a new file
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)

    print(f"Successfully processed {len(questions)} questions.")
    print(f"Output written to: {output_file}")


# Example usage6
if __name__ == "__main__":
    input_file = "input.json"
    output_file = "karimen.json"
    fix_question_ids(input_file, output_file)
