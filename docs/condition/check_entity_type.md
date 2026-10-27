#   Check Entity Type

Check if an entity is of a type or if it's included in an entity type tag.


Type ID: `kaya:check_effect_type`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`key` | [Identifier]({{ mc.identifier }}) | *optional* | If specified, checks if the entity is of this specific type.
`tag` | [Entity Type Tag]({{ mc.entity_type_tag }}) | *optional* | If specified, checks if the entity is included in this entity type tag.
`entity` | [Entity Provider][entity_provider] | | The entity to check.


???+ warning

    Both `key` and `tag` fields should **not** be present or absent at the same time! Otherwise an error will be thrown.


### Example

```json
{
    "type": "kaya:check_entity_type",
    "tag": "#minecraft:skeletons",
    "entity": "this"
}
```

This example will check if the entity provided by the `kaya:applied_effect` context parameter is included in the `#minecraft:skeletons` entity type tag.


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
