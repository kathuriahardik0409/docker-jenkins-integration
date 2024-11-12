import Book
from crypt import methods
from flask import Flask, render_template, request,abort,jsonify
import os

template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))
app = Flask(__name__, template_folder=template_dir)

# Creating Sample Book Objects and adding them to a list.
book1 = (1 , "Let us C" , "Yashavant Kanetkar" , 2000)
book2 = (2 , "abc" , "xyz" , 2019)

# A list that contains book objects
bookList = [book1 , book2]

# Home page for our web-app. This is the default route(/).
@app.route('/')
def welcome():
    return jsonify("Welcome to my website")

# Route that displays the books in the list.
@app.route('/books')
def books():
    return jsonify(bookList)


# Route that displays the details of book by a particular id. (/books/<int:book_id)
@app.route('/books/<int:book_id>')
def returnbookbyid(book_id):
    for book in bookList:
        if book[0] == book_id:

            return jsonify({
                "Id": book[0],
                "Name": book[1],
                "Author Name": book[2],
                "Year Published": book[3]
            })

    # If no book is found with the given ID, return 404
    abort(404)


# Route that adds a book to the books container.(/books/addBooks)
@app.route('/books/addBooks' , methods=['POST' , 'GET'])
def addBook():
    # If the request method is GET, we render a form where the user can enter the details of the new book to be added.
    if request.method == 'GET':
        return render_template("form.html")

    # If the request methods in POST, we get the details from the form, create a new book object and append it to the book container.
    elif request.method == 'POST':
        book_id = int(request.form['bookId'])
        book_name = request.form['bookName']
        author_name = request.form['authorName']
        year = int(request.form['year'])

        # Create a new book tuple
        new_book = (book_id, book_name, author_name, year)

        # Add the new book to the bookList
        bookList.append(new_book)

        # Return a confirmation message
        return f"Book '{book_name}' added successfully!"

    # For any other request method, we display an error message.
    else:
        return jsonify("Invalid request method.")


# Route to edit the details of a particular book with the given ID.(/books/editData/<int:book_id>)
@app.route('/books/editData/<int:book_id>', methods=['POST', 'GET'])
def loadeditbookinfoform(book_id):
    # Find the book by ID.
    book = next((book for book in bookList if book[0] == book_id), None)

    # If book not found, we return status code 404 which indicated not found.
    if book is None:
        abort(404)  # Book not found

    # If request methods is GET, we render a form/
    if request.method == 'GET':
        # Render the edit form with the book's current data
        return render_template("editData.html", book = book)

    # If request method is POST, we retrieve the details from the form and edit the information.
    else:
        # Update the book's details
        new_book_name = request.form['title']
        new_author_name = request.form['author']
        new_book_year = int(request.form['year'])

        bookList.remove(book)

        book = (book_id , new_book_name,new_author_name,new_book_year)
        bookList.append(book)

        return jsonify(f"Details for book with id:'{book_id}' have been updated successfully!! !")



# Route that deletes a book with the given ID from the container.
@app.route('/books/editData/delete/<int:book_id>', methods=['POST', 'GET'])
def deleteBookById(book_id):
    # Search for the book with the given ID.
    book = next((book for book in bookList if book[0] == book_id), None)

    # if book is not found, we return status code 404
    if book is None:
        abort(404)

    # else delete the book from the container.
    bookList.remove(book)
    return jsonify(f"Book with id:'{book_id}' deleted successfully!! !")


# Calling of the main function.
if __name__ == '__main__':
    app.run(debug = True)




