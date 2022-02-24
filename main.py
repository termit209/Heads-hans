import random
from typing import List

MAX_LENGHT: int = 10


def generate_random_list(size: int) -> List[int]:
    random_list = [random.randint(-size, size) for _ in range(size)]
    return random_list

def generate_random_lists(n: int) -> List[List[int]]:
    lists = []
    sizes = []
    if n > MAX_LENGHT:
        raise AssertionError(f"Number of list {n} more than MAX_LENGHT={MAX_LENGHT}. Size of lists can not be unique.")
    size = random.randint(1, MAX_LENGHT) 
    for i in range(n):
        while size in sizes:
            size = random.randint(1, MAX_LENGHT)
        lists.append(generate_random_list(size))
        sizes.append(size)
    return lists

def sort_lists(lists: List[List[int]]) -> List[List[int]]:
    for i in range(len(lists)):
        is_odd = (i + 1) % 2 == 1
        lists[i].sort(reverse=is_odd)
    return lists

def main_funtion(n: int) -> List[List[int]]:
    random_lists = generate_random_lists(n)
    sorted_lists = sort_lists(random_lists)
    return sorted_lists
