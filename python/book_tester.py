from book import Book
books = []

with open("books.txt", "r") as file:
    for line in file:
        title, author, genre, is_checked_out = line.strip().split(",")
        if len (title = (title), author = (author), genre = (genre)) == 3:
            title, author, genre
            book = Book(title.strip(),author.strip(), genre.strip())
            book.append(book)
            print(book)

        first_book = books[0]
 
        print("Title:", first_book.get_title()) 
        print("Author:", first_book.get_author())
        print("Genre:", first_book.get_genre())
        print("Checked out:", first_book.is_checked_out)
       

    print("Checked out")
    first_book.check_out()
    print(first_book)

    print("Return book")
    first_book.return_book()
    print(first_book)

    