study_plan = {}
total_hours = []
with open('teaching hour.txt', encoding='utf-8') as f:
    for line in (f.readlines()):
        hours = []
        study_plan[line.split()[0].strip(':')] = []
        new_number = ''
        for el in line:
            if el.isdigit():
                new_number = new_number + el
            if not el.isdigit() and new_number != '':
                hours.append(int(new_number))
                new_number = ''
        total = 0
        for hour in hours:
            total = total + hour
        total_hours.append(total)
        for num, key in enumerate(study_plan):
            study_plan[key] = (total_hours[num])
    print(study_plan)
