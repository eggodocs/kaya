#   Entity Bounds

Provides the bounding box of an entity.


Type ID: `kaya:entity/bounds`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`entity` | [Entity Provider][entity_provider] | | The entity to get the bounding box from.


### Example

```json
{
    "type": "kaya:entity/bounds",
    "entity": "this"
}
```

This example provides bounding box of the entity provided by the `kaya:this_entity` context parameter.


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
