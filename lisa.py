nimi = "Pavel"
punktid = 92
puudumised = 0
tood_esitatud = "jah"

# Hinde määramine
if punktid >= 90:
    hinne = 5
elif punktid >= 75:
    hinne = 4
elif punktid >= 50:
    hinne = 3
elif punktid >= 20:
    hinne = 2
else:
    hinne = 1

print("Õpilane:", nimi)
print("Hinne:", hinne)

# Puudumiste kontroll
if puudumised > 10:
    print("Hoiatus: liiga palju puudumisi.")
else:
    print("Puudumiste arv on lubatud.")

# Tööde kontroll
if tood_esitatud == "jah":
    print("Kõik tööd on esitatud.")
else:
    print("Kõik tööd ei ole esitatud.")

# Aine läbimise kontroll
if hinne >= 3 and puudumised <= 10 and tood_esitatud == "jah":
    print("Aine on läbitud.")
else:
    print("Aine ei ole läbitud.")

# OR tingimus
if hinne == 1 or hinne == 2:
    print("Hinne on alla rahuldava.")
