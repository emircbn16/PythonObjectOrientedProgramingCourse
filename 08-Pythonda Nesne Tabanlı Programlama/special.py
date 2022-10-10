mylist = [1,2,3]
# myString = 'My String'

# print(len(mylist))
# print(len(myString))
# print(type(mylist))
# print(type(myString))

class Movie():
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration
        print('Movie Objesi Oluşturuldu.')
    
    def __str__(self):
        return f"{self.title} By {self.director}"
    
    def __len__(self):
        return self.duration

    def __del__(self):
        print('Film Silindi')
m = Movie('Film Adı','Yönetmen Adı',120)

# print(str(mylist))
# print(str(m))
# print(len(mylist))
# print(len(m))