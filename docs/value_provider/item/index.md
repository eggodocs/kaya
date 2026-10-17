#   Item Provider

Item providers are data objects that operate on the given context, and return an item stack based on the provided information.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`type`| [Identifier]({{ mc.identifier }}) | | The identifier of the desired item provider type.


???+ tip

    Specifying a [string][string] will implicitly use the [`context`](../meta/conditional.md) item provider type.


### Types

- [`conditional/composite`](../meta/conditional_composite.md)
- [`conditional`](../meta/conditional.md)
- [`context`](../meta/conditional.md)
