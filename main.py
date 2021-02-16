from pizza import Pizza

def getFileContent(filename):
    with open(filename) as f:
        return f.readlines()

def getPizzas(content):
    p = []
    p_count = getPizzasCount(content)   
    for n in range(1,p_count+1):
        line = content[n].split()
        i_count = int(line[0])
        pizza = Pizza()
        for i in range(1, i_count+1):
            pizza.ingredients.append(line[i])    
        p.append(pizza)
    return p

def getTeams(content):
    t = []
    lineSplit = content[0].split()
    for n in range(1,len(lineSplit)):
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
                ing_idx = all_ingredients.index(i)+1
                all_ingredients[ing_idx] = all_ingredients[ing_idx]+1
            else:
                all_ingredients.append(i)
                all_ingredients.append(1)
    for p in pizzas:
        for i in p.ingredients:
            ing_idx = all_ingredients.index(i)+1
            p.value += all_ingredients[ing_idx]

content = getFileContent("a_example")
teams = getTeams(content) 
pizzasCount = getPizzasCount(content)
teamsCount = getTeamsCount(teams)

pizzas = getPizzas(content)
evaluatePizzas(pizzas)

a = 0
