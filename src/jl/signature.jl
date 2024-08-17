# AUTO GENERATED FILE - DO NOT EDIT

export signature

"""
    signature(;kwargs...)

A Signature component.

Keyword arguments:
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `save` (Bool; optional): The trigger for the component to update the value.
Setting to true will update the value.
- `value` (String; optional): The value displayed in the input.
"""
function signature(; kwargs...)
        available_props = Symbol[:id, :save, :value]
        wild_props = Symbol[]
        return Component("signature", "Signature", "dash_ijack_components", available_props, wild_props; kwargs...)
end

