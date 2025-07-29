class Animal:
    
    def __init__(self, name):
        self.name = name
        
    def __repr__(self):
        return f'Anime name: {self.name}'


if __name__ == '__main__':
    cat1 = Animal('lucy')
    print(repr(cat1))