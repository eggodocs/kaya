#   Block Provider

Block providers are data objects that operate on the given context, and return an object that contains the position, state, and entity of a block based on the provided information.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`type` | [Identifier]({{ mc.identifier }}) | | The identifier of the desired block provider.


???+ tip

    Specifying a [string][string] will implicitly use the [`context`](../meta/context.md) block provider type.


### Meta types

- [`conditional/composite`](../meta/conditional_composite.md)
- [`conditional`](../meta/conditional.md)
- [`context`](../meta/context.md)
- [`weighted`](../meta/weighted.md)


### Types

- [`world`](world.md)
