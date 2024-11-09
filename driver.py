import voting as vot

if __name__ == '__main__':
    # variables
    candidates: dict[str, str] = {}
    votes: dict[str, int] = {}

    # welcome message
    print("Welcome to the Simple Electronic Voting System:")
    print("+++++++++++++++++++++++++++++++++++++++++++++++")

    # prompts the user to enter a string collection of electoral candidates
    entry: str = input("\nPlease enter a collection electoral candidates (id, name) separated by `;`:\n")
    vot.update_candidate(entry, candidates, votes)

    while True:
        # displays several codes with its respective description
        print("\n\n********************************")
        print("| Code >> Description          |")
        print("********************************")
        print("|  1   >> Display candidates   |")
        print("|  2   >> Vote a candidate     |")
        print("|  3   >> Add new candidate(s) |")
        print("|  4   >> Display results      |")
        print("|  0   >> End SEVS             |")
        print("********************************")
        prompt: str = input("\nEnter a code, from the aforementioned, that corresponds to your task: ")

        # ------------------------------------------------------------------------------------------------------------------------------ #
        if prompt == "1":
            print("*****************************************")
            print("|  ID >> Candidate's Name               |")
            print("*****************************************")
            vot.display_candidates(candidates)
            print("*****************************************")

        # ------------------------------------------------------------------------------------------------------------------------------ #
        if prompt == "2":
            id = input("\nPlease enter the ID of the candidate you wish to vote for: ")
            vot.vote_candidate(id, votes, candidates)

        # ------------------------------------------------------------------------------------------------------------------------------ #
        if prompt == "3":
            new_candidates: str = input("\nPlease enter a collection of new electoral candidates (id, name) separated by `;`:\n")
            vot.update_candidate(new_candidates, candidates, votes)
            print("Successfully added new set of electoral candidates to the Voting System.")

        # ------------------------------------------------------------------------------------------------------------------------------ #
        if prompt == "4":
            print("******************************************************************")
            print("| Position | Votes/Ballots | ID | Candidate's Name               |")
            print("******************************************************************")
            vot.display_results(votes, candidates)
            print("******************************************************************")

        # ------------------------------------------------------------------------------------------------------------------------------ #
        if prompt == "0":
            break

    # closing message
    print("Thank you for using our Electronic Voting System.", end="")
