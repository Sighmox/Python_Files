class Author:


    def __init__(self, name):
        self.name = name
        self.books = []

    def publish(self, title):
        self.books.append(title)

    def __str__(self):
        titles = ', '.join(self.books) or 'No Published Books'
        return f'{self.name}. Books: {titles}'

king = Author('Stephen King')
king.publish('It')
king.publish('Under the Dome')

print(king)
