#   Effect Provider

Effect providers are data objects that operate on the given context, and return an effect instance based on the provided information.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`type` | [Identifier]({{ mc.identifier }}) | | The identifier of the desired effect provider type.


???+ tip

    Specifying certain data types will implicitly use a specific type:

    Data Type | Effect Provider Type
    ----------|---------------------
    [String][string] | `context`
    [Status Effect Instance][status_effect_instance] | `constant`


### Types

- `conditional/composite`
- `conditional`
- `constant`
- `context`
