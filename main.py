import xml.etree.ElementTree as ET
import xml.dom.minidom


def create_xml_element(name, value):
    element = ET.Element(name)
    if value:
        element.text = value
    return element

def create_nested_xml(data: dict, root=None):
    if root is None:
        root = ET.Element("Assets")
        for key, value in data.items():
            if isinstance(value, dict):
                sub_element = ET.Element(key.split("_")[0])
                create_nested_xml(value, sub_element)
                root.append(sub_element)
            else:
                element = create_xml_element(key.split("_")[0], str(value))
                root.append(element)
    return root