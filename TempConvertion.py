# Python function to convert temperatures to and from celsius, fahrenheit.
#  [ Formula : c/5 = f-32/9 [where c = temperature in celsius and f = temperature in fahrenheit ]
#Expected Output :
"""60°C is 140 in Fahrenheit
45°F is 7 in Celsius
"""
#temperature input in either c or f
temp = input("Input the  temperature, please add either 'F' after the integer for fahrenheit or 'C' for celcious; ")
degree = int(temp[:-1])
i_convention = temp[-1]

if i_convention.upper() == "C":
  result = int(round((9 * degree) / 5 + 32))
  o_convention = "Fahrenheit"
elif i_convention.upper() == "F":
  result = int(round((degree - 32) * 5 / 9))
  o_convention = "Celsius"
else:
  print("Input proper convention.")
  quit()

print((temp[:-1]),u'\N{DEGREE SIGN}',temp[-1],"is",result,"in", o_convention)
#end of program