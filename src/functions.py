def namestr(obj, namespace):
    """ Function which displays the name of the variable """
    return [name for name in namespace if namespace[name] is obj]

def separator():
    print("------------------------------------------------------------------------------------------------------------")