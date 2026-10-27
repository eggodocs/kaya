#   Modify Player Spawn

Modifies the spawn point of the player holding the power.


Type ID: `kaya:modify/player/spawn`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`dimension` | [Identifier]({{ mc.identifier }}) | | The ID of the dimension to look for a new spawn point.
`biome` | [Identifier]({{ mc.biome_identifier }}) or [Tag]({{ mc.biome_tag }}) | *optional* | The ID or the tag of a biome to look for a new spawn point.
`structure` | [Identifier]({{ mc.structure_identifier }}) or [Tag]({{ mc.structure_tag }}) | *optional* | The ID or the tag of the structure to look for a spawn point.
`priority` | [Integer][integer] | `0` | Determines the order of which powers of this type will be checked.


??? question "About priorities"

    The instances of this type will be sorted in its **reversed** *natural order* meaning that instances that have a higher priority value will be checked first if it has found a spawn point before those that have lower priority values.


### Example

```json
{
    "type": "kaya:modify/player/spawn",
    "dimension": "minecraft:overworld",
    "biome": "#c:is_aquatic"
}
```

This example will make the player holding the power have a spawn point that is on a biome included in the `#c:is_aquatic` biome tag.


### History

<table>
    <tr>
        <td style="text-align: center; vertical-align: middle"><b>Minecraft</b></td>
        <td style="text-align: center; vertical-align: middle"><b>Mod</b></td>
        <td style="vertical-align: middle"><b>Changelog</b></td>
    </tr>
    <tr style="text-align: center; vertical-align: middle">
        <td style="text-align: center; vertical-align: middle">1.21.5</td>
        <td style="text-align: center; vertical-align: middle">0.1.0</td>
        <td style="vertical-align: middle">Added the type.</td>
    </tr>
</table>
