from lxml import etree
import StringIO

class Schema:

  dpiva = etree.XMLSchema(etree.parse(open("/Users/misaelperezchamorro/Documents/Diverza/elixir-snake/DPIVA.xsd")))
  cuentas = etree.XMLSchema(etree.parse(open("/Users/misaelperezchamorro/Documents/Diverza/elixir-snake/CatalogoCuentas_1_1.xsd"))) 
  balanzas = etree.XMLSchema(etree.parse(open("/Users/misaelperezchamorro/Documents/Diverza/elixir-snake/BalanzaComprobacion_1_1.xsd")))
  def __init__(self,name):
  	self.name = name


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

