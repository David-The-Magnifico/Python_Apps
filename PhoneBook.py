class PhoneBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact_details):
        self.contacts.append(contact_details)
        self.contacts.sort()
        print("Contact added successfully")

    def view_contacts(self):
        if not self.contacts:
            print("Phone book is empty")
        else:
            print("Contacts in the phone book:")
            for contact in self.contacts:
                print(contact)

    def edit_contact(self, old_contact, new_contact):
        if old_contact in self.contacts:
            index = self.contacts.index(old_contact)
            self.contacts[index] = new_contact
            print("Contact edited successfully")
        else:
            print("Contact not found")

    def delete_contact(self, contact):
        if contact in self.contacts:
            self.contacts.remove(contact)
            print("Contact deleted successfully")
        else:
            print("Contact not found")

def main():
    phone_book = PhoneBook()

    while True:
        print("\nPhone Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("\nEnter contact details:")
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            phone_number = input("Phone Number: ")
            address = input("Address: ")
            email = input("Email: ")
            workplace = input("Workplace: ")
            workplace_address = input("Address of Workplace: ")

            contact_details = (
                f"First Name: {first_name}\n"
                f"Last Name: {last_name}\n"
                f"Phone Number: {phone_number}\n"
                f"Address: {address}\n"
                f"Email: {email}\n"
                f"Workplace: {workplace}\n"
                f"Address of Workplace: {workplace_address}"
            )
            phone_book.add_contact(contact_details)

        elif choice == 2:
            phone_book.view_contacts()

        elif choice == 3:
            contact_to_edit = input("Enter the name of the contact to edit: ")
            if contact_to_edit in phone_book.contacts:
                print("Enter new contact details:")
                new_first_name = input("First Name: ")
                new_last_name = input("Last Name: ")
                new_phone_number = input("Phone Number: ")
                new_address = input("Address: ")
                new_email = input("Email: ")
                new_workplace = input("Workplace: ")
                new_workplace_address = input("Address of Workplace: ")

                new_contact_details = (
                    f"First Name: {new_first_name}\n"
                    f"Last Name: {new_last_name}\n"
                    f"Phone Number: {new_phone_number}\n"
                    f"Address: {new_address}\n"
                    f"Email: {new_email}\n"
                    f"Workplace: {new_workplace}\n"
                    f"Address of Workplace: {new_workplace_address}"
                )
                phone_book.edit_contact(contact_to_edit, new_contact_details)
            else:
                print("Contact not found")

        elif choice == 4:
            contact_to_delete = input("Enter the name of the contact to delete: ")
            phone_book.delete_contact(contact_to_delete)

        elif choice == 5:
            print("Exiting...")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
