class Dogs:
    def __init__(self, name, breed, location):
        self.name = name
        self.breed = breed
        self.location = location
        self.tricks = []
    def learn_tricks (self, trick):
        if trick not in self.tricks:
            self.tricks.append(trick)
            print(f"WooW 💪💪 {self.name} learn a new trick {trick}")
        else:
            print(f"{self.name} already know this {trick} trick")

dogOtter = Dogs('Otter', 'German', 'Liverpool')

dogOtter.learn_tricks('stay')
dogOtter.learn_tricks('sit')
dogOtter.learn_tricks('sit')

print(dogOtter.tricks)

