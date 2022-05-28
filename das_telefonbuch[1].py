def empty_array_4():
    array = [[None, None, None, None],
             [None, None, None, None],
             [None, None, None, None],
             [None, None, None, None]]
    return array


def create_dict(name, year, phone_number):
    data = {"name": name,
            "year": year,
            "phone_number": phone_number}
    return data


def calculate_hash(array_2d, data):
    array_length = len(array_2d)
    first_letter = data["name"][0]
    hashed_name = ord(first_letter) % array_length
    return hashed_name


def insert(array_2d, data):
    vertical_index = calculate_hash(array_2d, data)
    horizontal_array = array_2d[vertical_index]

    v, condition = is_full(array_2d, data)
    if condition is True:
        horizontal_array = resize(horizontal_array, len(horizontal_array) * 2)
        array_2d[vertical_index] = horizontal_array

    for index in range(len(horizontal_array)):
        if horizontal_array[index] is not None:
            if horizontal_array[index] == data:
                return array_2d
        if horizontal_array[index] is None:
            horizontal_array[index] = data
            break
    return array_2d


def search(array_2d, data):
    name = data["name"]
    year = data["year"]
    vertical_index = calculate_hash(array_2d, data)
    horizontal_array = array_2d[vertical_index]
    v, h = 0, 0

    for index in range(0, len(horizontal_array)):
        if horizontal_array[index] is not None:
            if (horizontal_array[index]["name"]) == name and (horizontal_array[index]["year"]) == year:
                v = vertical_index
                h = index
                return ((v, h), horizontal_array[index])
    return ((v, h), None)


def is_full(array_2d, data):
    vertical_index = calculate_hash(array_2d, data)
    horizontal_array = array_2d[vertical_index]
    last_horizontal_index = len(horizontal_array) - 1
    v = vertical_index

    if horizontal_array[last_horizontal_index] == None:
        v = vertical_index
        return v, False
    return v, True


def resize(h_array, new_size):
    new_h_array = [None] * new_size
    for index in range(len(h_array)):
        new_h_array[index] = h_array[index]
    return new_h_array


def add_new_data():
    name = input(("Name: ").lower())
    year = int(input("Birth of Year: "))
    phone_number = input("Phone Number: ")
    return name, year, phone_number


def check_data(array_2d, data):
    name = data["name"]
    year = data["year"]
    vertical_index = calculate_hash(array_2d, data)
    horizontal_array = array_2d[vertical_index]

    for index in range(len(horizontal_array)):
        if horizontal_array[index] != None:
            if horizontal_array[index]["name"] == name and horizontal_array[index]["year"] == year:
                print("Phone Number  : Cant add data already exists")
                return True
    return False


def menu_input():
    while (True):
        try:
            choice = int(input("Choise?".ljust(28)))
            assert choice in range(1, 4), "There are only 3 choices. Please choose 1, 2, or 3."
            break
        except ValueError:
            print("Please input a number.")
        except AssertionError as msg:
            print(msg)
    return choice


def main():
    array_2d = empty_array_4()
    while (True):
        print("\n")
        print("Das Telefonbuch".center(30))
        print("\n1. Add new number \n2. Search by name \n3. Exit\n")
        choice = menu_input()
        print("\n")

        if choice == 1:
            print("Das Telefonbuch".center(30))
            name, year, phone_number = None, None, None
            while True:
                print("\nAdd new data")
                name = input("Name          : ").lower()
                while True:
                    try:
                        year = (input("Birth of Year : "))

                        if year == "":
                            enter = True
                            break
                        else:
                            try:
                                year = int(year)
                                break
                            except ValueError:
                                print("Please insert a number.")
                    except:
                        print("Please insert a number.")
                if year == "":
                    break
                else:
                    check = check_data(array_2d, create_dict(name, year, None))
                    if check == True:
                        continue
                    if check == False:
                        break
            phone_number = input("Phone Number  : ")
            if name == "" and year == "" and phone_number == "":
                continue
            else:
                array_2d = insert(array_2d, create_dict(name, year, phone_number))
                print("\n")

        elif choice == 2:
            print("Das Telefonbuch".center(30))
            print("\nSearch by name")
            search_name = input("Name          : ").lower()

            enter = False
            while True:
                try:
                    search_year = (input("Birth of Year : "))

                    if search_year == "":
                        enter = True
                        break
                    else:
                        try:
                            search_year = int(search_year)
                            break
                        except ValueError:
                            print("Please insert a number.")
                except:
                    print("Please insert a number.")
            if enter == True:
                continue
            if search_name == "" and search_year == "":
                continue

            search_data = create_dict(search_name, search_year, None)
            (v, h), data = search(array_2d, search_data)

            if data is not None:
                print("Phone Number  :", data["phone_number"])
            else:
                print("Phone Number  : Not Found")
                ("\n")

        elif choice == 3:
            print("Thank you!")
            break

        else:
            print("Wrong input, please try again.")


