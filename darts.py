def main():
    print("Welcome to the darts calculator! I will keep track of your game of darts.")
    rivi = input("What is the start score of the game?\n")
    score = int(rivi)
    kierros = 1
    while score != 0:
        print("Enter the results of your throws for round", kierros, ":")
        results = 0
        for i in range(1, 4):
            tul = str(i)
            tuloste = "Throw "+tul+" :"
            rivi = input(tuloste)
            throw = int(rivi)
            results = results + throw
        if score < results or (score - results) == 1:
            print("You have reduced your score to",  (score - results), ". Score resetting to the initial score of the round.")
        else:
            score = score - results
        print("You have", score, "points remaining.")
        kierros = kierros + 1
    print("You have won the game after",  kierros-1, "rounds. Congratulations!")


main()
