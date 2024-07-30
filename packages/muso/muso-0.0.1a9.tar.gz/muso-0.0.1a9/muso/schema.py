# -*- coding: UTF-8 -*-

import datetime

import orjson
import tzlocal
from marshmallow import Schema, fields


class BaseSchema(Schema):
    class Meta:
        render_module = orjson


class EmptyResponseSchema(BaseSchema):
    code = fields.Integer(missing=0, allow_none=False, dump_default=0)
    msg = fields.String(missing='', dump_default='')
    data = fields.Raw(missing=None, allow_none=True)


class LocalDateTimeField(fields.DateTime):

    def _serialize(self, value, attr, obj, **kwargs):
        if value is None:
            return None
        value = value.replace(microsecond=0)
        return super()._serialize(value.astimezone(
            tz=tzlocal.get_localzone()), attr, obj, **kwargs)


class FileField(fields.Field):
    pass
