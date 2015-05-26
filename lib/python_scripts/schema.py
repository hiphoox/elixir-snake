from lxml import etree
import StringIO

class Schema:

    path = "/Users/hiphoox/Development/Elixir/Diverza/elixir-snake/"
    dpiva = etree.XMLSchema(etree.parse(open(path + "DPIVA.xsd")))
    cuentas = etree.XMLSchema(etree.parse(open(path + "CatalogoCuentas_1_1.xsd")))
    balanzas = etree.XMLSchema(etree.parse(open(path + "BalanzaComprobacion_1_1.xsd")))

def validate_dpiva(xml_data):
    xml = StringIO.StringIO(xml_data)
    doc = etree.parse(xml)
    if Schema.dpiva.validate(doc) :
        return "Todo bien"
    log = Schema.dpiva.error_log
    error = log.last_error
    print(error.message)
    return error.message

def load_dpiva():
        print "dpiva loaded"

