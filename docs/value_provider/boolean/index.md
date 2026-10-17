#   Boolean Provider

Boolean providers are data objects that operate on the given context, and return a boolean value based on the provided information.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`type` | [Identifier]({{ mc.identifier }}) | | The identifier of the desired boolean provider.


???+ question "Implict types"

    When defining a boolean provider, specifying certain data types will implicitly use a specific type:

    Data Type | Boolean Provider Type
    ----------|----------------------
    [String][string] | `context`
    Boolean | `constant`


### Meta types

- `conditional/composite`
- `conditional`
- `constant`
- `context`


### Types

- `condition_result`
- `nbt`
