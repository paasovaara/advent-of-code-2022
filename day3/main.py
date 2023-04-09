# Part1 solution is 100% provided by chat-gpt 🤯, the Part2 is also assembled from the chat-gpt output

def find_common_item_type(items) -> str:
    # Convert the list of lists to a set of sets for efficient intersection.
    item_sets = [set(item_list) for item_list in items]
    
    # Find the intersection of all three sets.
    common_items = set.intersection(*item_sets)
    
    if not common_items:
        return None
    return common_items.pop()


def item_priority(item: str):
    if not isinstance(item, str) or len(item) != 1 or not item.isascii() or not item.isalpha():
        raise ValueError("Input must be a string of length 1 representing an ASCII letter")
    
    """Returns the priority of an item."""
    if item.islower():
        return ord(item) - 96
    else:
        return ord(item) - 38

def solve_part1 (rucksacks): 
    total_priority = 0
    for rucksack in rucksacks:
        half_len = len(rucksack) // 2
        first_half = rucksack[:half_len]
        second_half = rucksack[half_len:]
        common_items = set(first_half) & set(second_half)
        common_priority = sum([item_priority(item) for item in common_items])
        total_priority += common_priority

    print("Part 1 answer: ", total_priority)

def solve_part2 (groups):
    group_common_items = [find_common_item_type(items) for items in groups]
    group_priorities = [item_priority(item) for item in group_common_items]
    total_priority = sum(group_priorities)
    print("Part 2 answer: ", total_priority)


with open('input.txt', 'r') as f:
    rucksacks = [line.strip() for line in f.readlines()]
    groups = [rucksacks[i:i+3] for i in range(0, len(rucksacks), 3)]

solve_part1(rucksacks)
solve_part2(groups)