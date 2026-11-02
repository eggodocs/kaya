# Slot Provider

Slot providers are data objects that operate on the given context, and return a slot based on the provided information.


### Format

Field | Type | Default | Description                                       
------|------|:-------:|------------
`type` | [Identifier]({{ mc.identifier }}) | | The identifier of the desired slot provider type.

???+ tip
    
    Specifying a [string][string] will implicitly use the [`context`](../meta/context.md) slot provider type.


### Meta types

- [`conditional/composite`](../meta/conditional_composite.md)
- [`conditional`](../meta/conditional.md)
- [`context`](../meta/context.md)
- [`weighted`](../meta/weighted.md)


### Types

- [`block`](block.md)
- [`entity`](entity.md)
  
