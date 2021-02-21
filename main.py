class Pizza:
    def __init__(self):
        self.value = 0
        self.ingredients = []

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
                all_ingredients[ing_idx] += 1
            else:
                all_ingredients.append(i)
                all_ingredients.append(1)
    for p in pizzas:
        for i in p.ingredients:
            ing_idx = all_ingredients.index(i)+1
            p.value += all_ingredients[ing_idx]

def isEven(x):
    return x % 2 == 0

def getTeamsToDeliver(teams, num_pizzas):
    total_members = teams[0]*2 + teams[1]*3 + teams[2]*4

    if(num_pizzas >= total_members):
        return teams
    else:
        if(num_pizzas <= teams[0]*2):
            if(isEven(num_pizzas)):
                return [int(num_pizzas/2), 0, 0]
            elif(teams[1] > 0):
                return [int(num_pizzas/2)-1, 1,0]
            else:
                return [int(num_pizzas/2), 0,0]
        elif(num_pizzas <= (teams[0]*2 + teams[1]*3)):
            pizzas_remaining = num_pizzas - teams[0]*2
            if(pizzas_remaining % 3 == 0):
                return [teams[0], int(pizzas_remaining/3), 0]
            elif(teams[2] > 0):
                return [teams[0] - 1, int(pizzas_remaining/3), 1]
            else:
                return [teams[0], int(pizzas_remaining/3), 0]
        else:
            pizzas_remaining = num_pizzas - teams[0]*2 - teams[1]*3
            if(pizzas_remaining % 4 == 0):
                return [teams[0], teams[1], int(pizzas_remaining/4)]
            elif(teams[2] > int(pizzas_remaining/4)):
                if(isEven(num_pizzas)):
                    return [teams[0] - 1, teams[1], int(pizzas_remaining/4) + 1]
                else:
                    return [teams[0], teams[1] - 1, int(pizzas_remaining/4) + 1]

def generateOutput(filename, teams_delivered, deliveries, pizzas):
    f = open(filename + "_output", "w")
    f.write(str(teams_delivered) + "\n")
    for team in deliveries:
        line = str(team['team_type']) + " "
        for i in range(0, team['team_type']):
            line += str(pizzas.index(team['pizzas'][i])) + " "
        f.write(line + "\n")
    f.close()

def solve(filename):
    content = getFileContent(filename)
    teams = getTeams(content)    
    pizzas = getPizzas(content)
    evaluatePizzas(pizzas)

    teams_to_deliver = getTeamsToDeliver(teams, getPizzasCount(content))

    deliveries = []
    for i in range(0, 3):
        for j in range(0, teams_to_deliver[i]):
            deliveries.append({"team_type": i + 2, "pizzas" : []})

    pizzas_sorted = pizzas.copy()
    pizzas_sorted.sort(key=lambda x: x.value)

    members_receiving = teams_to_deliver[0]*2 + teams_to_deliver[1]*3 + teams_to_deliver[2]*4
    teams_receiving = teams_to_deliver[0] + teams_to_deliver[1] + teams_to_deliver[2]

    i = 0
    deliveries.reverse()
    for j in range(0, members_receiving):        

        while(i < teams_receiving and len(deliveries[i]['pizzas']) >= deliveries[i]['team_type']):
            i += 1

        if(i == teams_receiving):
            i = 0

        deliveries[i]['pizzas'].append(pizzas_sorted[j])

        i += 1
    
    generateOutput(filename, teams_receiving, deliveries, pizzas)

solve("a_example")
solve("b_little_bit_of_everything.in")
solve("c_many_ingredients.in")
solve("d_many_pizzas.in")
solve("e_many_teams.in")