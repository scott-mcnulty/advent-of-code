import math

def run():
    masses = [line.rstrip('\n') for line in open('data')]
    fuels = [calculate_module_fuel(int(mass)) for mass in masses]
    print(sum(fuels))


def calculate_module_fuel(mass: int):
    return math.floor(mass / 3) - 2


if __name__ == '__main__':
    run()