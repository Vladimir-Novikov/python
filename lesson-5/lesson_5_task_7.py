import json

company_list = []
name_profit = {}
average = {'average_profit': []}
with open('company.txt', encoding='utf-8') as f:
    for el in f.readlines():
        name_profit[el.split()[0]] = float(el.split()[2]) - float(el.split()[3])
    i = 0
    total = 0
    for company in name_profit:
        if name_profit[company] > 0:
            total = total + name_profit[company]
            i += 1
        average['average_profit'] = int(total / i)
    company_list.append(name_profit)
    company_list.append(average)

with open('company_list.json', 'w', encoding='utf-8') as f:
    json.dump(company_list, f)

with open('company_list.json', encoding='utf-8') as f:
    js = json.load(f)
    print(js)
