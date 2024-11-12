import requests
#import MyApp.utils as utils
import utils


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
    

class GetRandomBookScapper:

    def __init__(self):
        self.random_book = {}

    def add_data_db(self):

        utils.add_data_to_database()

    def get_data_db(self):

        dictionary_random_book = utils.get_random_books()

        #Store book data
        self.random_book = {
            "Title": dictionary_random_book['title'],
            "Publisher": dictionary_random_book['authors'],
            "ratings": dictionary_random_book['ratings'],
            "Image": dictionary_random_book['image_url']
        }

        return dictionary_random_book

    

if __name__ == '__main__':


    # stephen_book = GetRandomBook()

    book1 = GetRandomBookScapper()

    book1.add_data_db()

    data = book1.get_data_db()

    if book1:
        print(f"Image URL: {data['image_url']}")
        print(f"Title: {data['title']}")
        print(f"Authors: {data['authors']}")
        print(f"Ratings: {data['ratings']}")

    else:
        print('no book found in records...')

    # title , book_created_date , book_publisher ,  book_isbn , book_image = stephen_book.get_random_book()

    # Display the book details
    # print(f"Title: {title}")
    # print(f"Created At: {book_created_date}")
    # print(f"Publisher: {book_publisher}")
    # print(f"ISBN: {book_isbn}")

    # book_image.show()