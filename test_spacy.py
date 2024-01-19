import spacy
from logger_nlp.logger import NLPLogger
from utils import string_utils

log = NLPLogger()

nlp = spacy.load('es_core_news_sm')

text = '''EBusiness  Solutions,  Proyecto:  Puridiom, En la empresa    eBusiness   Solutions 
realice  el  mantenimiento  del  Proyecto: Puridiom,  el  trabajo  que  realizaba  era  crear 
Reportes con Jasper,  manipulación  de  la base  de  datos  en  Oracle  y  SQl  Server  2008 
R2,  Programación en Web (Jquery,  javaScript,  JSP),  hice uso  de  la  IDE  de  Eclipse 
(Juno),   desarrollo con  Java.,  URL de  la  empresa: ebs-pe.com. 
Modelo MVC'''

def _preprocess(text: str) -> str:
    text = text.strip()
    text = string_utils.clean_text(text)
    log.debug(f'Processing query: {text}')

doc = nlp(text)

# entities: PER ,LOC ,ORG ,MISC
print([(ent.text, ent.label_) for ent in doc.ents if ent.label_ == "MISC"])

log.debug("miau miau", "shi")