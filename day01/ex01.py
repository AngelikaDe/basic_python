from ex00 import add_ingot, get_ingot, empty, sqeak


@sqeak
def split_booty(*purses):
    purse_res = []
    prev_number = purses[0].get("gold_ingots", 1)

    for purse in purses:
        if "gold_ingots" in purse.keys():
            gold_ingots_curr = purse.get("gold_ingots")
        else:
            purse = empty(purse)
            gold_ingots_curr = 0
        if gold_ingots_curr > prev_number:
            while gold_ingots_curr > prev_number:
                purse = get_ingot(purse)
                prev_number += 1
        elif gold_ingots_curr < prev_number:
            while gold_ingots_curr < prev_number:
                purse = add_ingot(purse)
                prev_number -= 1
        purse_res.append(purse)

    if purse_res[-2].get("gold_ingots") == purse_res[-1].get("gold_ingots"):
        add_ingot(purse_res[-1])
    return purse_res


# if __name__ == "__main__":
#     purses = [{"gold_ingots": 0}, {"ggold_ingots_currold_ingots": 0}, {"apples": 10}]
#     purses = [{"gold_ingots": 3}, {"gold_ingots": 2}, {"apples": 10}]
#     result = split_booty(*purses)
#     print(result)