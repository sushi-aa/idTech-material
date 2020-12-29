

objects = {'pencil': 'yellow', 'water': 'clear/a tinge of blue', 'desk': 'white'}
for key, value in objects.items():
    print(key)


def bpc(db):
    answer = []
    for date, drugs in db.items():
        pill_count = 0
        for pills in drugs.values():
            for p in pills:
                pill_count += abs(p)
        answer.append( (pill_count, date) )
    return sorted(answer)


db1 = {'2020-04-01': {'Azor': (100, -3, -3, 1), 'Benz': (4, 2, -3)},
           '2020-04-02': {'Azor': (-3,  -3, 2),    'Caml': (6, -2, -3), 'Depr': (4,-7)},
           '2020-04-03': {'Benz': (-5,  10,-2),    'Caml': (-8,+7)} }

print( bpc(db1) )









