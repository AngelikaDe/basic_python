def split_booty(*purses):
    purse_res = {}
    for purse in purses:
        if "gold_ingots" in purse.keys() and purse["gold_ingots"] >= 0:
            # print(purse)
            purse_res.update(purse)
    print(purse_res)
    return purse_res



if __name__ == "__main__":
    # print(split_booty({"gold_ingots":3}, {"gold_ingots":2}))
    split_booty({"gold_ingots":3}, {"gold_ingots":2})