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
year = int(0) #Input year
month = int(0) #Input month
day = int(0) #Input day
hour = int(0) #Input hour
minute = int(0) #Input minute
second = float('nan') #Input second

#Arguments are strings by default
if len(sys.argv) == 7:
   year = int(sys.argv[1])
   month = int(sys.argv[2])
   day = int(sys.argv[3])
   hour = int(sys.argv[4])
   minute = int(sys.argv[5])
   second = float(sys.argv[6])
else:
   print('Usage: python3 ymdhms_to_jd.py year month day hour minute second')
   sys.exit()

#Main body of script
jd = day - 32075.0 \
     + int(1461.0 * (year + 4800.0 + int((month - 14.0) / 12.0)) / 4.0) \
     + int(367.0 * (month - 2.0 - int((month - 14.0) / 12.0) * 12.0) /12.0) \
     - int(3.0 * (int((year + 4900.0 + int((month - 14.0) / 12.0)) / 100.0)) / 4.0)

jd_mid = jd - 0.5
d_frac = (second + 60 * (minute + 60 * hour)) / 86400
jd_frac = jd_mid + d_frac

print(jd_frac)
