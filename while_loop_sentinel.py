# MARKJOHN OBIAS
# Week 04 - Looping Statements
# Laboratory # 15 - Guided Coding Exercise: while Loop for User Input with a Sentinel Value

total_sum = 0

while True:
    user_input = input("Enter a number (or 'stop' to finish): ")

    if user_input.strip().lower() == "stop":
        break  # Exit the loop

    try:
        number = float(user_input)
        total_sum += number
    except ValueError:
        print("Invalid input. Please enter a numeric value or 'stop'.")
        continue  # Allow the user to try again

print("The total sum is:", total_sum)
