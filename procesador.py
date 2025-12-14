import re
import csv

PATRON = re.compile(
    r'^(?P<nombre>[A-Za-zÁÉÍÓÚáéíóúñÑ\s]+)\s*-\s*'
    r'(?P<email>[\w\.-]+@[\w\.-]+\.\w+)\s*-\s*'
    r'(?P<edad>\d{1,3})$'
)

def validar_email(email):
    return re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email)

def procesar_usuarios(archivo_entrada, archivo_salida):
    usuarios = []

    try:
        with open(archivo_entrada, encoding="utf-8") as f:
            for linea in f:
                try:
                    match = PATRON.match(linea.strip())
                    if match and validar_email(match.group("email")):
                        usuarios.append({
                            "nombre": match.group("nombre"),
                            "email": match.group("email"),
                            "edad": match.group("edad")
                        })
                except Exception:
                    continue
    except FileNotFoundError:
        print("Archivo de entrada no encontrado")
        return

    with open(archivo_salida, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["nombre", "email", "edad"])
        writer.writeheader()
        writer.writerows(usuarios)

    print(f"Archivo generado correctamente: {archivo_salida}")

if __name__ == "__main__":
    procesar_usuarios("usuarios.txt", "usuarios_limpios.csv")
