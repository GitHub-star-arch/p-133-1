from opcode import stack_effect
import pandas as pd
import csv

elist=[]
with open('cleanedstarsdata.csv', 'r') as f:
    r=csv.reader(f)
    for row in r:
        elist.append(row)
header=elist[0]
star_data=elist[1:]
print(header)
print(len(star_data))

temp_star_data=list(star_data)
for i in temp_star_data:
    star_mass=i[3]
    star_radius=i[4]
    if star_mass.lower()=='unknown':
       star_data.remove(i)
       continue
    else:
        star_newmass_val=float(star_mass)*1.989e+30
        i[3]=star_newmass_val
    if star_radius.lower()=='unknown':
        star_data.remove(i)
        continue
    else:
        #bug start
        star_newradius_val=float(star_radius)*6.957e+8
        #bug end
        i[4]=star_newradius_val
print(len(star_data))

grav_list=[]
for i in star_data:
    g=6.67e-11*(float(i[3])/(float(i[4])*float(i[4])))
    grav_list.append(g)
print(grav_list)