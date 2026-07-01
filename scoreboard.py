# sports-scoreboard.py

class Cricket:
    def __init__(self, player, score):
        self.__player = player
        self.__score = score

    def info(self):
        print(f"Cricket - Player: {self.__player}, Score: {self.__score}")

    def play(self):
        print(f"{self.__player} hits a six!")

    def get_score(self):
        return self.__score

    def set_score(self, new_score):
        if new_score >= 0:
            self.__score = new_score
        else:
            print("Error: Score cannot be negative.")


class Football:
    def __init__(self, player, score):
        self.__player = player
        self.__score = score

    def info(self):
        print(f"Football - Player: {self.__player}, Score: {self.__score}")

    def play(self):
        print(f"{self.__player} scores a goal!")

    def get_score(self):
        return self.__score

    def set_score(self, new_score):
        if new_score >= 0:
            self.__score = new_score
        else:
            print("Error: Score cannot be negative.")


# Create objects
cricket = Cricket("Rohit", 85)
football = Football("Arjun", 2)

# Polymorphism using a loop
for sport in [cricket, football]:
    sport.info()
    sport.play()
    print()

# Attempt to change private attribute directly
cricket.__score = 999

print("After direct change attempt:")
print("Cricket score:", cricket.get_score())  # Still 85

# Update scores safely using setter
cricket.set_score(100)
football.set_score(3)

print("\nAfter updating with setter:")
cricket.info()
football.info()