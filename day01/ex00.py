def add_ingot(purse):
    purse["gold_ingots"] += 1
    return purse

def get_ingot(purse):
    if purse["gold_ingots"] > 0:
        purse["gold_ingots"] -= 1
        return purse
    else:
        return purse

def empty(purse):
    return {"gold_ingots": 0}


if __name__ == "__main__":
    purse = {}
    # new_purse = empty(purse)
    print(add_ingot(get_ingot(add_ingot(empty(purse)))))