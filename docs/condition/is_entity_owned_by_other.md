#   Is Entity Owned by Other

Checks if an entity is owned by another entity.


Type ID: `neo-apoli:is_entity_owned_by_other`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`first` | [Entity Provider][entity_provider] | | The ownable entity to check if it's owned by an entity.
`second` | [Entity Provider][entity_provider] | | The supposed owner of the ownable entity.


### Example

```json
{
    "type": "neo-apoli:is_entity_owned_by_other",
    "first": "target",
    "second": "actor"
}
```

This example will check if the entity provided by the `neo-apoli:target_entity` context parameter is owned by the entity provided by the `neo-apoli:actor_entity` context parameter.


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
