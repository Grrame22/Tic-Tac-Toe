def write_tic_tac_toe():
    line = "---------"
    print(line)
    print("|       |")
    print("|       |")
    print("|       |")
    print(line)

    def the_filed():
        print(line)
        print("| " + field[0][0] + " " + field[1][0] + " " + field[2][0] + " |")
        print("| " + field[0][1] + " " + field[1][1] + " " + field[2][1] + " |")
        print("| " + field[0][2] + " " + field[1][2] + " " + field[2][2] + " |")
        print(line)

    field = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]

    symbol = "X"
    while True:
        user_input = input("Enter the coordinates: ").split(" ")
        if (not user_input[0].isdigit()) or (not user_input[1].isdigit()):
            print("You should enter numbers!")
            continue
        elif not (1 <= int(user_input[0]) < 4) or not (1 <= int(user_input[1]) < 4):
            print("Coordinates should be from 1 to 3!")
            continue
        else:
            user_coordinates = [int(user_input[0]) - 1, int(user_input[1]) - 1]
            if user_coordinates[1] == 0:
                user_coordinates[1] = user_coordinates[1] - 1
            elif user_coordinates[1] == 2:
                user_coordinates[1] = user_coordinates[1] - 2
            if field[user_coordinates[0]][user_coordinates[1]] == " ":
                field[user_coordinates[0]][user_coordinates[1]] = symbol
                if symbol == "X":
                    symbol = "O"
                else:
                    symbol = "X"
                if all(field[user_coordinates[0]]):
                    if "".join(field[user_coordinates[0]]) == "XXX":
                        the_filed()
                        print("X wins")
                        break
                    elif "".join(field[user_coordinates[0]]) == "OOO":
                        the_filed()
                        print("O wins")
                        break

                if (field[0][0] == "X") and (field[1][0] == "X") and (field[2][0] == "X"):
                    the_filed()
                    print("X wins")
                    break
                elif (field[0][0] == "O") and (field[1][0] == "O") and (field[2][0] == "O"):
                    the_filed()
                    print("O wins")
                    break
                elif (field[0][1] == "X") and (field[1][1] == "X") and (field[2][1] == "X"):
                    the_filed()
                    print("X wins")
                    break
                elif (field[0][1] == "O") and (field[1][1] == "O") and (field[2][1] == "O"):
                    the_filed()
                    print("O wins")
                    break
                elif (field[0][2] == "X") and (field[1][2] == "X") and (field[2][2] == "X"):
                    the_filed()
                    print("X wins")
                    break
                elif (field[0][2] == "O") and (field[1][2] == "O") and (field[2][2] == "O"):
                    the_filed()
                    print("O wins")
                    break
                elif (field[0][0] == "X") and (field[1][1] == "X") and (field[2][2] == "X"):
                    the_filed()
                    print("X wins")
                    break
                elif (field[0][0] == "O") and (field[1][1] == "O") and (field[2][2] == "O"):
                    the_filed()
                    print("O wins")
                    break
                elif (field[0][2] == "X") and (field[1][1] == "X") and (field[2][0] == "X"):
                    the_filed()
                    print("X wins")
                    break
                elif (field[0][2] == "O") and (field[1][1] == "O") and (field[2][0] == "O"):
                    the_filed()
                    print("O wins")
                    break

                if all(field[0]) and all(field[1]) and all(field[2]) and (not " " in field[0]) \
                        and (not " " in field[1]) and (not " " in field[2]):
                    the_filed()
                    print("Draw")
                    break

                the_filed()
                continue
            else:
                print("This cell is occupied! Choose another one!")


write_tic_tac_toe()
