print("Minutes          Calories Burned")
print("--------------------------------")

for i in range(10,31,5):
    caloriesBurned = float(0)
    caloriesBurned = caloriesBurned + 3.9 * i
    print(i,"             ",caloriesBurned)
