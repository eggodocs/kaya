#   Area

An object that defines a bounding box (that can have custom shapes) used for getting the entities/blocks within it. This is mainly used for executing actions or counting how many entities/blocks are within it.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`type` | [Identifier]({{ mc.identifier }}) | | The ID of the desired area type.
`target` | [Target][area_target] | | Determines what kind of target is affected by the area.
`shape` | [Shape][shape] | | The shape of the defined area.


[](){ #area_target }

???+ info "Target"

    A [string][string] that determines what kind of target is affected by an area.


    ### Values

    Value | Description
    ------|------------
    `entity` | The area will affect entities within it.
    `block` | The area will affect blocks within it.


### Types

- [`box`](box.md)
- [`radius`](radius.md)
