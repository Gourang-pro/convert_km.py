#the distance between two cities (in km.) is input through the keybord. write a program to convert and print this distance in meters, feet, inches and centimeters.

km=eval(input('Enter the km to convert: '))

meter =      km*1000
feet =       km*3280.84
inches =     km*39370.1
centimeter = km*100000

print('The {}km in meter is {}'.format(km,meter))
print('The {}km in feet is {}'.format(km,feet))
print('The {}km in inches is {}'.format(km,inches))
print('The {}km in centimeter is {}'.format(km,centimeter))
