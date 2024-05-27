import csv
from Hero import Hero
from Villain import Villain
from Child_of_Good import NonHumanHero
from child_of_evil import RedHairedVillain


def create_character(row):
    name = row['Name']
    intelligence = int(row['Intelligence'])
    strength = int(row['Strength'])
    speed = int(row['Speed'])
    durability = int(row['Durability'])
    power = int(row['Power'])
    combat = int(row['Combat'])
    alignment = row['Alignment']
    race = row['Race']
    hair_color = row['Hair color']

    if alignment == 'good':
        if race != 'Human':
            return NonHumanHero(name, intelligence, strength, speed, durability, power, combat, race)
        else:
            return Hero(name, intelligence, strength, speed, durability, power, combat, race)
    elif alignment == 'bad':
        if hair_color == 'Red':
            return RedHairedVillain(name, intelligence, strength, speed, durability, power, combat, race, hair_color)
        else:
            return Villain(name, intelligence, strength, speed, durability, power, combat, race, hair_color)
    else:
        return None


def battle_royale(characters):
    results = {char._name: {'wins': 0, 'losses': 0, 'ties': 0} for char in characters}

    for i in range(len(characters)):
        for j in range(i + 1, len(characters)):
            char1 = characters[i]
            char2 = characters[j]
            score1 = char1.getStats() + char1.getBonus()
            score2 = char2.getStats() + char2.getBonus()

            if score1 > score2:
                results[char1._name]['wins'] += 1
                results[char2._name]['losses'] += 1
            elif score1 < score2:
                results[char1._name]['losses'] += 1
                results[char2._name]['wins'] += 1
            else:
                results[char1._name]['ties'] += 1
                results[char2._name]['ties'] += 1

    return results


def report_results(results):
    best_record = max(results.items(), key=lambda x: (x[1]['wins'] + 0.5 * x[1]['ties']))
    worst_record = min(results.items(), key=lambda x: (x[1]['wins'] + 0.5 * x[1]['ties']))

    for name, result in results.items():
        print(f"{name}: {result['wins']} wins, {result['losses']} losses, {result['ties']} ties")

    print(f"Best record: {best_record[0]} with {best_record[1]['wins']} wins and {best_record[1]['ties']} ties")
    print(f"Worst record: {worst_record[0]} with {worst_record[1]['losses']} losses and {worst_record[1]['ties']} ties")



# Main code
file_path = '../SuperpowerDataset.csv'  # Update this path as needed

with open(file_path) as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')
    characters = [create_character(row) for row in reader if create_character(row) is not None]

results = battle_royale(characters)
report_results(results)
