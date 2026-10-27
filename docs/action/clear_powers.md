#   Clear Powers

Clears the powers of an entity.


Type ID: `kaya:clear_powers`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`entity` | [Entity Provider][entity_provider] | | The entity to clear the powers of.


### Example

```json
{
    "type": "kaya:clear_powers",
    "entity": {
        "type": "kaya:weighted",
        "entries": [
            {
                "value": "actor",
                "weight": 1
            },
            {
                "value": "target",
                "weight": 1
            }
        ]
    }
}
```

This example will clear the powers of one out of two entities picked at random with $50\%$ chance each:

- the entity provided by the `kaya:actor_entity` context parameter.
- the entity provided by the `kaya:target_entity` context parameter.


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