###### testing ######
def test():
    print("Test running...")
    should_return_same_hash()
    should_return_different_hash()
    should_add_new_data()
    should_add_new_data_and_resize()
    should_return_data_with_v_and_h_index()
    should_not_return_data()
    should_get_new_horizontal_array_with_new_length_2times_after_insert()
    should_return_array_2d_with_the_same_length_like_before_after_insert()
    should_return_true_when_array_full()
    should_return_false_when_array_is_not_full()
    print("Test finished.")


def should_return_same_hash():
    array = [[None, None, None, None],
             [None, None, None, None],
             [None, None, None, None],
             [None, None, None, None]]
    name1 = "ab"
    name2 = "ac"
    name1 = {"name": name1}
    name2 = {"name": name2}
    hashed_name1 = calculate_hash(array, name1)
    hashed_name2 = calculate_hash(array, name2)
    assert hashed_name1 == hashed_name2, "didn't return same hash"


def should_return_different_hash():
    array = [[None, None, None, None],
             [None, None, None, None],
             [None, None, None, None],
             [None, None, None, None]]
    name1 = "ba"
    name2 = "ac"
    name1 = {"name": name1}
    name2 = {"name": name2}
    hashed_name1 = calculate_hash(array, name1)
    hashed_name2 = calculate_hash(array, name2)
    assert hashed_name1 != hashed_name2, "returned same hash"


def should_add_new_data():
    array = [[None, None, None, None],
             [None, None, None, None],
             [None, None, None, None],
             [None, None, None, None]]
    book = {'name': 'stephen', 'year': 1999, 'phone_number': '12345'}
    new_array = insert(empty_array_4(), book)
    vertical_index = calculate_hash(array, book)
    assert array[vertical_index][0] != new_array[vertical_index][0], "new data was not added."


def should_add_new_data_and_resize():
    array = [[None, None, None, None],
             [None, None, None, None],
             [None, None, None, None],
             [{'name': 'stephen', 'year': 1999, 'phone_number': '12345'},
              {'name': 'stephen', 'year': 1998, 'phone_number': '21435'},
              {'name': 'stephen', 'year': 1997, 'phone_number': '32345'},
              {'name': 'stephen', 'year': 1996, 'phone_number': '45321'}]]

    array_2 = [[None, None, None, None],
               [None, None, None, None],
               [None, None, None, None],
               [{'name': 'stephen', 'year': 1999, 'phone_number': '12345'},
                {'name': 'stephen', 'year': 1998, 'phone_number': '21435'},
                {'name': 'stephen', 'year': 1997, 'phone_number': '32345'},
                {'name': 'stephen', 'year': 1996, 'phone_number': '45321'}]]

    book = {'name': 'stephen', 'year': 1995, 'phone_number': '12345'}
    array_2 = insert(array_2, book)
    assert array != array_2, "new data was not added and array was not resized."


