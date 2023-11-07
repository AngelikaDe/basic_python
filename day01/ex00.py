def sqeak(func):
    def wrapper(*args):
        return func(*args)
    print("SQEAK")
    return wrapper

@sqeak
def add_ingot(purse):
    purse["gold_ingots"] += 1
    return purse

@sqeak
def get_ingot(purse):
    if purse["gold_ingots"] > 0:
        purse["gold_ingots"] -= 1
        return purse
    else:
        return purse

@sqeak
def empty(purse):
    return {"gold_ingots": 0}

# if __name__ == "__main__":
#     purse = {'gold_ingots': 10}
#     print(add_ingot(get_ingot(add_ingot(purse))))