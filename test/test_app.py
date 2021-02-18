from app  import idchecker
from app import checkUnit

def test_checker_valid():
    response = idchecker("1111111111")    
    assert response[0] == True

def test_checker_notValid():
    response = idchecker("1111111114")    
    assert response[0] == False

def test_checker_charAsInput():
    response = idchecker("hej")    
    assert response[0] == False

def test_checker_charWithNumber():
    response = idchecker("123lkij23458j")    
    assert response[0] == False


def test_checker_wrongnumber():
    response = idchecker("123")    
    assert response[0] == False

def test_checker_withChars():
    response = idchecker("Assdb")    
    assert response[0] == False


def test_checker_overflow():
    response = idchecker("11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111")    
    assert response[0] == False


def test_checker_overflow2():
    response = idchecker("!@!@#$@#$%#%#$@%@$#!@#!#!##!#!@#!@#!@#!##!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!111")    
    assert response[0] == False


def test_check_testUnit():
     response = checkUnit()
     print(response)
     assert response == 'token13'