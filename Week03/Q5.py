contacts = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-9999"
}

# Access a value
print(f"Alice's number: {contacts['Alice']}")

# Add a new contact
contacts["Diana"] = "555-4321"
print(f"Contacts after adding Diana: {contacts}")

# Update a contact
contacts["Bob"] = "555-0000"
print(f"Contacts after updating Bob: {contacts}")

# Delete a contact
del contacts["Charlie"]
print(f"Contacts after deleting Charlie: {contacts}")

# Display keys
print(f"All names: {contacts.keys()}")

# Length of dictionary
print(f"Total contacts: {len(contacts)}")
