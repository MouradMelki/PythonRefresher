# class ClassTest:
#     def instance_method(self): # to produce the action that uses the data inside a python object
#         print(f"Called instance_method of {self}")
    
#     @classmethod
#     def class_method(cls): # they are used as factories
#         print(f"Called class_methes of {cls}")

#     @staticmethod
#     def static_method(): # they are used to place a method insid a class
#         print("Called static_method.")
    
# test = ClassTest()
# test.instance_method()
# ClassTest.instance_method(test)

# ClassTest.class_method()

# ClassTest.static_method()

class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name: str, book_type: str, weight: int):
        self.name = name
        self.book_type = book_type
        self.weight = weight
    
    def __repr__(self) -> str:
        return f"<Book {self.name}, {self.book_type}, weighting {self.weight}g>"
    
    @classmethod
    def hardcover(cls, name, page_weight) -> "Book":
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight) -> "Book":
        return cls(name, cls.TYPES[1], page_weight)

book1 = Book("Harry Poter", "comic book", 1500)
book2 = Book.hardcover("Harry Poter", 1400)
book3 = Book.paperback("Harry Poter", 1300)

print(book1)
print(book2)
print(book3)