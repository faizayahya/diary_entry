"""
#Parameters: text: takes a string/valid sentence
Capital letter, and given puncutation marks '.?!'
Returns true or false

Side effects: None

Example tests: 
Capital letter, full stop => true 
Non-capital letter, full stop => false
Capital letter, excamation mark => true 


"""

def check_grammar_of_sentence(sentence):
    punctuation_marks = (".", "!", "?")

    
    if sentence[0].isupper() and sentence[-1] in punctuation_marks:
        return True
    else:
        return False