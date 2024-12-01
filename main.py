import json

# Read the input JSON file
with open("input.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Create a dictionary to store unique questions
unique_questions = {}
new_questions = []
counter = 1

# Process each question
for question in data:
    question_text = question["question"]

    # If we haven't seen this question before, add it
    if question_text not in unique_questions:
        unique_questions[question_text] = True
        new_questions.append(
            {
                "question_id": counter,
                "question": question_text,
                "correct_answer": question["correct_answer"],
            }
        )
        counter += 1

# Create the final output structure
output = {"questions": new_questions}

# Write to output file with proper Japanese character encoding
with open("karimen.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"Processed {len(data)} original questions")
print(f"Found {len(new_questions)} unique questions")
