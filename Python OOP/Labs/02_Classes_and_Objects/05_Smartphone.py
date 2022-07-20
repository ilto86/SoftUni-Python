'''
Teacher Solution
'''

# class Smartphone:
#     def __init__(self, memory: int):
#         self.memory = memory
#         self.memory_used = 0
#         self.apps = []
#         self.is_on = False
# 
#     def install(self, app: str, app_memory: int):
#         if not self.is_on:
#             return f"Turn on your phone to install {app}"
# 
#         if self.calculate_memory_left() < app_memory:
#             return f"Not enough memory to install {app}"
# 
#         self.apps.append(app)
#         self.memory_used += app_memory
#         return f"Installing {app}"
# 
#     def power(self):
#         self.is_on = not self.is_on
# 
#     def status(self):
#         total_apps_count = len(self.apps)
#         memory_left = self.calculate_memory_left()
#         return f"Total apps: {total_apps_count}. Memory left: {memory_left}"
# 
#     def calculate_memory_left(self):
#         return self.memory - self.memory_used

'''
My Solution
'''

class Smartphone:
    def __init__(self, memory: int):
        self.memory = memory
        self.apps = []
        self.is_on = False

    def power(self):
        # self.is_on = not self.is_on  # The teacher showed it to us today and say that is better than 'if statement'
        if not self.is_on:
            self.is_on = True

    def install(self, app: str, app_memory: int):
        if not self.is_on:
            return f"Turn on your phone to install {app}"

        if app_memory > self.memory:
            return f"Not enough memory to install {app}"

        self.apps.append(app)
        self.memory -= app_memory
        return f"Installing {app}"

    def status(self):
        return f"Total apps: {len(self.apps)}. Memory left: {self.memory}"


smartphone = Smartphone(100)
print(smartphone.install("Facebook", 60))
smartphone.power()
print(smartphone.install("Facebook", 60))
print(smartphone.install("Messenger", 20))
print(smartphone.install("Instagram", 40))
print(smartphone.status())