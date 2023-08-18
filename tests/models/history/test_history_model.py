import json
from src.models.history_model import HistoryModel


def test_request_history():
    list_dict = json.loads(HistoryModel.list_as_json())

    for item in list_dict:
        item.pop("_id")

    assert list_dict == [
        {
            "text_to_translate": "Hello, I like videogame",
            "translate_from": "en",
            "translate_to": "pt",
        },
        {
            "text_to_translate": "Do you love music?",
            "translate_from": "en",
            "translate_to": "pt",
        },
    ]