from flask import Flask, request, render_template ,jsonify

app = Flask(__name__)



books = [
    {"id": 1, "title": "Harry Potter and the Sorcerer's Stone", "author": "J.K. Rowling", "year": 1997},
    {"id": 2, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
    {"id": 3, "title": "1984", "author": "George Orwell", "year": 1949},
    {"id": 4, "title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
    {"id": 5, "title": "A Promised Land", "author": "Barack Obama", "year": 2020},
]

@app.route('/', methods=['GET'])
def index():
	return render_template("indexx.html")

@app.route('/search', methods=['GET'])
def search():

    autorfromSearch = request.args.get('author')
    print(autorfromSearch)
    exist = False

    for livre in books:
        if livre['author'] == autorfromSearch:
            exist = True
            # Correction de la syntaxe ici
            return f"Livre : {livre['title']} ({livre['year']})"
        


         
    if exist == False:
         return "aucun livre trouve"
         
        
@app.route('/add_book', methods=['POST'])
def add_book():
    # Extraire les données du formulaire
    title = request.form.get('title')
    author = request.form.get('author')
    annee = request.form.get('year')

    try:
        annee = int(annee)  # Convertir en entier pour éviter une erreur de type
    except ValueError:
        return "L'année doit être un entier valide", 400

    books.append(
        {"id": len(books) + 1, "title": title, "author": author, "year": annee}
    )

    return f'titre: {title} / auteur: {author} / annee: {annee}'





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)