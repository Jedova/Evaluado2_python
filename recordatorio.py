
##Lista de los recordatorios iniciales##
recordatorios = [
    ["2021-01-01", "11:00", "Levantarse y ejercitar"],
    ["2021-07-15", "13:00", "No hacer nada es feriado"],
    ["2021-09-18", "16:00", "Ramadas"],
    ["2021-12-25", "00:00", "Navidad"],
    ["2021-05-01", "08:00", "Día del Trabajo"]
]

##1. Agregar evento del 2 de febrero##
recordatorios.append(["2021-01-02", "06:00", "Empezar el año"])

##2. Corregir fecha del 15 de julio (feriado mal asignado)##
for evento in recordatorios:
    if evento[0] == "2021-07-15":
        evento[0] = "2021-07-16"

##3. Este feriado se debe eliminar  por que me toca trabajar "Día del Trabajo: 1 de mayo"##
recordatorios = [evento for evento in recordatorios if evento[0] != "2021-05-01"]

##4. Agregar cenas de Navidad y Año Nuevo##
recordatorios.append(["2021-12-24", "22:00", "Cena de Navidad"])
recordatorios.append(["2021-12-31", "22:00", "Cena de Año Nuevo"])

recordatorios.sort(key=lambda x: (x[0], x[1]))

for evento in recordatorios:
    print(evento)
