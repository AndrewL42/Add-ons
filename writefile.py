import os
import datetime

date_and_time = datetime.datetime.now()
date = (date_and_time.strftime("%Y-%m-%d %H-%M"))
full_date = ((date_and_time.strftime("%Y-%m-%d %H:%M:%S")))
fileName = str(date + ".csv")

if os.path.exists(fileName):
    append_write = "a"
else:
    append_write = "w"

f = open(fileName, append_write)
f.write("INFORMATION_HERE, " + str(full_date) + "\n")
f.close()



