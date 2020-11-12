def createuser(**profile):
    return profile


def printUser(user):
    for k, v in user.items():
        print(f"{k}: v")


printUser(createuser)
