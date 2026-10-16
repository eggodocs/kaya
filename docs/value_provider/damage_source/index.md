#   Damage Source Provider

Damage source providers are data objects that operate on the given context, and return a `DamageSource`(1) based on the provided information.
{ .annotate }

1. `DamageSource` is an object that contains the damage type, causing/direct entity, and a position.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`type` | [Identifier]({{ mc.identifier }}) | The identifier of the desired damage source provider.


???+ question "Implicit type"

    When defining a damage source provider, if a [string][string] is specified, it will implicitly use the `context` damage source provider type.


### List of types

- `conditional/composite`
- `conditional`
- `context`
