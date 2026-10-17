#   Boolean Provider

Boolean providers are data objects that operate on the given context, and return a boolean value based on the provided information.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`type` | [Identifier]({{ mc.identifier }}) | | The identifier of the desired boolean provider.


???+ tip

    Specifying certain data types will implicitly use a specific type:

    Data Type | Boolean Provider Type
    ----------|----------------------
    [String][string] | [`context`](../meta/conditional.md)
    Boolean | `constant`


### Meta types

- [`conditional/composite`](../meta/conditional_composite.md)
- [`conditional`](../meta/conditional.md)
- [`constant`](constant.md)
- [`context`](../meta/conditional.md)


### Types

- [`condition_result`](condition_result.md)
- `nbt`
