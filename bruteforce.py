from time import time
import csv

actions = [["1", 20, 0.05], ["2", 30, 0.1], ["3", 50, 0.15], ["4", 70, 0.2], ["5", 60, 0.17], ["6", 80, 0.25],
           ["7", 22, 0.07], ["8", 26, 0.11], ["9", 48, 0.13], ["10", 34, 0.27], ["11", 42, 0.17], ["12", 110, 0.09],
           ["13", 38, 0.23], ["14", 14, 0.01], ["15", 18, 0.03], ["16", 8, 0.08], ["17", 4, 0.12], ["18", 10, 0.14],
           ["19", 24, 0.21], ["20", 114, 0.18]]
t1 = time()
argent = 500
# Initialisation du csv
fields = ['bénefice']
for item in actions:
    fields.append(item[0])
with open('solutions.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)

print('début du dénombrement')


def denombrement(dic, thune, res):
    if len(dic) == 0:  # S'il n'y a plus d'actions à envisager on calcul le bénéfice et on ajoute la solution au csv
        benefice = 0
        for action in res:
            benefice += action[0][1] * action[0][2] * action[1]
        listtemp = [benefice]
        for action in res:
            listtemp.append(action[1])
        with open('solutions.csv', 'a') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(listtemp)
    else:  # On selection la première action et on réapelle la fonction sans l'acheter et en l'achetant s'il reste
        # assez d'argent
        action_selected = dic[0]
        newdic = list(dic)
        newdic.pop(0)
        res0 = list(res)
        res0.append([action_selected, 0])
        denombrement(newdic, thune, res0)
        if thune >= action_selected[1]:
            res1 = list(res)
            res1.append([action_selected, 1])
            denombrement(newdic, thune - action_selected[1], res1)


denombrement(actions, argent, [])

print('fin du dénombrement')


def calcul():
    benefice = 0.0
    res = []
    n = 0
    with open('solutions.csv', 'r') as CSVFILE:
        csvreader = csv.reader(CSVFILE)
        for ligne in csvreader:
            if n == 0:
                n += 1
            else:
                n += 1
                if float(ligne[0]) > benefice:
                    benefice = float(ligne[0])
                    res = ligne
    print('Il y a ' + str(n) + ' possibilités')
    return res


def affichage(solution):
    prix = 0
    res = "La meilleur possibilité est d'acheter les actions : "
    for i in range(len(solution)-1):
        if solution[i+1] == '1':
            res += actions[i][0] + ', '
            prix += actions[i][1]
    res += ' pour un bénéfice de ' + str(round(float(solution[0]), 2)) + ' euros et un prix de ' + str(prix) + ' euros.'
    return res


print(affichage(calcul()))

t = time() - t1
print("le programme a mit", round(t), "s à s'éxecuter")
