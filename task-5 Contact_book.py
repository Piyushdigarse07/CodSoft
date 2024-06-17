class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Address: {self.address}"

class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self):
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        contact = Contact(name, phone, email, address)
        self.contacts[phone] = contact
        print("Contact added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
            return
        for phone, contact in self.contacts.items():
            print(contact)

    def search_contact(self):
        search_term = input("Enter name or phone number to search: ")
        found = False
        for phone, contact in self.contacts.items():
            if search_term in contact.name or search_term in phone:
                print(contact)
                found = True
        if not found:
            print("No contact found.")

    def update_contact(self):
        phone = input("Enter the phone number of the contact to update: ")
        if phone in self.contacts:
            name = input("Enter new name: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")
            contact = self.contacts[phone]
            contact.name = name
            contact.email = email
            contact.address = address
            print("Contact updated successfully.")
        else:
            print("Contact not found.")

    def delete_contact(self):
        phone = input("Enter the phone number of the contact to delete: ")
        if phone in self.contacts:
            del self.contacts[phone]
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")

def main():
    manager = ContactManager()

    while True:
        print("\n1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            manager.add_contact()
        elif choice == '2':
            manager.view_contacts()
        elif choice == '3':
            manager.search_contact()
        elif choice == '4':
            manager.update_contact()
        elif choice == '5':
            manager.delete_contact()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
