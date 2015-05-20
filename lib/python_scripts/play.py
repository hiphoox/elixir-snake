from lxml import etree
import StringIO

def func(name):
    xsd = open("/Users/hiphoox/Development/Elixir/Diverza/elixir-snake/BalanzaComprobacion_1_1.xsd")
    xmlschema_doc = etree.parse(xsd)
    xmlschema = etree.XMLSchema(xmlschema_doc)
    xml = open("/Users/hiphoox/Development/Elixir/Diverza/elixir-snake/Balanza_NoCert_Fail.xml")
    doc = etree.parse(xml)
    if xmlschema.validate(doc) :
        return "Todo bien"
    log = xmlschema.error_log
    error = log.last_error
    print(error.message)
    return error.message

def validate(xml_data):
    xsd = open("/Users/hiphoox/Development/Elixir/Diverza/elixir-snake/BalanzaComprobacion_1_1.xsd")
    xmlschema_doc = etree.parse(xsd)
    xmlschema = etree.XMLSchema(xmlschema_doc)
    
    xml = StringIO.StringIO(xml_data)
    doc = etree.parse(xml)
    if xmlschema.validate(doc) :
        return "Todo bien"
    log = xmlschema.error_log
    error = log.last_error
    print(error.message)
    return error.message
