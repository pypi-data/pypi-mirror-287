from mm_mongo import MongoModel, ObjectIdStr, json_dumps
from pydantic import Field


def test_json_dumps():
    class Data(MongoModel):
        id: ObjectIdStr | None = Field(None)
        name: str
        value: int

    data = Data(name="n1", value=1)
    assert json_dumps(data) == """{"id": null, "name": "n1", "value": 1}"""
