# Vec3 Provider

Vec3 providers are data objects that operate on the given context, and return a `Vec3`(1) based on the provided information.
{ .annotate }


1. A vector that contains 3 doubles.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`type` | [Identifier]({{ mc.identifier }}) | | The identifier of the desired vec3 provider type. |

???+ tip
    
    Specifying certain data types will implicitly use a specific type:

    Data Type | Vec3 Provider
    ----------|--------------
    [String][string] | [`context`](../meta/conditional.md)
    [Array][array] of 3 [Floats][float] | [`constant`](constant.md)


### Meta types

- [`conditional/composite`](../meta/conditional_composite.md)
- [`conditional`](../meta/conditional.md)
- [`constant`](constant.md)
- [`context`](../meta/conditional.md)
- [`dynamic`](dynamic.md)
- [`offset`](offset.md)
- [`weighted`](../meta/weighted.md)


### Types

- [`block/position`](block_position.md)
- [`direction`](direction.md)
- [`entity/position`](entity_position.md)
- [`entity/velocity`](entity_velocity.md)
- [`entity/view`](entity_view.md)
