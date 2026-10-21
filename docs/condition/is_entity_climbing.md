#   Is Entity Climbing

Checks if an entity is actively climbing a block.


Type ID: `neo-apoli:is_entity_climbing`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`entity` | [Entity Provider][entity_provider] | | The entity to check.


### Example

```json
{
    "type": "neo-apoli:is_entity_climbing",
    "entity": "this"
}
```

This example will check if the entity provided by the `neo-apoli:this_entity` context parameter is actively climbing a block.


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
