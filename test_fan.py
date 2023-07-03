# test programs on a diff file
from fan_class import Fan

# fan_1 = max speed, radius 10, yellow, on 
Dowell = Fan("Dowell", 3, 10, "Yellow")
Dowell.turn_on()
Dowell.show()
# fan_2 = medium speed, radius 5, color blue, off
Akari = Fan("Akari", 2, 5, "Blue")
Akari.turn_off()
Akari.show()

