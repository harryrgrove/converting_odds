def convert_odds(tup):
    a, b = tup[0], tup[1]
    return b / (a + b)


def find_k(odds_dict, booksum):
    lower_bound, upper_bound = 0, 2
    for repeat in range(100):
        k = (lower_bound + upper_bound) / 2
        if sum([convert_odds(odds_dict[i])**k for i in odds_dict]) > booksum:
            lower_bound = k
        else:
            upper_bound = k
    return k


FA_odds_dict = {'Man City': (4, 9),
            'Liverpool': (4, 7),
            'Chelsea': (8, 11),
            'Tottenham': (1, 1),
            'Leicester': (11, 10),
            'Arsenal': (6, 5),
            'Man United': (13, 8),
            'Sheffield Utd': (15, 8),
            'West Ham': (15, 8),
            'Burnley': (9, 4),
            'Newcastle': (9, 4),
            'Derby': (3, 1),
            'Portsmouth': (7, 2),
            'Sheffield Wednesday': (7, 2),
            'Birmingham': (4, 1),
            'QPR': (4, 1),
            'Bournemouth': (9, 2),
            'Norwich': (1, 1),
            'West Brom': (1, 1),
            'Wolves': (9, 2),
            'Brentford': (5, 1),
            'Southampton': (5, 1),
            'Barnsley': (11, 2),
            'Millwall': (11, 2),
            'Cardiff': (6, 1),
            'Reading': (6, 1),
            'Oxford Utd': (13, 2),
            'Coventry': (7, 1),
            'Northampton': (9, 1),
            'Watford': (9, 1),
            'Hull': (10, 1),
            'Blackpool': (11, 1),
            'Fulham': (12, 1),
            'Bristol City': (18, 1),
            'Bristol Rovers': (20, 1),
            'Carlisle': (28, 1),
            'Middlesbrough': (40, 1),
            'Rochdale': (40, 1),
            'Shrewsbury': (40, 1)}

k = find_k(FA_odds_dict, 8)
print('k =', k)
print('maximum difference at prob =', (1 / k) ** (1/(k - 1)))
for x, y in {i: convert_odds(FA_odds_dict[i]) ** k for i in FA_odds_dict}.items():
    print(x + ' ' * (20 - len(x)) + str(round(y, 4)))
