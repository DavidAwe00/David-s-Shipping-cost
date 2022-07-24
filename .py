# Simple python program that calculates a customers price and displays the price of the shipping -
# Lab practice source --- codecademy 
weight = 8.4

# "Ground Shipping"

if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight > 2 or weight <= 6:
  cost_ground = weight * 3 + 20
elif weight > 6 or weight <= 10:
  cost_ground = weight * 4 + 20
elif weight > 10:
  cost_ground = weight * 4.75 +20
else: 
  print("Print not available!")

print("Your ground Shipping cost $"+ str(cost_ground))

cost_ground_premium = 125.00 

print("Your Premium Ground Shippng cost is $", cost_ground_premium)

#"Drone Shipping"

if weight <= 2:
  cost_ground = weight * 4.5 
elif weight > 2 or weight <= 6:
  cost_ground = weight * 9
elif weight > 6 or weight <= 10:
  cost_ground = weight * 12
elif weight > 10:
  cost_ground = weight * 14.25
else:
  print("Invalid Number printed!")
  
