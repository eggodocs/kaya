#   Entity Yaw

Provides the yaw of an entity.


Type ID: `kaya:entity/yaw`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`entity` | [Entity Provider][entity_provider] | | The entity to get the yaw from.


### Example

```json
{
    "type": "kaya:entity/yaw",
    "entity": "this"
}
```

This example will provide the yaw of the entity provided by the `kaya:this_entity` context parameter.


### History

<table>
    <tr>
        <td style="text-align: center; vertical-align: middle"><b>Minecraft</b></td>
        <td style="text-align: center; vertical-align: middle"><b>Mod</b></td>
        <td style="vertical-align: middle"><b>Changelog</b></td>
    </tr>
    <tr style="text-align: center; vertical-align: middle">
        <td style="text-align: center; vertical-align: middle">1.21.5</td>
        <td style="text-align: center; vertical-align: middle">0.2.0</td>
        <td style="vertical-align: middle">Added the type.</td>
    </tr>
</table>
