# -*- coding: UTF-8 -*-

import orjson
from marshmallow import Schema, fields


class BaseSchema(Schema):
    class Meta:
        render_module = orjson


class EmptyResponseSchema(BaseSchema):
    code = fields.Integer(missing=0, allow_none=False, dump_default=0)
    msg = fields.String(missing='', dump_default='')
    data = fields.Raw(missing=None, allow_none=True)
