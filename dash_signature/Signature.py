# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Signature(Component):
    """A Signature component.


Keyword arguments:

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- defaultValue (string; default ''):
    The default value of the input. Usually a value from the database
    or an empty string.

- value (string; default ''):
    The value displayed in the input."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_signature'
    _type = 'Signature'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, value=Component.UNDEFINED, defaultValue=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'defaultValue', 'value']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'defaultValue', 'value']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(Signature, self).__init__(**args)
