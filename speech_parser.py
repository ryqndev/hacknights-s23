import spacy

nlp = spacy.load("en_core_web_sm")

def parse_text(text):
    doc = nlp(text)

    pos_tag = ['PROPN', 'ADJ', 'NOUN'] 

    result = []
    doc = nlp(text.lower()) 
    for token in doc:
        if(token.text in nlp.Defaults.stop_words):
            continue
        if(token.pos_ in pos_tag):
            result.append(token.text)
            
    return result



