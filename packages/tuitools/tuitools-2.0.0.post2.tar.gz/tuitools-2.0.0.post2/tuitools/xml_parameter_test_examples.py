def read_xml_params(xml_file):
    import xml.etree.ElementTree as ET
    from itertools import product
    tree = ET.parse(xml_file)
    root = tree.getroot()
    params = {}
    for param in root.findall('param'):
        name = param.get('name')
        values = [value.text for value in param.findall('value')]
        params[name] = values
    test_cases = list(product(*params.values()))
    for i, case in enumerate(test_cases, start=1):
        print(f"TestCase {i}: {dict(zip(params.keys(), case))}")