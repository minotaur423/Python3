# Fahrenheit to Celsius
# You are to write program to convert degrees of Fahrenheit to Celsius.
#import math
def temp_conv(temp):
    return (temp - 32) * 5/9
    
temperatures = '545 305 576 325 380 245 43 441 439 411 399 579 448 233 538 38 261 476 295 566 326 419 453 566 278 397 454 376 461 43 259 406 317 235 131 97 448 142'
temp_list = temperatures.split(' ')
for reading in temp_list:
    #print(math.ceil(temp_conv(int(reading))), end=' ')
    print(round(temp_conv(int(reading))), end=' ')