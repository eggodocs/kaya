# Vec3 Provider

Vec3 providers are data objects that operate on the given context, and return a 3D vector based on the provided information.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`type` | [Identifier]({{ mc.identifier }}) | | The identifier of the desired vec3 provider type. |

???+ tip
    
    Specifying certain data types will implicitly use a specific type:

    Data Type | Vec3 Provider
    ----------|--------------
    [String][string] | [`context`](../meta/context.md)
    [Array][array] of 3 [Floats][float] | [`constant`](constant.md)


### Meta types

- [`conditional/composite`](../meta/conditional_composite.md)
- [`conditional`](../meta/conditional.md)
- [`constant`](constant.md)
- [`context`](../meta/context.md)
- [`dynamic`](dynamic.md)
- [`normalize`](normalize.md)
- [`offset`](offset.md)
- [`weighted`](../meta/weighted.md)


### Types

- [`block/position`](block_position.md)
- [`direction`](direction.md)
- [`entity/position`](entity_position.md)
- [`entity/velocity`](entity_velocity.md)
- [`entity/view`](entity_view.md)
