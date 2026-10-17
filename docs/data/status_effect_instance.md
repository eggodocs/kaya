#   Status Effect Instance

An object that defines a status effect with its duration, amplifier, and other properties.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`id` | [Identifier]({{ mc.identifier }}) | | The ID of the status effect.
`amplifier` | [Integer][integer] | `0` | Determines how strong the status effect is. The value must be within the range of 0 to 255. The actual level of the status effect is $(Level = Amplifier + 1)$
`duration` | [Integer][integer] | `0` | Determines how long the status effect would last. If -1 is specified, the status effect will last forever.
`ambient` | Boolean | `false` | Determines whether the particles emitted by the status effect should be semi-transparent.
`show_particles` | Boolean | `true` | Determines if particles should be emitted.
`show_icon` | Boolean | | Determines whether to show or hide the icon of the status effect.


### Example

```json
{
    "id": "minecraft:poison",
    "amplifier": 2,
    "duration": 200,
    "ambient": true
}
```

This example defines a Poison III (00:10) status effect with semi-transparent particle effects.
