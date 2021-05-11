import json
import yaml
import xmltodict

def parse_json(filename):
    """Metodo para parsear arquivos JSON

    Args:
        filename (string): Path do aquivo
    """
    result = {}
    with open(filename, "r") as fp:
        result = json.load(fp)
    
    return result

def parse_xml(filename):
    """Metodo para parsear arquivos JSON

    Args:
        filename (string): Path do aquivo
    """
    result = {}
    with open(filename, "r") as fp:
        result = xmltodict.parse(fp.read())   
    
    return result

def parse_yaml(filename):
    """Metodo para parsear arquivos JSON

    Args:
        filename (string): Path do aquivo
    """
    result = {}
    with open(filename, "r") as fp:
        result = yaml.safe_load(fp)

    print(result.get("access_token"))

    return result   

parse_yaml("files/myfile.yaml")
