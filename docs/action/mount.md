#   Mount

Mounts an entity to another entity.


Type ID: `neo-apoli:mount`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`vehicle` | [Entity Provider][entity_provider] | | The entity that will be ridden.
`passenger` | [Entity Provider][entity_provider] | | The entity that will be the passenger.
`force` | [Boolean Provider][boolean_provider] | `false` | Determines if the process of mounting should be forced.


### Example

```json
{
    "type": "neo-apoli:mount",
    "vehicle": "actor",
    "passenger": "target"
}
```

This example will make the entity provided by the `neo-apoli:target_entity` context parameter ride the entity provided by the `neo-apoli:actor_entity`.


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
