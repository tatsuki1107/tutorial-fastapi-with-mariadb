from database import SessionLocal
from models import Book, User

db = SessionLocal()


def seed():
    book_titles = [
      "施策デザインのための機械学習入門"
    ]
    books = [Book(title=title) for title in book_titles]

    user = User(username='tatsuki')
    user.books = books  # リレーションも丸ごと表現できる

    db.add(user)
    db.commit()


if __name__ == '__main__':
    seed()
