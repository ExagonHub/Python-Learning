# This script converts a distance from kilometers to miles.

km = input('Km: ')
mi = float(km) / 1.609344
mi = round(mi, 2)    

print(km + ' Km= ' + str(mi) + ' Mil')
