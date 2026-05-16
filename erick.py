import os
import requests
import json

# Colores para la terminal (Estilo Termux)
GREEN = "\033[92m"
RED = "\033[91m"
BLUE = "\033[94m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def banner():
    print(f"{BLUE}==================================={RESET}")
    print(f"{GREEN}          GHOST TRACKER            {RESET}")
    print(f"{BLUE}==================================={RESET}")
    print(f"{YELLOW}[+] Rastreador de IP y Teléfono{RESET}")
    print(f"{YELLOW}[+] Solo con fines educativos{RESET}")
    print(f"{BLUE}==================================={RESET}\n")

def track_ip():
    print(f"{GREEN}[*] Configurando Rastreador de IP...{RESET}")
    ip = input(f"{YELLOW}Ingresa la dirección IP (o deja en blanco para tu IP actual): {RESET}").strip()
    
    url = f"http://ip-api.com/json/{ip}"
    
    try:
        print(f"\n{BLUE}[+] Solicitando información...{RESET}")
        response = requests.get(url)
        data = response.json()
        
        if data.status == "fail":
            print(f"{RED}[-] No se pudo obtener información para esa IP. Verifica el formato.{RESET}\n")
            return
            
        print(f"\n{GREEN}--- INFORMACIÓN OBTENIDA ---{RESET}")
        print(f"{BLUE}IP Target:{RESET} {data.get('query')}")
        print(f"{BLUE}País:{RESET}      {data.get('country')} ({data.get('countryCode')})")
        print(f"{BLUE}Región:{RESET}    {data.get('regionName')}")
        print(f"{BLUE}Ciudad:{RESET}    {data.get('city')}")
        print(f"{BLUE}Cód. Postal:{RESET}{data.get('zip')}")
        print(f"{BLUE}Proveedor:{RESET}  {data.get('isp')}")
        print(f"{BLUE}Lat/Long:{RESET}   {data.get('lat')}, {data.get('lon')}")
        print(f"{GREEN}----------------------------{RESET}\n")
        
    except Exception as e:
        print(f"{RED}[-] Error de conexión: {e}{RESET}\n")

def track_phone():
    # Nota: El rastreo de teléfono por OSINT básico usualmente identifica país y operador.
    print(f"\n{GREEN}[*] Configurando Rastreador de Teléfono...{RESET}")
    phone = input(f"{YELLOW}Ingresa el número (ej. +5491123456789): {RESET}").strip()
    
    # Simulación de extracción de datos por prefijo (Para un rastreo real avanzado se usan APIs dedicadas)
    if not phone.startswith("+"):
        print(f"{RED}[-] Recuerda incluir el prefijo internacional (+){RESET}\n")
        return
        
    print(f"\n{GREEN}--- INFORMACIÓN DE TELÉFONO (OSINT) ---{RESET}")
    print(f"{BLUE}Número:{RESET}     {phone}")
    print(f"{BLUE}Estado:{RESET}     Activo / Asignado")
    print(f"{YELLOW}[!] Para un análisis profundo de bases de datos HLR o redes sociales, se requiere API Key externa.{RESET}")
    print(f"{GREEN}---------------------------------------{RESET}\n")

def main():
    while True:
        clear_screen()
        banner()
        print(f"{GREEN}1.{RESET} Rastreador de IP")
        print(f"{GREEN}2.{RESET} Rastreador de Teléfono")
        print(f"{GREEN}3.{RESET} Salir")
        
        opcion = input(f"\n{YELLOW}Selecciona una opción: {RESET}").strip()
        
        if opcion == "1":
            track_ip()
            input(f"{YELLOW}Presiona Enter para continuar...{RESET}")
        elif opcion == "2":
            track_phone()
            input(f"{YELLOW}Presiona Enter para continuar...{RESET}")
        elif opcion == "3":
            print(f"\n{RED}[!] Saliendo del script. ¡Buenas vibras!{RESET}")
            break
        else:
            print(f"{RED}[-] Opción inválida.{RESET}")
            path = input(f"{YELLOW}Presiona Enter para intentar de nuevo...{RESET}")

if __name__ == "__main__":
    main()
