from bson import ObjectId
from pydantic import BaseModel, GetCoreSchemaHandler
from pydantic_core import core_schema


class PyObjectId(ObjectId):
    """
    A custom type that lets Pydantic understand MongoDB's ObjectId.

    Why needed:
      MongoDB uses ObjectId as its primary key (_id), but Pydantic doesn't
      know how to serialize/validate it out of the box. This bridge class
      makes it work seamlessly in both directions.
    """

    @classmethod
    def __get_validators__(cls):
        # Pydantic v1 compatibility
        yield cls.validate

    @classmethod
    def validate(cls, v, handler=None):
        if not ObjectId.is_valid(v):
            raise ValueError(f"Invalid ObjectId: {v}")
        return ObjectId(v)

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type, handler: GetCoreSchemaHandler
    ) -> core_schema.CoreSchema:
        # Pydantic v2 support
        return core_schema.no_info_plain_validator_function(
            cls.validate,
            serialization=core_schema.to_string_ser_schema(),
        )
