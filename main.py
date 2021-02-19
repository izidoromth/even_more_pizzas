from pizza import Pizza
from tree import *


def getFileContent(filename):
    with open(filename) as f:
        return f.readlines()


def getPizzas(content):
    p = []
    p_count = getPizzasCount(content)
    for n in range(1, p_count + 1):
        line = content[n].split()
        i_count = int(line[0])
        pizza = Pizza()
        for i in range(1, i_count + 1):
            pizza.ingredients.append(line[i])
        p.append(pizza)
    return p


def getTeams(content):
    t = []
    lineSplit = content[0].split()
    for n in range(1, len(lineSplit)):
        t.append(int(lineSplit[n]))
    return t


def getPizzasCount(content):
    return int(content[0].split()[0])


def getTeamsCount(teams_list):
    sum = 0
    for n in teams_list:
        sum += n
    return sum


def evaluatePizzas(pizzas):
    all_ingredients = []
    for p in pizzas:
        for i in p.ingredients:
            if (i in all_ingredients):
                ing_idx = all_ingredients.index(i) + 1
                all_ingredients[ing_idx] = all_ingredients[ing_idx] + 1
            else:
                all_ingredients.append(i)
                all_ingredients.append(1)
    for p in pizzas:
        for i in p.ingredients:
            ing_idx = all_ingredients.index(i)+1
            p.value += all_ingredients[ing_idx]


def findAllDeliveryPaths(trees):
    paths = []

    for root in trees:
        findTreePaths(root, paths, 0)

    return paths


def getBestDeliveryPath(paths, numPizzas):
    deliveries = []

    for path in paths:
        members = 0
        teams_count = 0
        for teams in path:
            members += teams[0] * teams[1]
            teams_count += teams[0]

        if(numPizzas >= members):
            deliveries.append({
                "members": members,
                "teams": teams_count,
                "path": path
            })

    deliveries.append({
        "members": 5,
        "teams": 3,
        "path": []
    })

    deliveries = [x for x in deliveries if x['members'] == max(
        deliveries, key=lambda x: x['members'])['members']]

    return max(deliveries, key=lambda x: x['teams'])


content = getFileContent("a_example")
teams = getTeams(content)
# teams = [2, 2, 1]

pizzasCount = getPizzasCount(content)
teamsCount = getTeamsCount(teams)

pizzas = getPizzas(content)
evaluatePizzas(pizzas)

c = createDeliveryTrees(teams, 0)

paths = findAllDeliveryPaths(c)
deliv = getBestDeliveryPath(paths, pizzasCount)

a = 0
