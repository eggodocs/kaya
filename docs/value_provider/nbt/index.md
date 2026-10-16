#   NBT Provider

NBT providers are data objects that operate on the given context, and return an NBT based on the provided information.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`type`| [Identifier]({{ mc.identifier }}) |  | The identifier of the desired NBT provider type.


???+ question "Implicit type"

    When defining an NBT provider, if you specify a [string][string] or NBT, it will implicitly use the `constant` NBT provider type.


### Meta types

- `conditional/composite`
- `conditional`
- `constant`


### Types

- `block`
- `entity`
- `item`
- `power`
- `storage`
