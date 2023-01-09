from app import db

class Author(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   first_name = db.Column(db.String(100), index=True)
   surname = db.Column(db.String(100), index=True)
   book = db.relationship("Book", backref="author", lazy="dynamic")

   def __str__(self):
       return f"<Author: {self.first_name} {self.surname}>"


class Book(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   title = db.Column(db.Text)
   description = db.Column(db.Text)
   author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
   shelf = db.relationship("Shelf", backref="book", lazy="dynamic")
   
   def __str__(self):
       return f"Title: {self.title} Description: {self.description[:50]} ...>"

class Shelf(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   status = db.Column(db.Boolean, unique=False, default=True)
   book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
   
   def __str__(self):
       return f">Position {self.book_id} status on shelf: {self.status}"