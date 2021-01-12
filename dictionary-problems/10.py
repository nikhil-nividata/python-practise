# Count Votes

def count():
    votes = [
        "john", "johnny", "jackie",
        "johnny", "john", "jackie",
        "jamie", "jamie", "john",
        "johnny", "jamie", "johnny",
        "john"
    ]
    counts = {}
    for vote in votes:
        counts[vote] = counts.get(vote, 0) + 1

    max_votes = max(counts.values())

    return sorted(
        [k
            for k, val in counts.items()
            if val == max_votes
         ])[0]


if __name__ == "__main__":
    print(count())
