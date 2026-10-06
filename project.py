class Contact:

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email


class ContactBook:

    def __init__(self):
        self.contacts = []

    # Add Contact
    def add_contact(self):

        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")

        contact = Contact(name, phone, email)

        self.contacts.append(contact)

        print("Contact added successfully!")

    # View Contacts
    def view_contacts(self):

        if len(self.contacts) == 0:
            print("No contacts found.")
            return

        print("\n===== CONTACTS =====")

        for contact in self.contacts:

            print("--------------------")
            print("Name:", contact.name)
            print("Phone:", contact.phone)
            print("Email:", contact.email)

    # Search Contact
    def search_contact(self):

        name = input("Enter name to search: ")

        found = False

        for contact in self.contacts:

            if contact.name.lower() == name.lower():

                print("--------------------")
                print("Name:", contact.name)
                print("Phone:", contact.phone)
                print("Email:", contact.email)

                found = True

        if found == False:
            print("Contact not found.")

    # Update Contact
    def update_contact(self):

        name = input("Enter name to update: ")

        for contact in self.contacts:

            if contact.name.lower() == name.lower():

                new_phone = input("Enter new phone number: ")
                new_email = input("Enter new email: ")

                contact.phone = new_phone
                contact.email = new_email

                print("Contact updated successfully!")

                return

        print("Contact not found.")

    # Delete Contact
    def delete_contact(self):

        name = input("Enter name to delete: ")

        for contact in self.contacts:

            if contact.name.lower() == name.lower():

                self.contacts.remove(contact)

                print("Contact deleted successfully!")

                return

        print("Contact not found.")

    # Save Contacts
    def save_contacts(self):

        with open("contacts.txt", "w") as file:

            for contact in self.contacts:

                file.write(
                    contact.name + "|" +
                    contact.phone + "|" +
                    contact.email + "\n"
                )

        print("Contacts saved successfully!")

    # Load Contacts
    def load_contacts(self):

        try:

            with open("contacts.txt", "r") as file:

                for line in file:

                    data = line.strip().split("|")

                    name = data[0]
                    phone = data[1]
                    email = data[2]

                    contact = Contact(name, phone, email)

                    self.contacts.append(contact)

        except FileNotFoundError:

            pass


# Menu
def menu():

    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Save Contacts")
    print("7. Exit")


# Create Contact Book
book = ContactBook()

# Load old contacts
book.load_contacts()


# Main Program
while True:

    menu()

    choice = input("Enter your choice: ")

    if choice == "1":

        book.add_contact()

    elif choice == "2":

        book.view_contacts()

    elif choice == "3":

        book.search_contact()

    elif choice == "4":

        book.update_contact()

    elif choice == "5":

        book.delete_contact()

    elif choice == "6":

        book.save_contacts()

    elif choice == "7":

        book.save_contacts()

        print("Thank you for using Contact Book!")

        break

    else:

        print("Invalid choice. Please try again.")1
        