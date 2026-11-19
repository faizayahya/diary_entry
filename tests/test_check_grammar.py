from lib.check_grammar import check_grammar_of_sentence

def test_no_capital_letter_fails():
    result = check_grammar_of_sentence("this sentence fails.")
    assert result == False

def test_capital_letter_full_stop_in_sentece():
    result = check_grammar_of_sentence("This sentence passes the test.")
    assert result == True

def test_no_full_stop_fails():
    result = check_grammar_of_sentence("This sentence fails")
    assert result == False