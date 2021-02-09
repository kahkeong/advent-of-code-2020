import logging
from collections import deque
logging.basicConfig(level=logging.INFO)

file1 = open('input22.txt', 'r')


p1Deck = []
p2Deck = []

appendToP1 = True
for line in file1.readlines():
    line = line.strip()

    if (line == ''):
        appendToP1 = False
    elif ('Player' in line):
        pass
    elif (appendToP1):
        p1Deck.append(int(line))
    else:
        p2Deck.append(int(line))




def p1():
    queueP1 = deque(p1Deck)
    queueP2 = deque(p2Deck)

    while queueP1 and queueP2:
        cardP1 = queueP1.popleft()
        cardP2 = queueP2.popleft()

        if (cardP1 > cardP2):
            queueP1.append(cardP1)
            queueP1.append(cardP2)
        else:
            queueP2.append(cardP2)
            queueP2.append(cardP1)

    logging.debug(p1Deck)
    logging.debug(p2Deck)

    logging.debug(queueP1)
    logging.debug(queueP2)
    computeAnswer(queueP1, queueP2)


def computeAnswer(queueP1, queueP2):
    if (queueP1):
        compute = queueP1
    else:
        compute = queueP2
    answer = [x * compute.popleft() for x in range(len(compute), 0, -1)]

    logging.info(answer)
    total = sum(answer)
    logging.info(total)


def helper(queueP1, queueP2, gameNumber):
    logging.debug(f'\n=== Game {gameNumber} === ')
    unique = set()
    round = 1
    while queueP1 and queueP2:
        logging.debug(f'-- Round {round} (Game {gameNumber}) --')
        logging.debug(f"Player 1's deck: {list(queueP1)}")
        logging.debug(f"Player 2's deck: {list(queueP2)}")
        hashID = (str(list(queueP1)), str(list(queueP2)))

        # first rule of part two
        if (hashID in unique):
            logging.debug('these two decks appear before, player 1 win')
            return True
        else:
            cardP1 = queueP1.popleft()
            cardP2 = queueP2.popleft()
            logging.debug(f'Player 1 plays: {cardP1}')
            logging.debug(f'Player 2 plays: {cardP2}')

            if (cardP1 <= len(queueP1) and cardP2 <= len(queueP2)):
                logging.debug('Playing a sub-game to determine the winner...')
                p1Won = helper(deque(list(queueP1)[:cardP1]), deque(
                    list(queueP2)[:cardP2]), gameNumber+1)
                if (p1Won):
                    logging.debug(
                        f'Player 1 wins round {round} of game {gameNumber}!')
                    queueP1.append(cardP1)
                    queueP1.append(cardP2)
                else:
                    logging.debug(
                        f'Player 2 wins round {round} of game {gameNumber}!')
                    queueP2.append(cardP2)
                    queueP2.append(cardP1)
            elif (cardP1 > cardP2):
                logging.debug(
                    f'Player 1 wins round {round} of game {gameNumber}!')
                queueP1.append(cardP1)
                queueP1.append(cardP2)
            else:
                logging.debug(
                    f'Player 2 wins round {round} of game {gameNumber}!')
                queueP2.append(cardP2)
                queueP2.append(cardP1)

        unique.add(hashID)
        round += 1
        logging.debug('\n')

    logging.debug(f'...anyway, back to game {gameNumber-1}')
    if (gameNumber == 1):
        # logging.info(queueP1)
        # logging.info(queueP2)
        computeAnswer(queueP1, queueP2)
    if (queueP1):
        # logging.debug(queueP1)
        return True
    else:
        # logging.debug(queueP2)
        return False


def p2():
    queueP1 = deque(p1Deck)
    queueP2 = deque(p2Deck)
    helper(queueP1, queueP2, 1)


p1()
p2()
