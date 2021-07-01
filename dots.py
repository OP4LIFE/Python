# pikica, dve pikici, tri pikice, ..., dvajset pikic, devetnajst pikic, osemnajst pikic,...
dot = '.'
by = 1
repeated = 1
while repeated <= 3:
    print(dot*by)
    by = by + 1
    if by == 37:
        while by >= 2:
            by = by - 1
            print(dot*by)
        repeated = repeated + 1
