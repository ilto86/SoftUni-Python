# class Hotel:
#     def __init__(self, name: str):
#         self.name = name
#         self.rooms = []
#
#     @property
#     def guests(self):
#         return sum([r.guests for r in self.rooms])
#
#     @classmethod
#     def from_stars(cls, stars_count: int):
#         return cls(f"{stars_count} stars Hotel")
#
#     def add_room(self, room):
#         self.rooms.append(room)
#
#     def take_room(self, room_number: int, people: int):
#         room = [r for r in self.rooms if r.number == room_number][0]
#         return room.take_room(people)
#
#     def free_room(self, room_number: int):
#         room = [r for r in self.rooms if r.number == room_number][0]
#         return room.free_room()
#
#     def status(self):
#         free_rooms = [str(room.number) for room in self.rooms if not room.is_taken]
#         taken_rooms = [str(room.number) for room in self.rooms if room.is_taken]
#
#         return f"Hotel {self.name} has {self.guests} total guests\n" \
#                f"Free rooms: {', '.join(free_rooms)}\n" \
#                f"Taken rooms: {', '.join(taken_rooms)}"


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    # @property
    # def guests(self):
    #     return sum([r.guests for r in self.rooms])

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number: int, people: int):
        room = [r for r in self.rooms if r.number == room_number][0]
        self.guests += people
        return room.take_room(people)

    def free_room(self, room_number: int):
        room = [r for r in self.rooms if r.number == room_number][0]
        self.guests -= room.people
        return room.free_room()

    def status(self):
        free_rooms = [str(room.number) for room in self.rooms if not room.is_taken]
        taken_rooms = [str(room.number) for room in self.rooms if room.is_taken]

        return f"Hotel {self.name} has {self.guests} total guests\n" \
               f"Free rooms: {', '.join(free_rooms)}\n" \
               f"Taken rooms: {', '.join(taken_rooms)}"
