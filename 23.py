import math
import logging
from pathlib import Path

logging.basicConfig(level=logging.WARNING)


def read():
    path = Path(__file__).parent / "input23.txt"
    file = open(path, "r")

    for line in file.readlines():
        cups = list(map(int, line.strip()))

    return cups


def p1(cups):
    cups = list(cups)
    round_to_run = 100
    length = len(cups)
    round_runned = 0
    current_cup_index = 0

    while round_runned != round_to_run:
        other_cup_index = cups[current_cup_index]
        dest_cup_value = other_cup_index - 1

        logging.debug(f"-- moves {round_runned} --")
        logging.debug(f"cups: {cups}")
        next_three = []
        next_three_index = current_cup_index
        for _ in range(3):
            next_three_index += 1
            next_three_index %= length
            next_three.append(cups[next_three_index])
        logging.debug(f"pick up: {next_three}")

        while dest_cup_value in next_three and dest_cup_value != 0:
            dest_cup_value -= 1

        if dest_cup_value == 0:
            # wrap around to find largest value excluding the next three
            index = current_cup_index + 4
            index %= length

            maximum = -math.inf
            for _ in range(length - 3):
                if cups[index] > maximum:
                    maximum = cups[index]
                index += 1
                index %= length

            dest_cup_index = cups.index(maximum)

        else:
            dest_cup_index = cups.index(dest_cup_value)

        logging.debug(f"dest_cup_value: {cups[dest_cup_index]}")
        old_cups = list(cups)

        index = current_cup_index + 1
        index %= length
        old_cup_index = current_cup_index + 4
        old_cup_index %= length

        while old_cup_index != dest_cup_index:
            cups[index] = old_cups[old_cup_index]
            index += 1
            index %= length
            old_cup_index += 1
            old_cup_index %= length

        cups[index] = old_cups[dest_cup_index]
        index += 1
        index %= length

        for y in range(3):
            cups[index] = old_cups[(current_cup_index + y + 1) % length]
            index += 1
            index %= length

        logging.debug("")
        current_cup_index += 1
        current_cup_index %= length
        round_runned += 1

    logging.debug(cups)
    cup_one_index = cups.index(1)
    other_cup_index = cup_one_index + 1
    answer = ""

    # dun include 1 in answer
    for _ in range(length - 1):
        answer += str(cups[other_cup_index])
        other_cup_index += 1
        other_cup_index %= length

    logging.info(answer)
    return answer


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


def p2(cups):
    cups = list(cups)
    logging.debug(cups)

    round_to_run = 10_000_000
    amount_of_cup = 1_000_000
    length = len(cups)
    cup_map = {}
    current_cup = Node(cups[0])
    cup_map[current_cup.value] = current_cup
    prev_cup = current_cup

    for x in range(1, length):
        new_cup = Node(cups[x])
        prev_cup.next = new_cup
        cup_map[new_cup.value] = new_cup
        prev_cup = new_cup

    for y in range(length + 1, amount_of_cup + 1):
        new_cup = Node(y)
        prev_cup.next = new_cup
        cup_map[y] = new_cup
        prev_cup = new_cup

    # connect last cup to first cup to form the full circle
    prev_cup.next = current_cup
    round_runned = 0

    while round_runned != round_to_run:
        logging.debug(f"current cup: {current_cup.value}")
        dest_cup_value = current_cup.value - 1
        logging.debug(f"initial dest cup: {dest_cup_value}")
        next_cup_of_current_cup = current_cup.next

        logging.debug(
            f"next cup of current cup: {next_cup_of_current_cup.value}")
        temp_cup = current_cup.next
        next_three_cup_values = []
        for x in range(3):
            next_three_cup_values.append(temp_cup.value)
            temp_cup = temp_cup.next

        logging.debug(f"next three values: {next_three_cup_values}")
        cup_after_three_cup = temp_cup
        logging.debug(f"cup after three cup: {cup_after_three_cup.value}")
        while dest_cup_value in next_three_cup_values and dest_cup_value != 0:
            dest_cup_value -= 1

        if dest_cup_value == 0:
            maximum = amount_of_cup
            while maximum in next_three_cup_values:
                maximum -= 1
            dest_cup = cup_map[maximum]
            next_cupof_dest_cup = dest_cup.next
        else:
            dest_cup = cup_map[dest_cup_value]
            next_cupof_dest_cup = dest_cup.next

        logging.debug(f"dest cup: {dest_cup.value}")
        logging.debug(f"next cup of dest cup: {next_cupof_dest_cup.value}")
        current_cup.next = cup_after_three_cup
        dest_cup.next = next_cup_of_current_cup

        temp_cup = dest_cup.next
        for x in range(2):
            temp_cup = temp_cup.next

        # connect the last cup of the three picked cups to the cup next to destination cup
        temp_cup.next = next_cupof_dest_cup

        current_cup = current_cup.next
        round_runned += 1

    one_value_cup = cup_map[1]
    first_cup = one_value_cup.next
    second_cup = first_cup.next

    logging.info(f"first cup: {first_cup}, second cup: {second_cup}")
    answer = first_cup.value * second_cup.value
    logging.info(answer)
    return answer


def main():
    input = read()
    print(p1(input))
    print(p2(input))


if __name__ == "__main__":
    main()
