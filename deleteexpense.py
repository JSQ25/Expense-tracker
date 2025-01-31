def delete_expense(expenses):
    # Ask user
    category = input("Enter the category of the expense to delete: ").strip().lower
    date = input("Enter the date of the expense: ").strip().lower
     # Check category
    if category in expenses:
        expenses[category] = [expense for expense in expenses[category] if expense["date"] != date]
        # Remove category if no expenses left
        if not expenses[category]:
            del expenses[category]
            print(f"'{category}' removed because there are no more expenses.")
        else:
            print(f"Expense on {date} deleted.")
    else:
        print(f"'{category}' not found.")

    return expenses