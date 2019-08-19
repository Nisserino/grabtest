facit = [25, 15, 76.5, 150, 20, 30, 6, 180, 30, 40]

def floatToPercent (num):
   return str(float(num * 100)) + "%"

print("Hello!")

name = "start"

for letter in name : 
   name = input("Name : ")

   if name == "done":
      break
   else:
      bshrimp = float(input("Big soup-shrimp : "))
      sshrimp = float(input("Small soup-shrimp : "))
      mexi = float(input("Mexi : "))
      broccoli = float(input("Broccoli for the salad : "))
      onion = float(input("Burger onion : "))
      paprika = float(input("Caesar paprika : "))
      granade = float(input("Salad granade : "))
      fries = float(input("Sweet potato fries : "))
      kale = float(input("Wok kale : "))
      cheese = float(input("Fajita cheese : "))

      result1 = bshrimp / facit[0]
      result2 = sshrimp / facit[1]
      result3 = mexi / facit[2]
      result4 = broccoli / facit[3]
      result5 = onion / facit[4]
      result6 = paprika / facit[5]
      result7 = granade / facit[6]
      result8 = fries / facit[7]
      result9 = kale / facit[8]
      result10 = cheese / facit[9]
      average = (
            (result1 +
            result2 + 
            result3 + 
            result4 + 
            result5 + 
            result6 +
            result7 +
            result8 +
            result9 +
            result10 ) / 10 
         )

      with open('results.txt', 'a+') as f:
         line = (
            name, 
            floatToPercent(result1), 
            floatToPercent(result2), 
            floatToPercent(result3), 
            floatToPercent(result4), 
            floatToPercent(result5), 
            floatToPercent(result6), 
            floatToPercent(result7), 
            floatToPercent(result8), 
            floatToPercent(result9), 
            floatToPercent(result10),
            floatToPercent(average)
            )
         f.write(str(line) + "\n")