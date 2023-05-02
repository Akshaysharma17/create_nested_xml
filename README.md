# XML Creator

This is a Python script that creates an XML document from a dictionary.

## Usage

To use this script, follow these steps:

### 1. Import the necessary modules:

   - import xml.etree.ElementTree as ET
   - import xml.dom.minidom

### 2. Define the `create_xml_element` function:

```
def create_xml_element(name, value):
   element = ET.Element(name)
   if value:
      element.text = value
      return element
```

_This function creates an XML element with the given name and value._


### 3. Define the `create_nested_xml` function:

```
def create_nested_xml(data: dict, root=None):
  if root is None:
  root = ET.Element("Assets")
  for key, value in data.items():
    if isinstance(value, dict):
      sub_element = ET.Element(key.split("")[0])
      create_nested_xml(value, sub_element)
      root.append(sub_element)
    else:
      element = create_xml_element(key.split("")[0], str(value))
      root.append(element)
      return root
```

_This function creates a nested XML document from a dictionary. It calls the `create_xml_element` function to create the XML elements._

#### 4. Call the `create_nested_xml` function with your dictionary to create the XML document:
```
data = {
"asset_name": "My Asset",
"description": "This is a test asset",
"data": {
"data_type": "text",
"data_value": "Hello, world!"
}
}

xml_tree = ET.ElementTree(create_nested_xml(data))
xml_string = ET.tostring(xml_tree.getroot(), encoding="utf-8", method="xml")
pretty_xml_string = xml.dom.minidom.parseString(xml_string).toprettyxml(encoding="utf-8")
print(pretty_xml_string)
```

_This will create an XML string from the `data` dictionary in pretty format and print it to the console._

## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request
