direccion_clinica = "avenida santa fe 298"

print ("\n" + "----- Datos del cliente -----")

nro_paciente = int(input("Ingrese su numero de paciente: "))
nombre_paciente = input("Ingrese su nombre: ")
nacimiento = input("Ingrese su fecha de nacimiento: ")


if nro_paciente > 0:
    print ("\n" + "----- Datos del Medico -----")
    fecha = input("fecha de hoy: ")
    receta = input("Receta medica: ")
    proximo_turno = input("proximo turno: ")
    print("\n" + "📃📃 ------- RECETA MEDICA ------- 📃📃 " +
         "\n⏰Fecha de emicion: " + fecha +
         "\n🚑Direccion clinica: " + direccion_clinica +
         "\n" +
         "\n🙍Nombre del paciente: " + nombre_paciente + 
         "\n🎉Fecha de nacimiento: " + nacimiento + 
         "\n🥼Receta medica: " + receta + "Proxima visita medica: " + proximo_turno + "\n" )
