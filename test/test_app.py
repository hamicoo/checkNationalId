from app import checker
import requests



def test_checker_valid():
    url = 'http://127.0.0.1:5000/checkid/1111111111'    
    resp = requests.get(url)           
    assert resp.status_code == 200
    assert resp.json()["message"] == "Valid"

def test_checker_notValid():
    url = 'http://127.0.0.1:5000/checkid/1111111114'    
    resp = requests.get(url)           
    assert resp.status_code == 200
    assert resp.json()["message"] == "Not Valid !"       

def test_checker_charAsInput():
    url = 'http://127.0.0.1:5000/checkid/hej'    
    resp = requests.get(url)           
    assert resp.status_code == 200
    assert resp.json()["message"] == "The Number Of ID Number Is Invalid"    

def test_checker_charWithNumber():
    url = 'http://127.0.0.1:5000/checkid/123lkij23458j'    
    resp = requests.get(url)           
    assert resp.status_code == 200
    assert resp.json()["message"] == "The Number Of ID Number Is Invalid"    

def test_checker_wrongNumber():
    url = 'http://127.0.0.1:5000/checkid/123'    
    resp = requests.get(url)           
    assert resp.status_code == 200
    assert resp.json()["message"] == "The Number Of ID Number Is Invalid"    


def test_checker_withChars():
    url = 'http://127.0.0.1:5000/checkid/Assdb'    
    resp = requests.get(url)           
    assert resp.status_code == 200
    assert resp.json()["message"] == "The Number Of ID Number Is Invalid"    
