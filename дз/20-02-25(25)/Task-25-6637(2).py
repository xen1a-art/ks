from fnmatch import fnmatch

for i in range(1021390004 - 1021390004 % 3052,10**10,3052):
    if fnmatch(str(i), '1?2139*4'):
        print(i,i//3052)