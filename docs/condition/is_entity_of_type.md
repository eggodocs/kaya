#   Is Entity of Type

Check if an entity is of a specific type.


Type ID: `neo-apoli:is_entity_of_type`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`entity_type` | [Identifier]({{ mc.identifier }}) | | The ID of the entity type.
`entity` | [Effect Provider][effect_provider] | | The entity to check.


### Example

```json
{
    "type": "neo-apoli:is_entity_of_type",
    "entity_type": "minecraft:creeper",
    "entity": "target"
}
```

This example will check if the type of the entity provided by the `neo-apoli:target_entity` context parameter is `minecraft:creeper`.


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
