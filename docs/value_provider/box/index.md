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
    [String][string] | `context`
    [Array][array] of 6 [Floats][float] | `constant`


### Meta types

- `conditional/composite`
- `conditional`
- `constant`
- `context`
- `dynamic`
- `offset`
- `translate`


### Types

- `block/bounds`
- `entity/bounds`
