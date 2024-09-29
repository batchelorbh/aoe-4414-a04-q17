#!/usr/bin/env python
# ymdhms_to_jd.py
#
# Converts year, month, day, hour, minute, second to fraction Julian date
#
# Usage: python3 ymdhms_to_jd.py year month day hour minute second
#
# Written by Blake Batchelor, batchelorbh@vt.edu
# Other contributors: none
#
# Parameters:
#    year                input year
#    month               input month
#    day                 input day
#    hour                input hour
#    minute              input minute
#    second              input second
#
# Output:
#    jd_frac             fractional julian date
#
# Revision history:
#    09/29/2024          Script created
#
###############################################################################

#Import relevant modules
import sys
from math import floor

#Pre-initialize input parameters
year = float('nan') #Input year
month = float('nan') #Input month
day = float('nan') #Input day
hour = float('nan') #Input hour
minute = float('nan') #Input minute
second = float('nan') #Input second

#Arguments are strings by default
if len(sys.argv) == 7:
   year = float(sys.argv[1])
   month = float(sys.argv[2])
   day = float(sys.argv[3])
   hour = float(sys.argv[4])
   minute = float(sys.argv[5])
   second = float(sys.argv[6])
else:
   print('Usage: python3 ymdhms_to_jd.py year month day hour minute second')
   sys.exit()

#Main body of script
jd1 = day - 32075
jd2 = 1461 * (year + 4800 + (month - 14) / 12) / 4
jd3 = 367 * (month - 2 - (month - 14) / 12 * 12) / 12
jd4 = -3 * ((year + 4900 + (month - 14) / 12) / 100) / 4

jd = jd1 + jd2 + jd3 + jd4

jd_mid = jd - 0.5
d_frac = (second + 60 * (minute + 60 * hour)) / 86400
jd_frac = "%.1f" % floor(jd_mid + d_frac)

print(jd_frac)
