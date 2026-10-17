#   Shape Type

A [string][string] used to determine how raycasts will handle shapes of blocks.


### Values

Value | Description
------|------------
`collider` | The ray will take the collision shape of the block into account, only stopping if the ray has hit a solid face of a block. *(e.g: blocks that cannot be walked through)*
`outline` | The ray will take the shape of the block into account, only stopping if the ray has hit a face of a block.
`visual` | The ray will only stop at blocks that aren't considered transparent. *(e.g: blocks that aren't see-through)*
