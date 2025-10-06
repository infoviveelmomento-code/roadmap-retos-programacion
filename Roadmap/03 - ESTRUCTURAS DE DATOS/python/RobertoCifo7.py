"""
ESTRUCTURAS
"""

# Listas
my_list: list = ["Cifo", "Sergi", "Karlitos", "Solis"]
print(my_list)
my_liar.append("Isabel") # Insercción
print(my_list)
my_list.remove("Solis") # Eliminación
print(my_list)
print(my_list[1]) # Acceso
my_list[1] = "El Mejor" # Actualización
print(my_lsit)
my_list.sort() #Ordenación
print(my_lsit)
print(type(my_lsit))

# Tuplas
my_tuple: tuple = ("Cifo", "Roberto", "@robertocifo", "33")
print(my_tuple[1]) # Acceso
print(my_tuple[3])
my_tuple = tuple(sorted(my_tuple)) # Ordenación
print(my_tuple)
print(type(my_tuple))

# Sets
my_set = {"Cifo", "Sergi", "Karlitos", "Solis"}
print(my_set)
my_set.add("roberr_92@hotmail.com") # Insercción
print(my_set)
my_set.remove("Cifo") # Eliminación
print(my_set)
my_set = set(sorted(my_Set)) # El set no se puede ordenar
print(my_set)
print(my_set[0])
print(type(my_set))

# Diccionario
my_dict: dict = {
  "name": "Roberto",
  "surname": "Cifo", 
  "alias": "@robertocifo", 
  "age": "33"
}
my_dict["email"] = "roberr_92@hotmail.com" # Insercción
print(my_dict)
del my_dict["surname"]
print(my_dict)
print(my_dict["name"]) # Acceso
print(my_dict)
my_dict["age"] = 34 # Actualización
print(my_dict)
my_dict = dict(sorted(my_dict.items())) # Ordenación
print(my_dict)
print(type(my_dict))

"""
EXTRAS
"""

def my_agenda():

  agenda ={}
  
  while True:
  
  print("")
  print("1. Buscar contacto")
  print("2. Insertar contacto")
  print("3. Actualizar contacto")
  print("4. Eliminar contacto")
  print("5. Salir")

  option = input("\nSelecciona una opción: ")

  match option:
    case "1":
        name = input("Introduce el nombre del contacto a buscar: ")
        if name in agenda:
            print(
                f"El número de teléfono de {name} es {agenda[name]}.")
        else: 
            print (f"El contacto {name} no existe.")
    case "2":
        name = input("Introduce el nombre del contacto: ")
        phone = input("Introduce el teléfono del contacto: ")
        if phone.isdigit() and le(phone) > 0 and len(phone) <= 11:
        agenda[name] = phone
        else:
            print("Debes introducir un número de teléfono con menos de 11 dígitos.")
    case "3":
        name = input("Introduce el nombre del contacto a actualizar: ")
        if name in agenda: 
            phone = input("Introduce el teléfono del contacto: ") 
            if phone.isdigit() and le(phone) > 0 and len(phone) <= 11:
        agenda[name] = phone
        else: 
            print(
                "Debes introducir un número de teléfono un máximo de 11 dígitos.")
    else:
        print (f"El contacto {name} no existe.")
    case "4":
        name = input("Introduce el nombre del contacto a eliminar: ")
        if name in agenda: 
            del agenda[name]
        else: 
            print (f"El contacto {name} no existe.")
    case "5":
        print("Saliendo de la agenda.")
        break
    case_:
        print("Opción no válida. Elige una opción del 1 al 5.")
