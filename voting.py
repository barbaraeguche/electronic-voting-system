
def display_candidates(to_display: dict[str, str]) -> None:
    """
    this function displays a complete list of all eligible candidates and their respective IDs.

    parameters: 
        to_display: dictionary containing candidate IDs and names.
    
    return: None
    """
    for ids, name in to_display.items():
        separator: int = 40 - (11 + len(name))
        print(f"|  {ids}  >>  {name}{' ' * separator}|")

def vote_candidate(id: str, votes: dict[str, int], candidates: dict[str, str]) -> None:
    """
    this function enables users vote for the candidate of their choice.
    
    parameters:
        id: the id of the candidate
        votes: dictionary of candidate IDs with their corresponding vote count
    
    returns: None
    """
    if id in candidates.keys():
        # update the vote count for the candidate
        votes.update({ id: votes.get(id) + 1 })
        print(f"Your ballot has been successfully casted for: {candidates.get(id)} bearing candidate id ~ {id}")

def update_candidate(to_add: str, candidates: dict[str, str], votes: dict[str, int]) -> None:
    """
    this funtion adds new candidates to the voting system.
    
    parameters:
        to_add: string of new candidates' information
        candidates: dictionary containing all candidates and their IDs
        votes: dictionary of candidate IDs with their corresponding vote count
    
    returns: None
    """
    for candid in to_add.split(';'):
        id_name: list[str] = candid.split(',')
        
        # add the candidates to the dictionary
        candidates.update({ id_name[0].strip(): ' '.join(map(lambda x: x.capitalize().strip(), id_name[1].split())) })
        # initially set votes for each candidate to zero
        votes.update({ id_name[0].strip(): 0 })

def display_results(votes: dict[str, int], candidates: dict[str, str]) -> None:
    """
    this function displays the electoral results in ascending order of vote count.
    
    parameters:
        votes: dictionary of candidate IDs with their corresponding vote count
        candidates: dictionary containing all candidates and their IDs
    
    returns: None
    """
    sorted_by_votes: dict[str, int] = dict(sorted(votes.items(), key=lambda x: x[1], reverse=True))
    position: int = 0
    prev_value: int = -1

    for ids, vote_count in sorted_by_votes.items():
        separator1: int = 8 - len(str(position))
        separator2: int = 13 - len(str(vote_count))
        separator3: int = 2 - len(str(ids))
        separator4: int = 30 - len(str(candidates.get(ids)))

        # update position when vote count for a candidate is different from the previous one
        if vote_count != prev_value:
            position += 1
        
        print(f"| {' ' * separator1}{position} | {' ' * separator2}{vote_count} | {' ' * separator3}{ids} | {candidates.get(ids)}{' ' * separator4} |")
        prev_value = vote_count
