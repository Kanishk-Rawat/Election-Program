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
    c8 = 0
    valid = 0
    invalid = 0
    cno = int(input("Number of Candidates: "))
    print("\nEnter Candidate Names")
    cn1 = str(input("\nEnter Candidate 1: "))
    cno -= 1
    cn2 = str(input("Enter Candidate 2: "))
    cno -= 1
    if cno != 0:
        cn3 = str(input("Enter Candidate 3: "))
        cno -= 1
    else:
        cn3 = None
    if cno != 0:
        cn4 = str(input("Enter Candidate 4: "))
        cno -= 1
    else:
        cn4 = None
    if cno != 0:
        cn5 = str(input("Enter Candidate 5: "))
        cno -= 1
    else:
        cn5 = None
    if cno != 0:
        cn6 = str(input("Enter Candidate 6: "))
        cno -= 1
    else:
        cn6 = None
    if cno != 0:
        cn7 = str(input("Enter Candidate 7: "))
        cno -= 1
    else:
        cn7 = None
    if cno != 0:
        cn8 = str(input("Enter Candidate 8: "))
        cno -= 1
    else:
        cn8 = None

    tim = int(input("Enter Time delay between two votes: "))
    voters = int(input("Enter Total Number of Voters : "))

    cand_num = ["1", "2", "3", "4", "5", "6", "7"]
    x = 0

    valid_vote = (
        "\n\n\n------------------------------------------------\n\n\n\n\n--------- Your vote has been registered"
        " --------\n\n\n\n\n------------------------------------------------\n\n\n\n\n\n")

    while x != voters:

        x = x + 1
        print("\nVote for Prime Minister\n\n Press your candidate number and then hit enter:\n\n\n'1' for", cn1,
              "\n'2' for", cn2, "\n'3' for", cn3, "\n'4' for", cn4, "\n'5' for", cn5, "\n'6' for", cn6, "\n'7' for",
              cn7, "\n'8' for", cn8)

        vote = (str(input()))

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
        if vote == "8":
            c8 += 1
            valid += 1
            print(valid_vote)

        if len(vote) > 1 or vote not in cand_num:
            print("\n\n\n------------------------------------------\n\n\n\n\n-------------- Invalid Vote --------------"
                  "\n\n\n\n\n------------------------------------------\n\n\n\n\n\n")
            invalid += 1

        t.sleep(tim)

    else:

        print(" ------- Election Process Complete ------- \n\n\n\n\n---------------- Results ----------------\n"
              "-----------------------------------------\n-----------------------------------------")

        print("\nc1:", c1, "\nc2:", c2, "\nc3:", c3, "\nc4:", c4,
              "\nc5:",
              c5, "\nc6:", c6, "\nc7:", c7, "\nc8:", c8, "\nValid Votes :", valid, "\nInvalid Votes :", invalid)

        print("\n-----------------------------------------\n-----------------------------------------")
        print("\n\nEnter X to close the program\n")

        data = {"Total Voters:": voters, cn1: c1, cn2: c2, cn3: c3,
                cn4: c4, cn5: c5, cn6: c6, cn7: c7, cn8: c8,
                "Invalid Votes": invalid}

        with open("../data.pkl", "wb") as file:
            p.dump(data, file)
        com = input()
        if com == "x":
            pass
