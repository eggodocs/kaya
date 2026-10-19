#   Damage Source Provider

Damage source providers are data objects that operate on the given context, and return a `DamageSource`(1) based on the provided information.
{ .annotate }

1. `DamageSource` is an object that contains the damage type, causing/direct entity, and a position.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`type` | [Identifier]({{ mc.identifier }}) | The identifier of the desired damage source provider.


???+ tip

    Specifying a [string][string] will implicitly use the [`context`](../meta/conditional.md) damage source provider type.


### Types

- [`conditional/composite`](../meta/conditional_composite.md)
- [`conditional`](../meta/conditional.md)
- [`context`](../meta/conditional.md)
- [`weighted`](../meta/weighted.md)
