# Vec3 Provider

Vec3 providers are data objects that operate on the given context, and return a `Vec3`(1) based on the provided information.
{ .annotate }


1. A vector that contains 3 doubles.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`type` | [Identifier]({{ mc.identifier }}) | | The identifier of the desired vec3 provider type. |

???+ question "Implicit types"
    
    When defining a vec3 provider, specifying certain data types will implicitly use a specific type:

    Data Type | Vec3 Provider
    ----------|--------------
    [String][string] | `context`
    [Array][array] of 3 [floats][float] | `constant`


### Meta types

- `conditional/composite`
- `conditional`
- `constant`
- `context`
- `dynamic`
- `offset`


### Types

- `direction`
- `entity/position`
- `entity/velocity`
- `entity/view`
