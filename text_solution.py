# Name of Competition: Caribbean STEM Olympaids - Coding Level II - 2027
# Names of Participants: Khalia Lewis, L'amour Austin, Rachael Givians, Deshawn Jones

# Greet the user and introduce the application.
print("Welcome to Edu-Agro!")
print("Learn how to grow crops in a changing climate.")

# Keep displaying the menu until the user chooses to exit.
while True:
    print("\nWhat would you like to do?")
    print("1. Learn about climate-resilient farming")
    print("2. Find farming techniques for my farm")
    print("3. View weather updates and alerts")
    print("4. Ask the agricultural assistant")
    print("5. Play the farming game")
    print("6. Exit")

    # Get the user's choice.
    choice = input("\nEnter a number from 1 to 6: ").strip()
    # .strip() removes spaces from the beginning and end of text.
    # _________________________________________________________________________________________________________________________________

    # Guide the user to the selected feature.
    if choice == "1":
        print("\n--- Learn About Climate-Resilient Farming ---")
        print("1. Drip irrigation")
        print("2. Contour farming")
        print("3. Mulching")

        technique = input("Choose a technique: ").strip()

        if technique == "1":
            print("\nDrip irrigation delivers water slowly")
            print("near plant roots, helping reduce water waste.")

        elif technique == "2":
            print("\nContour farming involves planting along")
            print("the contours of sloping land to reduce soil erosion.")

        elif technique == "3":
            print("\nMulching involves covering the soil")
            print("to help retain moisture and reduce weed growth.")

        else:
            print("Invalid choice. Please select a listed technique.")
    # _________________________________________________________________________________________________________________________________

    elif choice == "2":
        print("\n--- My Farm ---")
        print("What crops do you grow on your farm?")
        print("1. Tomatoes")
        print("2. Lettuce")
        print("3. Carrots")

        crop_type = input("Choose the crop you grow: ").strip()

        if crop_type == "1":
            print("Drip Irrigation is best")
        elif crop_type == "1":
            print("Water Harvesting is best")
        elif crop_type == "1":
            print("Crop rotation is best")
        else:
            print("Please choose a valid number pleaseee")

        print("to help identify suitable farming techniques.")
    # _________________________________________________________________________________________________________________________________

    elif choice == "3":
        print("\n--- Weather Updates and Alerts ---")
        print("Live weather information is not connected yet.")
    # _________________________________________________________________________________________________________________________________

    elif choice == "4":
        print("\n--- Agricultural Assistant ---")
        print("The AI assistant is not connected yet.")
    # _________________________________________________________________________________________________________________________________

    elif choice == "5":
        print("\n--- Farming Game ---")
        print("Coming soon: plant crops and choose techniques")
        print("to help your virtual farm handle changing weather.")
    # _________________________________________________________________________________________________________________________________

    elif choice == "6":
        print("\nThank you for using Edu-Agro. Goodbye!")
        break  # Stop the loop and end the program.
    # _________________________________________________________________________________________________________________________________

    else:
        print("\nInvalid choice. Please enter a number from 1 to 6.")
