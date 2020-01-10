import libreria

assert (libreria.validar_entero_positivo(12)==True)
assert (libreria.validar_entero_positivo(-12)==False)
assert (libreria.validar_entero_positivo("mundo")==False)
assert (libreria.validar_entero_positivo("hokaa")==False)
assert (libreria.validar_entero_positivo(-200)==False)
assert (libreria.validar_entero_positivo("mundo")==False)
print("validad entero positivo=> ok")

assert (libreria.validar_nota(12)==True)
assert (libreria.validar_nota(34)==False)
assert (libreria.validar_nota(-11)==False)
assert (libreria.validar_nota(311)==False)
assert (libreria.validar_nota("jhsjs")==False)
assert (libreria.validar_nota("osms")==False)
print("validad entero positivo=> ok")

assert (libreria.validar_dni(87654687)==True)
assert (libreria.validar_dni(12345678)==True)
assert (libreria.validar_dni("HOLAAAA")==False)
assert (libreria.validar_dni("hoaja")==False)
assert (libreria.validar_dni(97327222)==True)
assert (libreria.validar_dni(98252735)==True)
print("validad entero positivo=> ok")

assert (libreria.validar_telefono("goajaa")==False)
assert (libreria.validar_telefono(926254282)==True)
assert (libreria.validar_telefono(936352437)==True)
assert (libreria.validar_telefono("goajaa")==False)
assert (libreria.validar_telefono("hojaja")==False)
assert (libreria.validar_telefono("esta mal")==False)
print("validad entero positivo=> ok")

assert (libreria.validar_ip("10.9.8.D")==False)
assert (libreria.validar_ip("12.45.13.11")==True)
assert (libreria.validar_ip("45.63.21.26")==True)
assert (libreria.validar_ip("10.F.8.F")==False)
assert (libreria.validar_ip("12.244.13.11")==True)
assert (libreria.validar_ip("111.67.21.27")==True)
print("validad entero positivo=> ok")



assert (libreria.validar_rango(12,1,30)==True)
assert (libreria.validar_rango(23,1,12)==False)
assert (libreria.validar_rango("ss",1,30)==False)
assert (libreria.validar_rango(-1,1,20)==False)
assert (libreria.validar_rango(-20,1,30)==False)
assert (libreria.validar_rango(35,1,36)==True)
print("validad entero positivo=> ok")

