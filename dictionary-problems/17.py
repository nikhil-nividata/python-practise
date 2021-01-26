# Kth non repeating String character

def k_char():
    inp_str = "geeksforgeeks"
    k = 3
    from collections import OrderedDict
    counts = OrderedDict.fromkeys(inp_str, 0)
    for ch in inp_str:
        counts[ch] += 1
    non_rep = [k for k, val in counts.items() if val == 1]
    if k - 1 < len(non_rep):
        return non_rep[k-1]
    else:
        return None


if __name__ == "__main__":
    print(k_char())
