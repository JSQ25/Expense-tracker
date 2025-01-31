categories = {}

def addExpenses():
    while True:
        category_name = input("Enter category name: ").strip().lower()
        
        if category_name not in categories:
            categories[category_name] = []
        
        taga = input("date: ")
        tagb = input("money used: ")
        tagc = input("broke or not: ")

        new_entry = {"tag1": taga, "tag2": tagb, "tag3": tagc}
        
        # Append the dictionary to the category list
        categories[category_name].append(new_entry)
        
        # Display the categories and their entries
        print("\nCurrent data:")
        for category, entries in categories.items():
            print(f"Category: {category}")
            for i, entry in enumerate(entries, start=1):
                print(f"  {i}: {entry}")
        
        # Ask if the user wants to continue
        continue_input = input("\nDo you want to add more? (yes/no): ").strip().lower()
        if continue_input not in ["yes", "y"]:
            for category, entries in categories.items():
                print(f"Category: {category}")
                for i, entry in enumerate(entries, start=1):
                    print(f"  {i}: {entry}")
                    mainmenu()


def mainmenu():
    menuInput = input("Expense Tracker Menu:\n1. Add Expenses\n2. Exit")
    if menuInput == "1":
        addExpenses()
    if menuInput == "2":
        print('Cya next time')

mainmenu()