def should_return_data_with_v_and_h_index():
    array = [[None, None, None, None],
             [None, None, None, None],
             [None, None, None, None],
             [{'name': 'stephen', 'year': 1999, 'phone_number': '12345'},
              {'name': 'stephen', 'year': 1998, 'phone_number': '21435'},
              {'name': 'stephen', 'year': 1997, 'phone_number': '32345'},
              {'name': 'stephen', 'year': 1996, 'phone_number': '45321'}]]

    book = {'name': 'stephen', 'year': 1996, 'phone_number': '12345'}
    (v, h), data = search(array, book)
    condition = True
    if data is None:
        condition = False
    assert condition is True, "did not return data with v and h index."


def should_not_return_data():
    array = [[None, None, None, None],
             [None, None, None, None],
             [None, None, None, None],
             [{'name': 'stephen', 'year': 1999, 'phone_number': '12345'},
              {'name': 'stephen', 'year': 1998, 'phone_number': '21435'},
              {'name': 'stephen', 'year': 1997, 'phone_number': '32345'},
              {'name': 'stephen', 'year': 1996, 'phone_number': '45321'}]]

    book = {'name': 'maleakhi', 'year': 2002, 'phone_number': '12345'}
    (v, h), data = search(array, book)
    condition = False
    if v and h and data is not None:
        condition = True
    assert condition is False, "returned data (with v and h index)."


def should_get_new_horizontal_array_with_new_length_2times_after_insert():
    array = [[None, None, None, None],
             [None, None, None, None],
             [None, None, None, None],
             [{'name': 'stephen', 'year': 1999, 'phone_number': '12345'},
              {'name': 'stephen', 'year': 1998, 'phone_number': '21435'},
              {'name': 'stephen', 'year': 1997, 'phone_number': '32345'},
              {'name': 'stephen', 'year': 1996, 'phone_number': '45321'}]]

    array_2 = [[None, None, None, None],
               [None, None, None, None],
               [None, None, None, None],
               [{'name': 'stephen', 'year': 1999, 'phone_number': '12345'},
                {'name': 'stephen', 'year': 1998, 'phone_number': '21435'},
                {'name': 'stephen', 'year': 1997, 'phone_number': '32345'},
                {'name': 'stephen', 'year': 1996, 'phone_number': '45321'}]]
    book = {'name': 'stephen', 'year': 1995, 'phone_number': '12345'}
    vertical_index = calculate_hash(array, book)
    array_2 = insert(array_2, book)
    h_array = array[vertical_index]
    h_resized_array = array_2[vertical_index]
    assert len(h_array) != len(h_resized_array), "horizontal array was not resized."


def should_return_array_2d_with_the_same_length_like_before_after_insert():
    array = [[None, None, None, None],
             [None, None, None, None],
             [None, None, None, None],
             [None, None, None, None]]
    book = {'name': 'stephen', 'year': 1999, 'phone_number': '12345'}
    new_array = insert(array, book)
    vertical_index = calculate_hash(array, book)
    assert len(array[vertical_index]) == len(new_array[vertical_index]), "the array has a different length."


def should_return_true_when_array_full():
    array = [[None, None, None, None],
             [None, None, None, None],
             [None, None, None, None],
             [{'name': 'stephen', 'year': 1999, 'phone_number': '12345'},
              {'name': 'stephen', 'year': 1998, 'phone_number': '21435'},
              {'name': 'stephen', 'year': 1997, 'phone_number': '32345'},
              {'name': 'stephen', 'year': 1996, 'phone_number': '45321'}]]

    book = {'name': 'stephen', 'year': 1995, 'phone_number': '12345'}
    v, condition = is_full(array, book)
    assert condition is True, "is_full() function didn't work properly"


def should_return_false_when_array_is_not_full():
    array = [[None, None, None, None],
             [None, None, None, None],
             [None, None, None, None],
             [None, None, None, None]]
    book = {'name': 'stephen', 'year': 1999, 'phone_number': '12345'}
    v, condition = is_full(array, book)
    assert condition is False, "is_full() function didn't work properly"


if __name__ == "__main__":
    test()
    main()
