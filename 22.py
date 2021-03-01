import logging
from collections import deque
from pathlib import Path

# change to info or debug to see the game state being updated step by step
logging.basicConfig(level=logging.WARNING)


def read():
    path = Path(__file__).parent / "input22.txt"
    file = open(path, "r")

    p1_deck = []
    p2_deck = []

    append_to_p1 = True
    for line in file.readlines():
        line = line.strip()

        if line == "":
            append_to_p1 = False
        elif "Player" in line:
            pass
        elif append_to_p1:
            p1_deck.append(int(line))
        else:
            p2_deck.append(int(line))

    return p1_deck, p2_deck


def p1(args):
    p1_deck, p2_deck = args
    queue_p1 = deque(p1_deck)
    queue_p2 = deque(p2_deck)

    while queue_p1 and queue_p2:
        card_p1 = queue_p1.popleft()
        card_p2 = queue_p2.popleft()

        if card_p1 > card_p2:
            queue_p1.append(card_p1)
            queue_p1.append(card_p2)
        else:
            queue_p2.append(card_p2)
            queue_p2.append(card_p1)

    logging.debug(p1_deck)
    logging.debug(p2_deck)

    logging.debug(queue_p1)
    logging.debug(queue_p2)
    return compute_answer(queue_p1, queue_p2)


def compute_answer(queue_p1, queue_p2):
    if queue_p1:
        compute = queue_p1
    else:
        compute = queue_p2
    answer = [x * compute.popleft() for x in range(len(compute), 0, -1)]

    logging.info(answer)
    total = sum(answer)
    logging.info(total)
    return total


def helper(queue_p1, queue_p2, game_number):
    logging.debug(f"\n=== Game {game_number} === ")
    unique = set()
    round = 1
    while queue_p1 and queue_p2:
        logging.debug(f"-- Round {round} (Game {game_number}) --")
        logging.debug(f"Player 1's deck: {list(queue_p1)}")
        logging.debug(f"Player 2's deck: {list(queue_p2)}")
        hashID = (str(list(queue_p1)), str(list(queue_p2)))

        # first rule of part two
        if hashID in unique:
            logging.debug("these two decks appear before, player 1 win")
            return True
        else:
            card_p1 = queue_p1.popleft()
            card_p2 = queue_p2.popleft()
            logging.debug(f"Player 1 plays: {card_p1}")
            logging.debug(f"Player 2 plays: {card_p2}")

            if card_p1 <= len(queue_p1) and card_p2 <= len(queue_p2):
                logging.debug("Playing a sub-game to determine the winner...")
                p1_won = helper(
                    deque(list(queue_p1)[:card_p1]),
                    deque(list(queue_p2)[:card_p2]),
                    game_number + 1,
                )
                if p1_won:
                    logging.debug(
                        f"Player 1 wins round {round} of game {game_number}!")
                    queue_p1.append(card_p1)
                    queue_p1.append(card_p2)
                else:
                    logging.debug(
                        f"Player 2 wins round {round} of game {game_number}!")
                    queue_p2.append(card_p2)
                    queue_p2.append(card_p1)
            elif card_p1 > card_p2:
                logging.debug(
                    f"Player 1 wins round {round} of game {game_number}!")
                queue_p1.append(card_p1)
                queue_p1.append(card_p2)
            else:
                logging.debug(
                    f"Player 2 wins round {round} of game {game_number}!")
                queue_p2.append(card_p2)
                queue_p2.append(card_p1)

        unique.add(hashID)
        round += 1
        logging.debug("\n")

    logging.debug(f"...anyway, back to game {game_number-1}")
    if game_number == 1:
        return compute_answer(queue_p1, queue_p2)
    if queue_p1:
        return True
    else:
        return False


def p2(args):
    p1_deck, p2_deck = args
    queue_p1 = deque(p1_deck)
    queue_p2 = deque(p2_deck)
    return helper(queue_p1, queue_p2, 1)


def main():
    input = read()
    print(p1(input))
    print(p2(input))


if __name__ == "__main__":
    main()
