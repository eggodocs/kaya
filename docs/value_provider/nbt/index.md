#   NBT Provider

NBT providers are data objects that operate on the given context, and return an NBT based on the provided information.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`type`| [Identifier]({{ mc.identifier }}) |  | The identifier of the desired NBT provider type.


???+ tip

    Specifying certain data types will implicitly use a specific type:

    Data Type | NBT Provider Type
    ----------|------------------
    [String][string] | [`context`](../meta/conditional.md)
    [NBT]({{ mc.nbt }}) | `constant`


### Meta types

- [`conditional/composite`](../meta/conditional_composite.md)
- [`conditional`](../meta/conditional.md)
- [`constant`](constant.md)
- [`context`](../meta/conditional.md)
- [`weighted`](../meta/weighted.md)


### Types

- [`block`](block.md)
- [`entity`](entity.md)
- [`item`](item.md)
- [`power`](power.md)
- [`storage`](storage.md)
