def rand_word():
    with open("palavras.txt", "rt"):
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()

print(rand_word())
