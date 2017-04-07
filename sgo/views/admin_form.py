# -*- coding: utf-8 -*-

# modules
from ..models import Admin

from wtforms import form, widgets, validators
from wtforms.fields import (
    Field, StringField, PasswordField,
)

from bson import ObjectId, json_util


class ObjectIdField(Field):
    """
    This field is defined to process pymongo object id
    """
    widget = widgets.TextInput()

    def process_formdata(self, valuelist):
        Field.process_formdata(self, valuelist)
        if valuelist and len(valuelist[0]) == 24:
            try:
                self.data = ObjectId(valuelist[0])
            except TypeError:
                self.data = None
        else:
            self.data = None

    def _value(self):
        return str(self.data) if self.data is not None else ''



