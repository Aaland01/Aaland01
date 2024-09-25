
def getInnerText(node):
    """ Method for collecting all strings from textnodes in a tree consisting of
    textnodes or nodes with children. 

    Args:
        node (dict): keys: type = textnode or elementnode
        textnode['innertext'] = str
        elementnode['children'] = [{childnodes}]

    Returns:
        _type_: collective string of all textnodes' strings.
    """
    stringBuilder = ""
    if(node['type'] == "textNode"):
        return node['innerText']
    elif(node['type'] == "elementNode"):
        for child in node['children']:            
            stringBuilder += getInnerText(child)
    return stringBuilder    

node = {"type": "elementNode", "children": [{"type": "textNode", "innerText": "string"},
                                            {"type": "textNode", "innerText": "concat"}]}

node2 = {"type": "elementNode", "children": [{"type": "textNode", "innerText": "alotof"},
                                             node]}

print(getInnerText(node)) # Returns "stringconcat"
print(getInnerText(node2)) # Returns "alotofstringconcat"