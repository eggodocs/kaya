#   Entity Fluid Height

Provides the height of the specified fluid relative to an entity.


Type ID: `kaya:entity/fluid_height`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`fluid_tag` | [Fluid Tag]({{ mc.fluid_tag }}) | | The tag of the fluid.
`entity` | [Entity Provider][entity_provider] | | The entity to get the height of the fluid from.


### Example

```json
{
    "type": "kaya:entity/fluid_height",
    "fluid_tag": "#minecraft:water",
    "entity": "this"
}
```

This example will provide the height of the water fluid relative to an entity *(provided by the `kaya:this_entity` context parameter.)*


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
