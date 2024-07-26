from flask_restx import Namespace, fields


class NullableString(fields.String):
    __schema_type__ = ["string", "null"]
    __schema_example__ = "nullable string"


class NullableInteger(fields.Integer):
    __schema_type__ = ["integer", "null"]
    __schema_example__ = "nullable integer"


class NullableFloat(fields.Float):
    __schema_type__ = ["number", "null"]
    __schema_example__ = "nullable float"


class DynamicFields(fields.Raw):
    def format(self, value):
        if not isinstance(value, dict):
            raise ValueError("Value must be a dictionary")

        # List of date fields to format
        date_fields = ['created_on', 'modified_on']

        # Format each date field if it exists in the value
        for field in date_fields:
            if field in value:
                value[field] = value[field].isoformat()

        return value
