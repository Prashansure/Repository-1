# ISSUE 51
#
# Problem:
# Write a program that accepts a list of contacts containing names and phone numbers and allows searching, updating and deleting contacts using functions.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def find_contact(contacts, name):
    # TODO: Check whether names are compared consistently.
    for contact in contacts:
        if contact["name"] == name.lower():
            return contact
    return None

def update_contact(contacts, name, phone):
    contact = find_contact(contacts, name)
    # TODO: Check how the replacement phone number is used.
    if contact:
        contact["phone"] = name
    return contacts

def delete_contact(contacts, name):
    # TODO: Check which matching contact should remain in the list.
    return [contact for contact in contacts if contact["name"] == name]

def check_solution():
    contacts = [{"name":"Ava","phone":"111"},{"name":"Ben","phone":"222"}]
    assert find_contact(contacts,"Ava") == {"name":"Ava","phone":"111"}
    assert update_contact(contacts,"Ben","333")[1]["phone"] == "333"
    assert delete_contact(contacts,"Ava") == [{"name":"Ben","phone":"333"}]

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
