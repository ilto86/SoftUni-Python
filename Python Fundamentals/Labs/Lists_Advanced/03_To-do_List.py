# todo = ["" for i in range(11)]
#
# command = input()
#
# while command != "End":
#     explode = command.split("-")
#     priority = int(explode[0])
#     task = explode[1]
#     # todo.pop(priority)
#     # todo.insert(priority, task)
#     todo[priority] = task
#     command = input()
#
# final_todo = [task for task in todo if task != ""]
#
# print(final_todo)

to_do_notes = ["" for x in range(11)]
command = input()

while command != "End":
    current_command = command.split("-")
    importance = int(current_command[0])
    note = current_command[1]
    to_do_notes[importance] = note
    command = input()

final_to_do_notes = [note for note in to_do_notes if note != ""]
print(final_to_do_notes)
