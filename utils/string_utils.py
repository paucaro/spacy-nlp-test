import re
from logger_nlp.logger import NLPLogger

log = NLPLogger()

def clean_text(text):
    regex_spaces = re.compile(r'(?!\n)\s+')
    regex_newlines = re.compile(r'((\r\n)|[\n\v])+')
    try:
        text = text.replace('\t', ' ')
        text = regex_spaces.sub(' ', regex_newlines.sub(' ', text)).strip()
    except TypeError as e:
        print("")
        log.warn(f'Preprocessing text failed. Exception: {e}', conf=clean_text.__name__)
    return text