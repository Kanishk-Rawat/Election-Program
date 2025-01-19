# Electronic Voting Machine Mark II
import time as t
import pickle as p

a = input("Enter Z to load results from previous election:\nEnter X to start a new election: ")
if a == "z":
    with open("../data.pkl", "rb") as file:
        data = p.load(file)
    for i in data:
        print(i, data[i])
if a == "x":
    # Replace c-series with candidate names
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    c5 = 0
    c6 = 0
    c7 = 0
    valid = 0
    invalid = 0
    voters = int(input("Enter Total Number of Voters : "))

    cand_num = ["1", "2", "3", "4", "5", "6", "7"]
    x = 0

    valid_vote = (
        "\n\n\n------------------------------------------------\n\n\n\n\n--------- Your vote has been registered"
        " --------\n\n\n\n\n------------------------------------------------\n\n\n\n\n\n")

    while x != voters:

        x = x + 1
        vote = (str(input("\nVote for Prime Minister\n\n Press your candidate number and then hit enter:\n\n"
                          "\n'1' for c1"
                          "\n'2' for c2"
                          "\n'3' for c3"
                          "\n'4' for c4"
                          "\n'5' for c5"
                          "\n'6' for c6"
                          "\n'7' for c7\n\n")))

        if vote == "1":
            c1 += 1
            valid += 1
            print(valid_vote)
        if vote == "2":
            c2 += 1
            valid += 1
            print(valid_vote)
        if vote == "3":
            c3 += 1
            valid += 1
            print(valid_vote)
        if vote == "4":
            c4 += 1
            valid += 1
            print(valid_vote)
        if vote == "5":
            c5 += 1
            valid += 1
            print(valid_vote)
        if vote == "6":
            c6 += 1
            valid += 1
            print(valid_vote)
        if vote == "7":
            c7 += 1
            valid += 1
            print(valid_vote)

        if len(vote) > 1 or vote not in cand_num:
            print("\n\n\n------------------------------------------\n\n\n\n\n-------------- Invalid Vote --------------"
                  "\n\n\n\n\n------------------------------------------\n\n\n\n\n\n")
            invalid += 1

        t.sleep(8)

    else:

        print(" ------- Election Process Complete ------- \n\n\n\n\n---------------- Results ----------------\n"
              "-----------------------------------------\n-----------------------------------------")

        print("\nc1:", c1, "\nc2:", c2, "\nc3:", c3, "\nc4:", c4,
              "\nc5:",
              c5, "\nc6:", c6, "\nc7:", c7, "\nValid Votes :", valid, "\nInvalid Votes :", invalid)

        print("\n-----------------------------------------\n-----------------------------------------")
        print("\n\nEnter X to close the program\n")

        data = {"Total Voters:": voters, "Votes for c1:": c1, "Votes for c2:": c2, "Votes for c3:": c3,
                "Votes for c4:": c4, "Votes for c5:": c5, "Votes for c6:": c6, "Votes for c7:": c7,
                "Invalid Votes": invalid}

        with open("../data.pkl", "wb") as file:
            p.dump(data, file)
        com = input()
        if com == "x":
            pass
