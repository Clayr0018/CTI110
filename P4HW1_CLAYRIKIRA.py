# Rikira Clay
# April 14, 2025
# P4HW1 – Score Loop with Validation and Letter Grade
# This program asks the user how many test scores they want to enter,
# then collects valid scores using loops. It removes the lowest score,
# calculates the average of the rest, and prints a letter grade.

# Pseudocode:
# 1. Ask the user how many scores they want to enter
# 2. Use a loop to ask for each score
#    - Check if the score is between 0 and 100
#    - If not, show error and ask again
#    - If valid, add it to a list
# 3. After collecting all scores:
#    - Find and display the lowest score
#    - Remove the lowest score from the list
#    - Calculate average of the modified list
#    - Determine and display letter grade based on average

# Step 1: Ask for number of scores
num_scores = int(input("How many scores do you want to enter? "))

# Step 2: Collect valid scores in a list
scores = []
score_count = 1

while len(scores) < num_scores:
    score = float(input("Enter score #" + str(score_count) + ": "))

    if score < 0 or score > 100:
        print("INVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        print("Enter score #" + str(score_count) + " again:")
    else:
        scores.append(score)
        score_count = score_count + 1

# Step 3: Process scores
lowest = min(scores)
scores.remove(lowest)
average = sum(scores) / len(scores)

# Step 4: Determine letter grade
if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

# Step 5: Output results
print("\n---------- Results ----------")
print("Lowest Score  :", lowest)
print("Modified List :", scores)
print("Scores Average:", format(average, ".2f"))
print("Grade         :", grade)
print("-----------------------------")
