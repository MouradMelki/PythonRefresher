# student = {"name": "Rolf", "grades": (89, 90, 93, 78, 90)}

# def average(sequence):
#     return sum(sequence) / len(sequence)

# print(average(student["grades"]))

class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
    
    def average_grade(self):
        return sum(self.grades) / len(self.grades)

student1 = Student("Bob", (89, 90, 93, 78, 90))
student2 = Student("Rolf", (89, 90, 93, 78, 90))
# print(student1.name)
# print(student1.average_grade())
# print(student2.name)
# print(student2.average_grade())

class Store:
    def __init__(self, name):
        self.name = name
        self.items = []
        # You'll need 'name' as an argument to this method.
        # Then, initialise 'self.name' to be the argument, and 'self.items' to be an empty list.
    
    def add_item(self, name, price):
        # Create a dictionary with keys name and price, and append that to self.items.
        self.items.append({'name': name, 'price': price})
        print(self.items)

    def stock_price(self):
        return sum([item['price'] for item in self.items])
        # total = 0
        # for item in self.items:
        #     total += item["price"]
        # return total
        # Add together all item prices in self.items and return the total.

store1 = Store("MM")
store1.add_item("batata", 24)
store1.add_item("pomme", 30)
print(store1.stock_price())