# filename      :hello.py
# author        :Cyrus Requiro  
# description   :this is a python program   
#                that classifies a tropical
#                cyclone with its sustained winds

import sys

sustained_winds = sys.argv[1]

sustained_winds = float(sustained_winds)

if sustained_winds >= 220.0:
    print("Super Typhoon")
elif sustained_winds >= 118.0:
    print("Typhoon")
elif sustained_winds >= 89.0:
    print("Severe Tropical Storm")
elif sustained_winds >= 62.0:
    print("Tropical Storm")
else:
    print("Tropical Depression")
