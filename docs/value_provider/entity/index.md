#   Entity Provider

Entity providers are data objects that operate on the given context, and return an entity based on the provided information.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`type` | [Identifier]({{ mc.identifier }}) | | The identifier of the desired entity provider type.


???+ tip

    Specifying a [string][string] will implicitly use the [`context`](../meta/conditional.md) entity provider type.


### Meta types

- [`conditional/composite`](../meta/conditional_composite.md)
- [`conditional`](../meta/conditional.md)
- [`context`](../meta/conditional.md)


### Types

- [`selector`](selector.md)
