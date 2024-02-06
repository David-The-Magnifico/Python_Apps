import pytest
from phone_book import PhoneBook


def test_add_contact():
    phone_book = PhoneBook()
    contact_details = "First Name: David\nLast Name: Oladipo\nPhone Number: 07033529848\nAddress: Semicolon\nEmail: www.wealthydavid@gmail.com\nWorkplace: Semicolon.africa\nAddress of Workplace: 313, herbert macaulay way,sabo, yaba, lagos."
    phone_book.add_contact(contact_details)
    assert len(phone_book.contacts) == 1
    assert phone_book.contacts[0] == contact_details


def test_view_contacts(capsys):
    phone_book = PhoneBook()
    phone_book.view_contacts()
    captured = capsys.readouterr()
    assert "Phone book is empty" in captured.out


def test_edit_contact():
    phone_book = PhoneBook()
    contact_details = "First Name: David\nLast Name: Oladipo\nPhone Number: 07033529848\nAddress: Semicolon\nEmail: www.wealthydavid@gmail.com\nWorkplace: Semicolon.africa\nAddress of Workplace: 313, herbert macaulay way,sabo, yaba, lagos."
    new_contact_details = "First Name: John\nLast Name: Doe\nPhone Number: 08123576839\nAddress: Ibadan\nEmail: john@gmail.com\nWorkplace: ABC Inc\nAddress of Workplace: Callifornia, USA."
    phone_book.add_contact(contact_details)
    phone_book.edit_contact(contact_details, new_contact_details)
    assert new_contact_details in phone_book.contacts


def test_delete_contact():
    phone_book = PhoneBook()
    contact_details = "First Name: David\nLast Name: Oladipo\nPhone Number: 07033529848\nAddress: Semicolon\nEmail: www.wealthydavid@gmail.com\nWorkplace: Semicolon.africa\nAddress of Workplace: 313, herbert macaulay way,sabo, yaba, lagos."
    phone_book.add_contact(contact_details)
    phone_book.delete_contact(contact_details)
    assert len(phone_book.contacts) == 0
