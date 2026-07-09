correos_bloqueados = {
    "spam123@mail.com",
    "ofertas_gratis@fake.net",
    "ganaste@premio.org",
    "click_aqui@phishing.com"
}

def revisar_correo(correo):
    if correo in correos_bloqueados:
        print(f"Correo {correo} bloqueado")
    else:
        print(f"Correo {correo} permitido")

revisar_correo("spam123@mail.com")
revisar_correo("ndnveijnufev@gmail.com")