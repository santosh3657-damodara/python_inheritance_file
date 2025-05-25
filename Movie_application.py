class Movie:
    def __init__(self,title,hero,heroine):
        self.tile=title
        self.hero=hero
        self.heroine=heroine
    def info(self):
        print('movie name:',self.tile)
        print('hero name:',self.hero)
        print('heroine name:',self.heroine)
        
list_of_movies=[]
while True:
    title=input('enter hero name:')
    heroine=input('enter heroine name:')
    hero=input('enter title name:')
    m=Movie(title,hero,heroine)
    list_of_movies.append(m)
    print('Movie name add in list successfully')
    option=input('do you want to add another movie [yes|no]:')
    if option.lower =='no':
       break
   
print('all movies information :')
for movie in list_of_movies:
    movie.info()
    print()
