def roll_call_dwarves(dwarf_names):
    for index, name in enumerate(dwarf_names):
        print(f"{index + 1}. {name}")

def summon_captain_planet(veggies):
    return [veggie.capitalize() + '!' for veggie in veggies]

def long_planeteer_calls(calls):
        return any(len(call) > 4 for call in calls)

def find_the_cheese(snacks):
    cheese_types = ["cheddar", "gouda", "camembert"]
    for snack in snacks:
        if snack in cheese_types:
            return snack
    return None