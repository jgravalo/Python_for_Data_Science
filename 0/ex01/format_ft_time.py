import time

seconds = time.time()
result = time.localtime(seconds)
scientific_notation="{:e}".format(seconds)
#print("result:", result)
print("Seconds since January 1, 1970:", seconds, "or", "{:e}".format(seconds), "in scientific notation")
print(result.tm_mon, result.tm_mday, result.tm_year)
#print("tm_hour:", result.tm_hour)