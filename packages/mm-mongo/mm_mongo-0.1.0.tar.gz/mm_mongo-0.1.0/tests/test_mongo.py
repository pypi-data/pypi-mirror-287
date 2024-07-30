import time
from typing import ClassVar

import pytest
from bson import ObjectId
from mm_mongo import MongoCollection, MongoModel, ObjectIdStr
from mm_mongo.mongo import drop_collection, mongo_query, parse_indexes, parse_str_index_model
from pydantic import Field
from pymongo import IndexModel
from pymongo.errors import WriteError


def test_object_id_str(mongo_database):
    class Data(MongoModel):
        __collection__ = "data_test_object_id_str"
        id: ObjectIdStr = Field(..., alias="_id")
        name: str

    d = Data(**{"name": "n1", "_id": ObjectId("64a2741ee4524cebbfdbe26d")})  # noqa: PIE804
    assert d.id == ObjectIdStr("64a2741ee4524cebbfdbe26d")


def test_wrap_object_id(mongo_database):
    # with wrapper
    class Data1(MongoModel):
        __collection__ = "data1_test_wrap_object_id"
        id: ObjectIdStr | None = Field(None, alias="_id")
        name: str

    class Data2(MongoModel):
        __collection__ = "data2_test_wrap_object_id"
        id: ObjectIdStr = Field(..., alias="_id")
        name: str

    coll = MongoCollection(Data1, mongo_database)
    assert coll.wrap_object_id

    coll = MongoCollection(Data2, mongo_database)
    assert coll.wrap_object_id

    # without wrapper
    class Data3(MongoModel):
        __collection__ = "data3_test_wrap_object_id"
        id: int | None = Field(None, alias="_id")
        name: str

    coll = MongoCollection(Data3, mongo_database, False)
    assert not coll.wrap_object_id


def test_mongo_model_init_collection(mongo_database):
    class Data(MongoModel):
        __collection__ = "data_test_mongo_model_init_collection"
        id: ObjectIdStr | None = Field(None, alias="_id")
        name: str

    drop_collection(mongo_database, Data.__collection__)
    col: MongoCollection[Data] = Data.init_collection(mongo_database)
    col.insert_one(Data(name="n1"))
    col.insert_one(Data(name="n2"))
    assert col.count({}) == 2


def test_schema_validation(mongo_database):
    class Data(MongoModel):
        __collection__ = "data_test_schema_validation"
        id: int | None = Field(..., alias="_id")
        name: str
        value: int

        __validator__: ClassVar[dict[str, object]] = {
            "$jsonSchema": {"required": ["name", "value"], "properties": {"value": {"minimum": 10}}},
        }

    drop_collection(mongo_database, Data.__collection__)
    time.sleep(2)  # without it `-n auto` doesn't work. It looks like drop_collection invokes a little bit later
    col: MongoCollection[Data] = Data.init_collection(mongo_database)
    col.insert_one(Data(name="n1", value=100, _id=1))
    with pytest.raises(WriteError):
        col.update_one({"name": "n1"}, {"$set": {"value": 3}})


def test_parse_str_index_model():
    assert IndexModel("k").document == parse_str_index_model("k").document
    assert IndexModel("k", unique=True).document == parse_str_index_model("!k").document
    assert IndexModel([("a", 1), ("b", -1)], unique=True).document == parse_str_index_model("!a,-b").document


def test_parse_indexes():
    assert parse_indexes(None) == []
    assert parse_indexes("") == []
    assert [i.document for i in parse_indexes("a")] == [IndexModel("a").document]
    assert [i.document for i in parse_indexes("a, b")] == [IndexModel("a").document, IndexModel("b").document]
    assert [i.document for i in parse_indexes("a,b")] == [IndexModel("a").document, IndexModel("b").document]
    assert [i.document for i in parse_indexes("a,!b")] == [IndexModel("a").document, IndexModel("b", unique=True).document]
    assert [i.document for i in parse_indexes("a, !b")] == [IndexModel("a").document, IndexModel("b", unique=True).document]


def test_mongo_query():
    assert mongo_query(a=1, b=None, c="") == {"a": 1}
    assert mongo_query(a=0) == {"a": 0}
