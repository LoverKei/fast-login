from bson import ObjectId
from app.models.py_objectid import convert_id

def test_convert_id_correctly():
    #Input
    input = {
        "_id": ObjectId("615ea10e353e1774f9025d7e"),
        "name": "kyo kim",
        "phone": "01011112222"
    }

    #RUN
    converted = convert_id(input)
    
    #Result
    assert converted["id"] == '615ea10e353e1774f9025d7e'
    try:
        converted["_id"]
        assert False
    except Exception:
        assert True

def test_convert_id_with_None():
    #INPUT
    input = None

    #RUN
    converted = convert_id(input)
    
    #RESULT
    assert converted is None
