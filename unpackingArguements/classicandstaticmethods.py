class Book:
    TYPES = ('Hardcover', 'Paperback')

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __str__(self):
        return f"Book is {self.name} weighs {self.weight} of {self.book_type}"

    @classmethod
    def hardcover(cls, name, page_weight):
        return Book(name, Book.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight):
        return Book(name, Book.TYPES[1], page_weight)


hard = Book.hardcover("five point some one", 1500)

light = Book.paperback("atomic habits", 600)

print(hard)
print(light)




