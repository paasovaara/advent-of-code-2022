# This solution is 100% provided by chat-gpt 🤯

def item_priority(item):
    """Returns the priority of an item."""
    if item.islower():
        return ord(item) - 96
    else:
        return ord(item) - 38

with open('input.txt', 'r') as f:
    rucksacks = [line.strip() for line in f.readlines()]

total_priority = 0
for rucksack in rucksacks:
    half_len = len(rucksack) // 2
    first_half = rucksack[:half_len]
    second_half = rucksack[half_len:]
    common_items = set(first_half) & set(second_half)
    common_priority = sum([item_priority(item) for item in common_items])
    total_priority += common_priority

print(total_priority)
