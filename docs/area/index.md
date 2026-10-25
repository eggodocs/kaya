#   Area

An object that defines a bounding box (that can have custom shapes) used for getting the entities/blocks within it. This is mainly used for executing actions or counting how many entities/blocks are within it.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`type` | [Identifier]({{ mc.identifier }}) | | The ID of the desired area type.
`target` | [String][string] | | Determines whether to target entities (`"entity"`) or blocks (`"block"`) within the defined area.
`shape` | [Shape][shape] | | The shape of the defined area.


### Types

- [`box`](box.md)
- [`radius`](radius.md)
