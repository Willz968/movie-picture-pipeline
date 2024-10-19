while True:
    user_input = input("Enter 'stop' to end the loop: ").strip().lower()
    
    if user_input == "stop":
        print("Ending the loop.")
        break
    else:
        print("You didn't enter 'stop'. Loop continues.")
