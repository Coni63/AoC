import itertools


def eval_hand(hand):
    counts = [hand.count(card) for card in hand]

    if 5 in counts:  # 5 of a kind
        return 6
    if 4 in counts:  # 4 of a kind
        return 5
    elif {3, 2} & set(counts) == {3, 2}:  # full house
        return 4
    elif 3 in counts:  # 3 of a kind
        return 3
    if counts.count(2) == 4:  # 2 pairs
        return 2
    if 2 in counts:  # 1 pair
        return 1
    return 0


def score_card(card, version=1):
    if version == 1:
        return '23456789TJQKA'.index(card)
    else:
        return 'J23456789TQKA'.index(card)


def replacements(hand, version=1):
    if version == 1:
        yield hand
        return

    idx_joker = [i for i, card in enumerate(hand) if card == "J"]

    if len(idx_joker) == 0:
        yield hand
        return

    for swap in itertools.combinations_with_replacement("23456789TQKA", len(idx_joker)):
        new_hand = hand[:]
        for i, card in zip(idx_joker, swap):
            new_hand[i] = card
        yield new_hand


bets = []
VERSION = 1
with open('input07.txt') as f:
    lines = f.readlines()
    for line in lines:
        hand, bid = line.split(' ')
        bid = int(bid)
        hand = list(hand)

        score_card_hand = [score_card(card, version=VERSION) for card in hand]
        max_score_hand = max(eval_hand(new_hand) for new_hand in replacements(hand, version=VERSION))

        bets.append((max_score_hand, score_card_hand, bid, hand))

    bets.sort()

    ans = sum(idx * bid for idx, (_, _, bid, _) in enumerate(bets, start=1))
    print(ans)
