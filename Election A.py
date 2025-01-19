#Change variable names to real candidate names
candid_1 = 0
candid_2 = 0
candid_3 = 0
candid_4 = 0
candid_5 = 0
candid_6 = 0


x = 0

#Replace three with the actual number of voters before running so the loop is executed the same number of times
while x < 3:
    x = x + 1
    vote_pres = (int(input("\nVote for Prime Minister\n Press:"
                           "\n'1' for candid_1"
                           "\n'2' for candid_2"
                           "\n'3' for candid_3"
                           "\n'4' for candid_4"
                           "\n'5' for candid_5\n")))
    if vote_pres == 1:
        candid_1 = candid_1 + 1
    if vote_pres == 2:
        candid_2 = candid_2 + 1
    if vote_pres == 3:
        candid_3 = candid_3 + 1
    if vote_pres == 4:
        candid_4 = candid_4 + 1
    if vote_pres == 5:
        candid_5 = candid_5 + 1

    print("Voting Completed.\nSend Next Voter\n")

print(" ------- Election Process Complete ------- \n\n\nResults\n")
print("\nPrime Minister\ncandid_1:", candid_1, "\ncandid_2:", candid_2, "\ncandid_3:", candid_3, "\ncandid_4:",
      candid_4, "\ncandid_5:", candid_5)
