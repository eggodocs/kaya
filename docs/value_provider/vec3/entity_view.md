#   Entity View

Provides the view vec3 of the entity.


Type ID: `neo-apoli:entity/view`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`entity` | [Entity Provider][entity_provider] | | The entity to get the view vec3 from.


### Example

```json
{
    "type": "neo-apoli:entity/view",
    "entity": "target"
}
```

This example provides the view vec3 of the entity provided by the `neo-apoli:target_entity` context parameter.


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
