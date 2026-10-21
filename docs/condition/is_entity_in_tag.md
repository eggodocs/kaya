#   Is Entity In Tag

Checks if the type of an entity is in a specified entity type tag.


Type ID: `neo-apoli:is_entity_in_tag`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`tag` | [Entity Type Tag]({{ mc.entity_type_tag }}) | | The entity type tag to match.
`entity` | [Entity Provider][entity_provider] | | The entity to check.


### Example

```json
{
    "type": "neo-apoli:is_entity_in_tag",
    "tag": "#minecraft:skeletons",
    "entity": "this"
}
```

This example will check if the type of the entity provided by the `neo-apoli:this_entity` context parameter is included in the `#minecraft:skeletons` entity type tag.


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
