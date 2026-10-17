#   Direction Provider

Direction providers are data objects that operate on the given context, and return a direction based on the provided information.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`type` | [Identifier]({{ mc.identifier }}) | | The identifier of the desired direction provider type.


???+ tip

    Specifying a [string][string] will implicitly use the [`constant`](constant.md) direction provider type.


### Types

- [`conditional/composite`](../meta/conditional_composite.md)
- [`conditional`](../meta/conditional.md)
- [`constant`](constant.md)
- [`opposite`](opposite.md)
- [`rotate`](rotate.md)
