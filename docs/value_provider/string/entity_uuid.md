#   Entity UUID

Provides the string form of an entity's UUID.


Type ID: `kaya:entity/uuid`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`entity` | [Entity Provider][entity_provider] | | The entity to get the UUID of.


### Example

```json
{
    "type": "kaya:entity/uuid",
    "entity": {
        "type": "kaya:selector",
        "selector": "@e[sort = random, limit = 1]"
    }
}
```

This example provides the string form of the UUID of a random entity.


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
