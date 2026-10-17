#   NBT Provider

NBT providers are data objects that operate on the given context, and return an NBT based on the provided information.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`type`| [Identifier]({{ mc.identifier }}) |  | The identifier of the desired NBT provider type.


???+ question "Implicit types"

    When defining an NBT provider, specifying certain data types will implicitly use a specific type:

    Data Type | NBT Provider Type
    ----------|------------------
    [String][string] | `context`
    [NBT]({{ mc.nbt }}) | `constant`


### Meta types

- `conditional/composite`
- `conditional`
- `constant`
- `context`


### Types

- `block`
- `entity`
- `item`
- `power`
- `storage`
