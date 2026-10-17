#   Block Provider

Block providers are data objects that operate on the given context, and return a `CachedBlock`(1) based on the provided information.
{ .annotate }


1. `CachedBlock` is a record that contains the provided block's position, state, and entity.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`type` | [Identifier]({{ mc.identifier }}) | | The identifier of the desired block provider.


???+ tip

    Specifying a [string][string] will implicitly use the [`context`](../meta/conditional.md) block provider type.


### Meta types

- [`conditional/composite`](../meta/conditional_composite.md)
- [`conditional`](../meta/conditional.md)
- [`context`](../meta/conditional.md)


### Types

- `world`
