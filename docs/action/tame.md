#   Tame

Tames an entity with another entity as its owner.


Type ID: `kaya:tame`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`tameable` | [Entity Provider][entity_provider] | | The entity that will be tamed.
`owner` | [Entity Provider][entity_provider] | | The will-be owner of the entity that will be tamed.


### Example

```json
{
    "type": "kaya:tame",
    "tameable": "target",
    "owner": "actor"
}
```

This example will tame the entity provided by the `kaya:target_entity` context parameter, where the entity provided by the `kaya:actor_entity` context parameter will be its owner.


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
