def split_booty(*purses):
    purse_res = []
    number_of_ingots = []
    for purse in purses:
        if "gold_ingots" in purse.keys() and purse["gold_ingots"] >= 0:
            number_of_ingots.append(purse["gold_ingots"])
            purse_res.append(purse)
            print(number_of_ingots)
    return purse_res


if __name__ == "__main__":
    print(split_booty({"gold_ingots":3}, {"gold_ingots":2}, {"gold_ingots":-10}))