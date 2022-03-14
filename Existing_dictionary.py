Dictionary_values = {'Name': 'Sherlock', 'Age': 20, 'Passion': 'Singer'}

Key = input("Enter a Key Value to Check Whether its Present or Not: ")

if Key in Dictionary_values.keys():

      print("Key is Present and Key Value is:\n", Dictionary_values[Key])

else:

      print("Key is NOT Present in Dictionary")