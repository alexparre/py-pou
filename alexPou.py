import random

class Pou:
    def __init__(self, name):
        self.name = name
        self.age = 1
        self.hunger = 50
        self.energy = 50
        self.happiness = 50
        self.health = 100
        self.alive = True

    def status(self):

        print("Age:", self.age)
        print("Hunger:", self.hunger)
        print("Energy:", self.energy)
        print("Happiness:", self.happiness)
        print("Health:", self.health)

    def __str__(self):
        return f"{self.name} - hunger: {self.hunger}, energy: {self.energy}, happiness: {self.happiness}, health: {self.health}, age: {self.age}"

    def check_status(self):
        self.hunger = max(-10, min(self.hunger, 100))
        self.energy = max(-10, min(self.energy, 100))
        self.happiness = max(0, min(self.happiness, 100))
        self.health = max(0, min(self.health, 100))
        if self.hunger <= 0 or self.energy <= 0 or self.health <= 0 or self.age >= 18:
            self.alive = False

    def play(self):
        print(f"{self.name} is playing.")
        self.hunger -= 10
        self.energy -= 20
        self.happiness += 30
        self.health += 10
        self.check_status()

    def eat(self):
        print(f"{self.name} is eating.")
        self.hunger += 20
        self.energy += 30
        self.happiness += 20
        self.check_status()

    def take_rest(self):
        print(f"{self.name} is resting.")
        self.energy += 80
        self.health += 50
        self.happiness += 60
        self.check_status()

    def smoke_joints(self):
        print(f"{self.name}  (-_-) is High!")
        self.happiness += 85
        self.energy -= random.randint(10,20)
        self.hunger -= random.randint(5,50)
        self.health -= 5
        self.check_status()

def gameover():
    print("╔═══════════════════════════╗")
    print("║         GAME OVER!        ║")
    print("╚═══════════════════════════╝")

def print_menu():
    print("╔═══════════════════════════╗")
    print("║  What do you want to do?  ║")
    print("╠═══════════════════════════╣")
    print("║ 1 Play      2 Eat         ║")
    print("║ 3 Rest      4 Smoke Joint ║")
    print("║        5 - Exit           ║")
    print("╚═══════════════════════════╝")


pet = Pou(input("Welcome to Pou game, please insert your Pou's name: "))
rest_count = 0

while pet.alive:
        print_menu()
        choice = input("Choose one: ")

        if choice == "1":
            pet.play()
            rest_count = 0
        elif choice == "2":
            pet.eat()
            rest_count = 0
        elif choice == "3":
            pet.take_rest()
            rest_count += 1
            if rest_count == 2:
                pet.age += 1
                print("Your creature has aged by 1 year!")
                rest_count = 0
        elif choice == "4":
            pet.smoke_joints()
            rest_count = 0
        elif choice == "5":
            break
        else:
            print("Invalid input")

        pet.status()

if not pet.alive:
        gameover()
        print("Your pou died! (X.X) ")