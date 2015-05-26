from lxml import etree
import StringIO

def func(name):
    xsd = open("./BalanzaComprobacion_1_1.xsd")
    xmlschema_doc = etree.parse(xsd)
    xmlschema = etree.XMLSchema(xmlschema_doc)
    xml = open("./Balanza_NoCert_Fail.xml")
    doc = etree.parse(xml)
    if xmlschema.validate(doc) :
        return "Todo bien"
    log = xmlschema.error_log
    error = log.last_error
    print(error.message)
    return error.message

def validate(xml_data):
    #xsd = open("./BalanzaComprobacion_1_1.xsd")
    xsd = open("./DPIVA.xsd")
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

def load_schema():
    xsd = open("./DPIVA.xsd")
    xmlschema_doc = etree.parse(xsd)
    xmlschema = etree.XMLSchema(xmlschema_doc)
    print(xmlschema)
    return xmlschema

def validate(xml_data,xmlschema):
    xml = StringIO.StringIO(xml_data)
    doc = etree.parse(xml)
    if xmlschema.validate(doc) :
        return "Todo bien"
    log = xmlschema.error_log
    error = log.last_error
    print(error.message)
    return error.message




