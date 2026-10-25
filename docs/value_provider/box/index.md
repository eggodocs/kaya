#   Box Provider

Box providers are data objects that operate on the given context, and return an `AABB` (axis-aligned bounding box) based on the provided information.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`type` | [Identifier]({{ mc.identifier }}) | | The identifier of the desired box provider.


???+ tip

    Specifying certain data types will implicitly use a specific type:

    Data Type | Box Provider Type
    ----------|------------------
    [String][string] | [`context`](../meta/conditional.md)
    [Array][array] of 6 [Floats][float] | [`constant`](constant.md)


### Meta types

- [`conditional/composite`](../meta/conditional_composite.md)
- [`conditional`](../meta/conditional.md)
- [`constant`](constant.md)
- [`context`](../meta/conditional.md)
- [`dynamic`](dynamic.md)
- [`inflate`](inflate.md)
- [`resize`](resize.md)
- [`translate`](translate.md)
- [`weighted`](../meta/weighted.md)


### Types

- [`block/bounds`](block_bounds.md)
- [`entity/bounds`](entity_bounds.md)
