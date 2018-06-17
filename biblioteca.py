import sys
import fbx

def Initialization(filepath):
    manager = fbx.FbxManager.Create()
    importer = fbx.FbxImporter.Create(manager, '')
    status = importer.Initialize(filepath)

    if status == False:
        sys.exit()

    scene = fbx.FbxScene.Create(manager, '')
    importer.Import(scene)

    return manager, importer, scene

def Closing(manager, importer):

    manager.Destroy()
    importer.Destroy()

def ReturnRightArmNodes(scene):
    '''
    Função recebe o caminho para o arquivo .fbx
    Retornando uma lista contendo todos os nodos referentes ao braço direito.
    Nodos que estão na lista são da classe fbx.FbxNode
    '''
    handnode_list = []

    rootNode = scene.GetRootNode()
    right_arm_list = ['RightShoulder', 'RightArm', 'RightForeArm', 'RightHand',
                      'RightHandThumb1', 'RightHandThumb2', 'RightHandThumb3',
                      'RightHandThumb3_End', 'RightInHandIndex', 'RightHandIndex1',
                      'RightHandIndex2', 'RightHandIndex3', 'RightHandIndex3_End',
                      'RightInHandMiddle', 'RightHandMiddle1', 'RightHandMiddle2',
                      'RightHandMiddle3', 'RightHandMiddle3_End', 'RightInHandRing',
                      'RightHandRing1', 'RightHandRing2', 'RightHandRing3',
                      'RightHandRing3_End', 'RightInHandPinky', 'RightHandPinky1',
                      'RightHandPinky2', 'RightHandPinky3', 'RightHandPinky3_End']

    def traverse(node):
        if node.GetName() in right_arm_list:
            handnode_list.append(node)

        for i in range(0, node.GetChildCount()):
            child = node.GetChild(i)
            traverse(child)

    traverse(rootNode)

    return handnode_list

def GetDatafromNode(node, time):
    '''
    Função recebe um nodo fbx.FbxNode, o caminho para o arquivo .fbx, um float com o tempo exato a ser inspecionado.
    Função retorna um dicionário contendo:
        Nome de identificação do nodo
        Tupla com dados da rotação do nodo (x, y, z)
        Tupla com dados da translação do nodo (x, y, z)
        Tupla com dados da escala do nodo (x, y, z)
        Posição temporal destes dados
    '''
    print('a')
    timer = fbx.FbxTime()
    timer.SetSecondDouble(time)
    print('b')
    pivot = node.eSourcePivot
    print('c')
    matrix = node.EvaluateGlobalTransform(timer, pivot)

    node_rotacao = matrix.GetR()
    node_translacao = matrix.GetT()
    node_escala = matrix.GetS()

    node_dictionary = {
        'Name' : node.GetName(),
        'Rotation' : (node_rotacao[0], node_rotacao[1], node_rotacao[2]),
        'Translation' : (node_translacao[0], node_translacao[1], node_translacao[2]),
        'Scaling' : (node_escala[0], node_escala[1], node_escala[2]),
        'Time' : time
    }

    return node_dictionary
