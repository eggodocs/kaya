#   Sprite

An object that refers to a sprite from a texture atlas.


!!! note

    The following atlases needs a prefix to the path of the sprite ID in order for the sprite to be referenced correctly:

    Atlas | Prefix
    ------|-------
    `minecraft:textures/atlas/blocks.png` | `block` for block textures, `item` for item textures.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`atlas` | [Identifier]({{ mc.identifier }}) | | The ID of the texture atlas.
`id` | [Identifier]({{ mc.identifier }}) | | The ID of the sprite.


### Example

```json
{
    "atlas": "minecraft:textures/atlas/blocks.png",
    "sprite": "minecraft:block/dirt"
}
```

This example refers to the Dirt block texture from the `minecraft:textures/atlas/blocks.png` texture atlas.
