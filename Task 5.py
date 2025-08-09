# In-memory contact list
contacts = []

# Add a new contact
def add_contact():
    store = input("Store Name: ")
    phone = input("Phone Number: ")
    email = input("Email: ")
    address = input("Address: ")
    contacts.append({
        "store": store,
        "phone": phone,
        "email": email,
        "address": address
    })
    print("✅ Contact added successfully!")

# View all contacts
def view_contacts():
    if not contacts:
        print("No contacts found.")
        return
    print("\nContact List:")
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. {contact['store']} - {contact['phone']}")

# Search contact
def search_contact():
    query = input("Enter name or phone to search: ").lower()
    found = False
    for contact in contacts:
        if query in contact['store'].lower() or query in contact['phone']:
            print("\n🔍 Contact Found:")
            print(f"Store: {contact['store']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            found = True
    if not found:
        print("❌ Contact not found.")

# Update contact
def update_contact():
    phone = input("Enter phone number of contact to update: ")
    for contact in contacts:
        if contact['phone'] == phone:
            print("Leave blank to keep existing value.")
            contact['store'] = input(f"New Store Name ({contact['store']}): ") or contact['store']
            contact['phone'] = input(f"New Phone Number ({contact['phone']}): ") or contact['phone']
            contact['email'] = input(f"New Email ({contact['email']}): ") or contact['email']
            contact['address'] = input(f"New Address ({contact['address']}): ") or contact['address']
            print("✅ Contact updated successfully!")
            return
    print("❌ Contact not found.")

# Delete contact
def delete_contact():
    phone = input("Enter phone number of contact to delete: ")
    global contacts
    new_contacts = [c for c in contacts if c['phone'] != phone]
    if len(new_contacts) == len(contacts):
        print("❌ Contact not found.")
    else:
        contacts = new_contacts
        print("🗑️ Contact deleted successfully!")

# Menu
def main():
    while True:
        print("\n--- Contact Book ---")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option (1-6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("👋 Exiting Contact Book. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please select again.")

if __name__ == "__main__":
    main()
