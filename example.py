import biblioteca

filepath = 'Your filepath'

manager, importer, scene = biblioteca.Initialization(filepath)

nodos = biblioteca.ReturnRightArmNodes(scene)

print(nodos)

nodo_dict_list = []
for nodo in nodos:
    nodo_dict_list.append(biblioteca.GetDatafromNode(nodo, 0.0))

print(nodo_dict_list[0])
print('\n')
print(nodo_dict_list[1])

biblioteca.Closing(manager, importer)
