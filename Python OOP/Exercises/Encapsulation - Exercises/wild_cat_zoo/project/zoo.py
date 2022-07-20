from project.animal import Animal
from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price: float):
        if self.__budget < price:
            return "Not enough budget"
        if len(self.animals) == self.__animal_capacity:
            return "Not enough space for animal"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        if len(self.workers) == self.__workers_capacity:
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name: str):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        needed_salaries = sum(worker.salary for worker in self.workers)
        if needed_salaries > self.__budget:
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= needed_salaries
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        # needed_money = 0
        # for worker in self.workers:
        #     needed_money += worker.salary
        # if needed_money > self.__budget:
        #     return "You have no budget to pay your workers. They are unhappy"
        # self.__budget -= needed_money
        # return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        needed_care_money = sum(animal.money_for_care for animal in self.animals)
        if needed_care_money > self.__budget:
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= needed_care_money
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        # needed_money = 0
        # for animal in self.animals:
        #     needed_money += animal.money_for_care
        # if needed_money > self.__budget:
        #     return "You have no budget to tend the animals. They are unhappy."
        # self.__budget -= needed_money
        # return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    # def animals_status(self):
    #     result = f"You have {len(self.animals)} animals\n"
    #     result += self.__build_animal_str("Lion")
    #     result += self.__build_animal_str("Tiger")
    #     result += self.__build_animal_str("Cheetah")
    #     return result

    # def __build_animal_str(self, animal_type):
    #     # filtered = []
    #     # for animal in self.animals:
    #     #     if animal.__class__.__name__ == animal_type:
    #     #         filtered.append(animal)
    #     # result = f"----- {len(filtered)} {animal_type}s:\n"
    #     # for obj in filtered:
    #     #     result += repr(obj) + "\n"
    #     # return result
    #     counter = 0
    #     result = ""
    #     for animal in self.animals:
    #         if animal.__class__.__name__ == animal_type:
    #             counter += 1
    #             result += repr(animal) + "\n"
    #     return f"----- {counter} {animal_type}s:\n" + result

    # def animals_status(self):
    #     result = f"You have {len(self.animals)} animals\n"
    #     result += self.__build_entity_str(self.animals, "Lion")
    #     result += self.__build_entity_str(self.animals, "Tiger")
    #     result += self.__build_entity_str(self.animals, "Cheetah")
    #     return result.strip()

    # def workers_status(self):
    #     result = f"You have {len(self.workers)} workers\n"
    #     result += self.__build_entity_str(self.workers, "Keeper")
    #     result += self.__build_entity_str(self.workers, "Caretaker")
    #     result += self.__build_entity_str(self.workers, "Vet")
    #     return result.strip()

    # def __build_entity_str(self, entities, entity_type):
    #     counter = 0
    #     result = ""
    #     for entity in entities:
    #         if entity.__class__.__name__ == entity_type:
    #             counter += 1
    #             result += repr(entity) + "\n"
    #     return f"----- {counter} {entity_type}s:\n" + result



    def animals_status(self):
        result = f"You have {len(self.animals)} animals\n"
        lions = [repr(a) for a in self.animals if isinstance(a, Lion)]
        result += f"----- {len(lions)} Lions:\n" + "\n".join(lions) + "\n"
        tigers = [repr(a) for a in self.animals if isinstance(a, Tiger)]
        result += f"----- {len(tigers)} Tigers:\n" + "\n".join(tigers) + "\n"
        cheetahs = [repr(a) for a in self.animals if isinstance(a, Cheetah)]
        result += f"----- {len(cheetahs)} Cheetahs:\n" + "\n".join(cheetahs) + "\n"
        return result.strip()


    def workers_status(self):
        result = f"You have {len(self.workers)} workers\n"
        keepers = [repr(w) for w in self.workers if isinstance(w, Keeper)]
        result += f"----- {len(keepers)} Keepers:\n" + "\n".join(keepers) + "\n"
        caretakers = [repr(w) for w in self.workers if isinstance(w, Caretaker)]
        result += f"----- {len(caretakers)} Caretakers:\n" + "\n".join(caretakers) + "\n"
        vets = [repr(w) for w in self.workers if isinstance(w, Vet)]
        result += f"----- {len(vets)} Vets:\n" + "\n".join(vets) + "\n"
        return result.strip()