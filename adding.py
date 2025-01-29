# Initialize an empty list to store the dictionaries
data_list = []

while True:
    # Ask the user for input
    taga = input("date: ")
    tagb = input("money wasted: ")
    tagc = input("broke or not: ")

    # Create a dictionary with the input
    new_entry = {"tag1": taga, "tag2": tagb, "tag3": tagc}
    
    # Append the dictionary to the list
    data_list.append(new_entry)
    
    # Display the list so far
    print("\nCurrent list of entries:")
    for i, entry in enumerate(data_list, start=1):
        print(f"{i}: {entry}")
    
    # Ask if the user wants to continue
    continue_input = input("\nDo you want to add more? (yes/no): ").strip().lower()
    if continue_input not in ["yes", "y"]:
        print("\nExiting the program. Final list:")
        for i, entry in enumerate(data_list, start=1):
            print(f"{i}: {entry}")
        break
