#   Box Provider

Box providers are data objects that operate on the given context, and return an `AABB` (axis-aligned bounding box) based on the provided information.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`type` | [Identifier]({{ mc.identifier }}) | | The identifier of the desired box provider.


???+ question "Implicit type"

    When defining a box provider, if an [array][array] of 6 [floats][float] is specified, it will implicitly use the `constant` box provider type.


### List of box provider types

- `conditional/composite`
- `conditional`
- `constant`
- `dynamic`
- `offset`
- `translate`
- `block/bounds`
- `entity/bounds`
