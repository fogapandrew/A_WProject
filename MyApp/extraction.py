import requests
import MyApp.utils as utils


class GetRandomBook:
    def __init__(self):
        self.book_data = { }
 

    def get_random_book(self):
        
        book_title , created_date ,  publisher,  isbn , image = utils.random_boooks()

        # Store book data
        self.book_data = {
            "Title": book_title,
            "Created At": created_date,
            "Publisher": publisher,
            "ISBN": isbn,
            "Image": image
        }

        return book_title , created_date ,  publisher,  isbn , image
    


if __name__ == '__main__':
    stephen_book = GetRandomBook()

    title , book_created_date , book_publisher ,  book_isbn , book_image = stephen_book.get_random_book()

    # Display the book details
    print(f"Title: {title}")
    print(f"Created At: {book_created_date}")
    print(f"Publisher: {book_publisher}")
    print(f"ISBN: {book_isbn}")

    book_image.show()