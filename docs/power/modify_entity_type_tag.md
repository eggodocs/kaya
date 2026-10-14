#   Modify Entity Type Tag

Modifies whether the entity holding the power is considered included in an entity type tag without modifying the entity type tag directly.


Type ID: `neo-apoli:modify/entity/type_tag`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`tag` | [Identifier]({{ mc.identifier }}) | | The ID of the entity type tag to include the entity to.


### Example

```json
{
    "type": "neo-apoli:modify/entity/type_tag",
    "tag": "#minecraft:powder_snow_walkable_mobs",
    "active_condition": {
        "type": "neo-apoli:is_entity_sneaking",
        "entity": "this"
    }
}
```

This example makes the entity holding the power be able to walk on powder snow if they're sneaking.


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
        <td style="vertical-align: middle">Added the power type.</td>
    </tr>
</table>
