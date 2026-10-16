#   Entity

Compares the IDs of the first and second entities.


Type ID: `neo-apoli:entity`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`first` | [Entity Provider][entity_provider] | | The first entity to compare to.
`second` | [Entity Provider][entity_provider] | | The second entity to be compared.


### Example

```json
{
    "type": "neo-apoli:entity",
    "first": "actor",
    "second": "target"
}
```

This example compares the IDs of the entities from the `neo-apoli:actor_entity` and `neo-apoli:target_entity` context parameters.


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
        <td style="vertical-align: middle">Added the power type.</td>
    </tr>
</table>
