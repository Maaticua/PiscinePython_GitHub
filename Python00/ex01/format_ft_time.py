import time
import datetime

sec = time.time()
date = datetime.datetime.fromtimestamp(sec)

print(f"Seconds since January 1, 1970: {sec:,.4f} or {sec:.2e} in scientific notation")
print(date.strftime("%b %d %Y"))


# Various Notes:
"""
Format the date and time:
%d = day "30"
%m = month "12"
%y = year "99"
%Y = year "1999"
%a = weekday "Mon"
%A = weekday "Monday"
%b = month "Dec"
%B = month "December"

---

%H = hour "23"
%M = minute "59"
%S = second "59"

---

NumPy = a library for working with arrays and mathematical operations in Python.
Pandas = a library for data manipulation and analysis in Python.

---

date = datetime.datetime.fromtimestamp(sec)
       [module].[classe].[fonction/méthode]

---

f = float "deciaml"
e = exponential "science shi"

"""
# https://www.w3schools.com/python/python_ref_modules.asp