import pytest
from string_utils import StringUtils

utils = StringUtils()

#1

def test_capitilize():
   """Positiv"""
    assert utils.capitilize("Marina") == "Marina"
    assert utils.capitilize("777") == "777"
    assert utils.capitilize("14 сентября 2024") == "14 сентября 2024"
    """Negativ"""
    assert utils.capitilize("") == ""
    assert utils.capitilize(" ") == " "
    assert utils.capitilize("123привет") == "123привет" 

#2

def test_trim():
    """Positiv"""
    assert utils.trim("     Marina") == "Marina"
    assert utils.trim("     he llo   ") == "he llo   "
    assert utils.trim(" MAR  ") == "MAR  "
    """Negativ"""
    assert utils.trim("") == ""

@pytest.mark.xfail()
def test_trim_with_numbers_imput():
    assert utils.trim(888) == "888"

@pytest.mark.xfail()
def test_trim_with_spaces_output():
    assert utils.trim("   MAR   ") == "   MAR   "

#3

@pytest.mark.parametrize('string, delimeter, result', [
    #Позитив
   ("однажды, жил, играл", ",", ["однажды", "жил", "играл"]),
    ("1,2,3,4,5", ",", ["1", "2", "3", "4", "5"]),    
    ("!@#@$", "!", ["!", "#", "$"]),
    #Негатив
   ("", None, []),
    ("1,2,3,4,5", None, ["1", "2", "3", "4 5"]),   
])
def test_to_list(string, delimeter, result):
    if delimeter is None:
        res = utils.to_list(string)
    else:
       res = utils.to_list(string,delimeter)
    assert res == result

#4

@pytest.mark.parametrize('string, symbol, result', [
   ("кукла", "к", True),
    ("точка", "т", True),
    ("почва", "п", True),
    ("лось", "л", True),
    ("изгой", "и", True),
    ("ночь", "к", False),
    ("игра", "щ", False),
    ("лодка", "м", False),
    ("", "к", False),
   ("789", "о", False),
])
def test_contains(string, symbol, result):
    res = utils.contains(string, symbol)
    assert res == result


#5

@pytest.mark.parametrize('string, symbol, result', [
      ("уровень", "р", "уовень"),  
      ("красный", "к", "расный"),
      ("896", "6", "89"),
      
      ("дача", "н", "дача"),
      ("", "", ""),
      ("", "г", ""),
])
def test_contains(string, symbol, result):
    res = utils.delete_symbol(string, symbol)
    assert res == result

#6

@pytest.mark.parametrize('string, symbol, result', [
    ("фильм", "ф", True),
    ("нога", "н", True),
    ("игла", "и", True),
   ("Конь", "к", False),
    ("нож", "Н", False),
    ("роща", "щ", False),
])

def test_starts_with(string, symbol, result):
    res = utils.starts_with(string, symbol)
    assert res == result

#7

@pytest.mark.parametrize('string, symbol, result', [
    
    ("Марина", "а", True),
    ("ононь", "ь", True),
    ("", "", True),


    ("точность", "ш", False),
    ("укроп", "й", False),
     ("лошадь", "л", False),   
])

def test_end_with(string, symbol, result):
    res = utils.end_with(string, symbol)
    assert res == result

#8

@pytest.mark.parametrize('string, result', [
    
    ("", True),
    (" ", True),
    ("  ", True), 

    ("не пусто", False),
    ("не пусто с пробелом", False),
    ("777", False),
])
def test_is_empty(string, result):
    res = utils.is_empty(string)
    assert res == result

#9

@pytest.mark.parametrize('lst, joiner, result', [

    (["м", "е", "м"], ",", "м,е,м"),
    ([1, 2, 3], None, "1,2,3"),
    (["Первая", "Вторая"], "-", "Первая-Вторая"),
    (["к", "о", "н"], "", "кон"),
    
    ([], None, ""),
    ([], ",", ""),
    ([], "ром", "")
])
def test_list_to_string(lst, joiner, result):
    if joiner == None:
        res = utils.list_to_string(lst)
    else:
        res = utils.list_to_string(lst, joiner)
        assert res == result


