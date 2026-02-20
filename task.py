def workout_generator():
    workouts = [ # Define a list of workout dictionaries, each containing a muscle group and its exercises
        {"leg": ["squats", "lunges", "deadlifts"], "sets": 2, "reps": 10},
        {"arm": ["bicep curls", "tricep dips", "push-ups"], "sets": 2, "reps": 12},
        {"core": ["russian twists", "sit-ups", "leg raises"], "sets": 3, "reps": 15},
    ]
    return workouts
workouts = workout_generator() # Call the function to get the initial workouts
workouts.append({"cardio": ["running", "cycling", "swimming"], "minutes": 30}) # Add an additional workout category to the list
weights = [10, 15, 20] # Define a list of weights for the exercises

while True:  # repeat the whole workout selection process
    workout_choice = input("Which workout do you want to do? ") 
    print(f"You chose: {workout_choice}")

    for workout in workouts:
        if workout_choice in workout:
            print(f"Here are your {workout_choice} exercises: {workout[workout_choice]}") # Show the exercises for the chosen workout
            exercise_choice = input(f"Which exercise do you want to do in {workout_choice}? ")
            print(f"Exercise chosen: {exercise_choice}") 
            if workout_choice != "cardio":  # Only ask for weights if it's not a cardio workout
                weight_choice = input(f"Which weight do you want to use? {weights} ")
                if weight_choice == None or weight_choice == "":  # Check if the user did not select a weight
                    print("No weight selected. Defaulting to 0 kg.") # If no weight is selected, default to 0 kg
                    weight_choice = 0
                print(f"You chose to use {weight_choice} kg for your workout.")
            if workout_choice == "cardio":  # If it's a cardio workout, show the minutes instead of sets and reps
                print(f"You will do {workout['minutes']} minutes of {exercise_choice}.")
            else:
                print(f"Number of sets: {workout['sets']}") # Show the number of sets for the chosen workout
                print(f"Number of reps: {workout['reps']}")  # Show the number of reps for the chosen workout
            another_workout = input("Would you like to do another workout? (yes/no) ") # Ask the user if they want to do another workout after showing the details of the current workout

            if another_workout.lower() == "yes":
                break  # break out of the for-loop, but stay in the while-loop
            else:
                print("The workout you chose is:", exercise_choice) # After the loop, show the final exercise the user selected
                print("Enjoy your workout!")
                exit()  # exit the program if the user does not want to do another workout
                break  # break out of the for-loop after exiting the program

    else:
        print("Sorry, that workout is not available.") # This runs only if the loop completes without finding a matching workout
