import sys

# Validar que ingresen exactamente 4 argumentos
if len(sys.argv) != 5:
    print("Debe ingresar: python conversiones.py <tasa_sol> <tasa_peso_arg> <tasa_dolar> <valor_en_pesos_chilenos>")
    sys.exit(1)

try:
    tasas = {
        "Solperuano": float(sys.argv[1]),
        "PesoArgentino": float(sys.argv[2]),
        "DólarAmericano": float(sys.argv[3]),
    }

    pesos_CLP = float (sys.argv[4])

    print(f"Los {pesos_CLP:.0f} pesos equivalen a:")
    for moneda, i in tasas.items():
        convertido = pesos_CLP * i
        print(f"{convertido:.1f} {moneda}")

except ValueError:
    print("Error: Asegúrate de ingresar solo números (float o int) como argumentos.")
    sys.exit(1)