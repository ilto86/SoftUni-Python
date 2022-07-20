from project.animal import Animal
from project.mammal import Mammal
from project.gorilla import Gorilla
from project.bear import Bear
from project.reptile import Reptile
from project.lizard import Lizard
from project.snake import Snake

mammal = Mammal("Stella")
print(mammal.__class__.__bases__[0].__name__)
print(mammal.name)
lizard = Lizard("John")
print(lizard.__class__.__bases__[0].__name__)
print(lizard.name)


'''Exception Output 
Animal
Stella
Reptile
John 
'''