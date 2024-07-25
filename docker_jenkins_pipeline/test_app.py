import unittest
import json
import requests

BASE_URL = "http://localhost:8000"

class TestBookAPI(unittest.TestCase):
    def test_create_book(self):
        book_data = {"title": "Test Book", "author": "Test Author"}
        response = requests.post(f"{BASE_URL}/books", json=book_data)
        self.assertEqual(response.status_code, 201)
        self.assertIn("id", response.json())

    def test_get_books(self):
        response = requests.get(f"{BASE_URL}/books")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_get_book(self):
        # First, create a book
        book_data = {"title": "Test Book", "author": "Test Author"}
        create_response = requests.post(f"{BASE_URL}/books", json=book_data)
        book_id = create_response.json()["id"]

        # Then, get the book
        response = requests.get(f"{BASE_URL}/books/{book_id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["title"], "Test Book")

    def test_update_book(self):
        # First, create a book
        book_data = {"title": "Test Book", "author": "Test Author"}
        create_response = requests.post(f"{BASE_URL}/books", json=book_data)
        book_id = create_response.json()["id"]

        # Then, update the book
        updated_data = {"title": "Updated Test Book"}
        response = requests.put(f"{BASE_URL}/books/{book_id}", json=updated_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["title"], "Updated Test Book")

    def test_delete_book(self):
        # First, create a book
        book_data = {"title": "Test Book", "author": "Test Author"}
        create_response = requests.post(f"{BASE_URL}/books", json=book_data)
        book_id = create_response.json()["id"]

        # Then, delete the book
        response = requests.delete(f"{BASE_URL}/books/{book_id}")
        self.assertEqual(response.status_code, 200)

        # Verify the book is deleted
        get_response = requests.get(f"{BASE_URL}/books/{book_id}")
        self.assertEqual(get_response.status_code, 404)

if __name__ == '__main__':
    unittest.main()


