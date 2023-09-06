def ArrayChallenge(strArr):
    # code goes here
    card_values = {
        "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
        "seven": 7, "eight": 8, "nine": 9, "ten": 10,
        "jack": 10, "queen": 10, "king": 10, "ace": 11
    }
    total_val = 0
    ace_count = 0
    highest_card = ""

    # Calculate total val of cards
    # Check ace

    for card in strArr:
        total_val += card_values[card]
        if card == "ace":
            ace_count += 1

        # determine highest card
        if highest_card == "":
            highest_card = card
        elif card_values[card] > card_values[highest_card]:
            highest_card = card
        elif card_values[card] == card_values[highest_card]:
            if card in ["jack", "queen", "king"] and highest_card in ["ten", "jack", "queen", "king"]:
                highest_card = max(highest_card, card, key=lambda x: ["ten", "jack", "queen", "king"].index(x))

    # Check if the total val greater than 21 and there is aces
    while total_val > 21 and ace_count > 0:
        total_val -= 10
        ace_count -= 1

        # highest_card = "ace"
    importance = {
        "jack": 2, "queen": 3, "king": 4
    }
    face = ["jack", "queen", "king"]
    filtered_cards = [card for card in strArr if card != "ace"]
    if ace_count != 0:
        highest_card = "ace"
    else:
        if all(card not in importance for card in filtered_cards):
            highest_card = max(filtered_cards, key=lambda card: card_values[card])
        else:
            highest_card = max(filtered_cards, key=lambda card: importance.get(card, 0))

    # Determine the result

    if total_val == 21:
        return f"blackjack {highest_card}"
    elif total_val < 21:
        # highest_card = max(strArr, key=lambda card: card_values[card])
        return f"below {highest_card}"
    else:
        return f"above {highest_card}"



print(ArrayChallenge(["two","three","four","five","six","ace"]))
