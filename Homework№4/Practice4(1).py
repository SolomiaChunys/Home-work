number_of_room = int(input("What is the number of your room?: "))
number_of_floors = int(input("What is the number of floors?: "))
rooms_on_one_floor = int(input("How many rooms are there on one floor?: "))


def location_of_room(room, floors, on_one_floor):
    if number_of_room <= 0 or number_of_floors <= 0 or rooms_on_one_floor <= 0:
        return "One of the numbers is incorrect!"

    rooms_in_one_apartment = number_of_floors * rooms_on_one_floor

    entrance = number_of_room // rooms_in_one_apartment
    remainder1 = number_of_room % rooms_in_one_apartment
    if remainder1 > 0:
        entrance += 1

    floor = remainder1 // rooms_on_one_floor
    remainder2 = remainder1 % rooms_on_one_floor
    if remainder2 > 0:
        floor += 1

    return f'Room {number_of_room} is located in the {entrance} entrance on the {floor} floor'


result = location_of_room(number_of_room, number_of_floors, rooms_on_one_floor)
print(result)
