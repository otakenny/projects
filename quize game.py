quiz_questions = [
    {"question": "How many continents are there on Earth?", "answer": "7"},
    {"question": "How many sides does a hexagon have?", "answer": "6"},
    {"question": "Who was the first person to walk on the moon?", "answer": "Neil Armstrong"},
    {"question": "Who wrote 'Romeo and Juliet'?", "answer": "Shakespeare"},
    {"question": "What is the largest ocean on Earth?", "answer": "Pacific Ocean"}
]

score = 0  # Initialize score

# Loop through the questions
for q in quiz_questions:
    user_answer = input(q["question"] + " ").strip().lower()  # Take user input (case insensitive)
    correct_answer = q["answer"].strip().lower()  # Convert correct answer to lowercase
    
    if user_answer == correct_answer:  # Compare both in lowercase
        print("Correct!\n")
        score += 1  # Increase score for correct answers
    else:
        print(f"Wrong! The correct answer is: {q['answer']}\n")  # Show correct answer

# Display final score
print(f"Quiz Over! Your final score is {score} out of {len(quiz_questions)}.")

