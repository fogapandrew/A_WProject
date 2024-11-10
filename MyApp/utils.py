import requests
import json
from PIL import Image
import random
from io import BytesIO

STEPHEN_KING_IMAGES = { 
    "Carrie" : "https://m.media-amazon.com/images/I/51l0k7AjWwL._AC_UF894,1000_QL80_.jpg",
    "Salem's Lot" : "https://upload.wikimedia.org/wikipedia/commons/6/61/%27Salem%27s_Lot_%281975%29_front_cover%2C_first_edition.jpg",
    "The Shining" : "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1353277730i/11588.jpg",
    "Rage" : "https://upload.wikimedia.org/wikipedia/commons/a/af/Rage_%281977%29_front_cover%2C_first_edition.jpg",
    "The Stand" : "https://preview.redd.it/t4hd5oiz691z.jpg?auto=webp&s=1769357b49cfef10eacf9b3e7238f1a9f09b39d2",
    "The Long Walk" : "https://m.media-amazon.com/images/I/81cW2xNlv8L._AC_UF894,1000_QL80_.jpg", 
    "The Dead Zone" : "https://www.worldofbooks.com/cdn/shop/files/0751504327.jpg?v=1718320775&width=493",
    "Firestarter" : "https://upload.wikimedia.org/wikipedia/commons/f/fa/Firestarter_%281980%29_front_cover%2C_first_edition.jpg",
    "Roadwork" : "https://m.media-amazon.com/images/I/71QPyCqbkRL._AC_UF894,1000_QL80_.jpg",
    "Cujo" : "https://m.media-amazon.com/images/I/81UaFdZ62YL._AC_UF1000,1000_QL80_.jpg",
    "The Running Man" : "https://m.media-amazon.com/images/I/81haz9evhgL._UF1000,1000_QL80_.jpg",
    "The Dark Tower: The Gunslinger" : "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSwr4Y795qM_UqEOTgiTnItmj_L5qbUpPv4hA&s",
    "Christine" : "https://d28hgpri8am2if.cloudfront.net/book_images/onix/cvr9781668018071/christine-9781668018071_hr.jpg",
    "Pet Sematary" : "https://upload.wikimedia.org/wikipedia/commons/2/24/Pet_Sematary_%281983%29_front_cover%2C_first_edition.jpg",
    "Cycle of the Werewolf" : "https://m.media-amazon.com/images/I/91e9h1qY7lL._AC_UF894,1000_QL80_.jpg",
    "The Talisman" : "https://m.media-amazon.com/images/I/91472Kz5CDL.jpg",
    "The Eyes of the Dragon" : "https://i0.wp.com/www.stephenkingrevisited.com/wp-content/uploads/2016/06/the-eyes-of-the-dragon.jpg?fit=802%2C1200&ssl=1",
    "Thinner" : "https://m.media-amazon.com/images/I/714Et2jsqAL._AC_UF894,1000_QL80_.jpg",
    "It" : "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1334416842i/830502.jpg",
    "The Dark Tower II: The Drawing of the Three" : "https://m.media-amazon.com/images/I/91PHYFSBgfL.jpg"
}

def random_boooks():
    """ This methods generates random books from stephen-king API.
    
    Parameters:
            NONE
    Returns:
         books['data']["Title"] (str) : a  string
         books['data']["created_at"] (DATETIME) : a date time 
         books['data']["Publisher"]  (str) : a string
         books['data']["ISBN"] (int) = a number
         image_resized (long)  = an image
         
    """
    
    global  STEPHEN_KING_IMAGES
    
    book_number = random.randint(1, 20)

    size = (200, 300)
   
    response = requests.get("https://stephen-king-api.onrender.com/api/book/{}".format(book_number))

    data = response.text 

    books = json.loads(data)

    for booktittle , bookimage in STEPHEN_KING_IMAGES.items():
        if booktittle == books['data']["Title"] :
            bookImage = bookimage
            
    image = Image.open(requests.get(bookImage, stream=True).raw)

    image_resized = image.resize(size)
    
    
    return books['data']["Title"] , books['data']["created_at"], books['data']["Publisher"] , books['data']["ISBN"] , image_resized