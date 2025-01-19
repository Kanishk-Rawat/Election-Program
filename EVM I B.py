# Electronic Voting Machine Mark I
#

c1 = 0
c2 = 0
c3 = 0
c4 = 0
c5 = 0
c6 = 0
candate_num = [1, 2, 3, 4, 5, 6]
x = 0

#Replace 3 with the exact number of voters
while x != 3:
    x = x + 1
    vote = (int(input("\nVote for Prime Minister\n\n Press:"
                           "\n'1' for c1"
                           "\n'2' for c2"
                           "\n'3' for c3"
                           "\n'4' for c4"
                           "\n'5' for c5"
                           "\n'6' for c6\n\n")))

    if vote == 1:
        c1 = c1 + 1
    if vote == 2:
        c2 = c2 + 1
    if vote == 3:
        c3 = c3 + 1
    if vote == 4:
        c4 = c4 + 1
    if vote == 5:
        c5 = c5 + 1
    if vote == 6:
        c6 = c6 + 1
    if len(vote) > 6 or vote not in candate_num:
        print("Invalid Vote")

    print("\n\n\n\n\n\n\n------ Voting Completed ------\n\n-----Send Next Voter--------\n\n\n\n\n\n\n")

print(" ------- Election Process Complete ------- \n\n\nResults\n")
print("\nPrime Minister\nc1:", c1, "\nc2:", c2, "\nc3:", c3, "\nc4:", c4,
      "\nc5:",
      c5, "\nc6:", c6)
