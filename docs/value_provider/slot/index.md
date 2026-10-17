# Slot Provider

Slot providers are data objects that operate on the given context, and return a `SlotAccess`(1) based on the provided information.
{ .annotate }


1. `SlotAccess` is a functional interface that essentially references an item from an entity or an inventory.


### Format

Field | Type | Default | Description                                       
------|------|:-------:|------------
`type` | [Identifier]({{ mc.identifier }}) | | The identifier of the desired slot provider type.

???+ tip
    
    Specifying a [string][string] will implicitly use the [`context`](../meta/conditional.md) slot provider type.


### Meta types

- [`conditional/composite`](../meta/conditional_composite.md)
- [`conditional`](../meta/conditional.md)
- [`context`](../meta/conditional.md)


### Types

- `block`
- `entity`
  
