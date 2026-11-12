print("Tartu Rakenduslik Kolledž")
print("Õpilase päev") 

nimi = input("Sisesta oma nimi: ")
vanus = int(input("Sisesta vanus: "))
koolitee = float(input("Sisesta koolitee pikkus kilomeetrites: "))
aeg = int(input("Sisesta koolitee kestus minutites: "))

jargmine_vanus = vanus + 1
meetrites = koolitee * 1000
tunnid = aeg // 60
minutid = aeg % 60
kiirus = koolitee / (aeg / 60)

print("Tere, " + nimi + "!")
print("Järgmisel aastal oled", jargmine_vanus, "aastane.")
print("Sinu koolitee pikkus on", meetrites, "meetrit.") 
print("Koolitee kestab", tunnid, "tundi ja", minutid, "minutit.")
print("Keskmine kiirus on", round(kiirus, 1), "km/h.")
