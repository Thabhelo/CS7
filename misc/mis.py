def lh(start, goal, next_hop, is_lava):
    if is_lava(start) or is_lava(goal):
        return "No"
    num_hops = 0
    while start < goal:
        while is_lava(start):
            start -= 1
        start = next_hop(start)
        num_hops += 1
    return num_hops


def forbid_digit(f, forbidden):
    def forbid_wrapper(n):
        if n % 10 == forbidden:
            return forbid_digit(f, n // 10)
        else:
            return forbid_digit(f, n)
        return forbid_wrapper
