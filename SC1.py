#Name: Tucker Hooper
#Class: 6th Hour
#Assignment: Scenario 1

#Scenario 1:
#You are a programmer for a fledgling game developer. Your team lead has asked you
#to create a nested dictionary containing five enemy creatures (and their properties)
#for combat testing. Additionally, the testers are asking for a way to input changes
#to the enemy's damage values for balancing, as well as having it print those changes
#to confirm they went through.

#Other than damage which is required, it is up to you to decide what properties are
#important and the theme of the game.
enemies= {
    "Mara from Persona" : {
        "LVL": 13,
        "DMG": 65,
        "HP" : 175,
        "Location" : "Arena"
    },

    "Keith" : {
        "LVL": 20,
        "DMG": 115,
        "HP" : 325,
        "Location" : "Cave"},
    "Jack Baker" : {
        "LVL": 25,
        "DMG": 175,
        "HP" : 400,
        "Location" : "House"},
    "Lucas Baker" : {
        "LVL": 10,
        "DMG": 50,
        "HP" : 140,
        "Location" : "Circus"},
    "Ethan Winters" : {
        "LVL": 100,
        "DMG": 700,
        "HP" : 1600,
        "Location" : "Guest House"},

}
enemies["Mara from Persona"]["DMG"] =int(input("Mara from PersonaDMG"))
print(enemies["Mara from Persona"])
enemies["Keith"]["DMG"] =int(input("KeithDMG"))
print(enemies["Keith"])
enemies["Jack Baker"]["DMG"] =int(input("Jack BakerDMG"))
print(enemies["Jack Baker"])
enemies["Lucas Baker"]["DMG"] =int(input("Lucas BakerDMG"))
print(enemies["Lucas Baker"])
enemies["Ethan Winters"]["DMG"] =int(input("Ethan WintersDMG"))
print(enemies["Ethan Winters"])