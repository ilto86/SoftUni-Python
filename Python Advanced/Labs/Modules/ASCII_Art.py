from pyfiglet import figlet_format
from termcolor import colored, cprint

print(
    figlet_format("Python", font="isometric1")
)

print(
    figlet_format("ILTO", font="isometric1")
)

print(
    figlet_format('Doncho', font="isometric1")
)

print(
    colored("Doncho", 'green', attrs=['bold'])
)

print(
    colored("Doncho", 'green', attrs=['underline'])
)

print(
    colored("Doncho", 'green', attrs=['underline', 'bold'])
)

text = colored("Doncho", 'green', attrs=['underline', 'bold'])

print(
    figlet_format(
        text,
        font="isometric1"
    )
)

text = colored('Hello, World!', 'blue', attrs=['reverse', 'blink'])
print(text)
cprint('Hello, World!', 'red', 'on_yellow')