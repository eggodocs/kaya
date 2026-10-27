#   Entity Has Correct Tool For Block

Checks if an entity has the correct tool for a block.


Type ID: `kaya:entity_has_correct_tool_for_block`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`entity` | [Entity Provider][entity_provider] | | The entity to check if it has the correct tool for the block.
`block` | [Block Provider][block_provider] | | The block to check if the tool is correct for.


### Example

```json
{
    "type": "kaya:entity_has_correct_tool_for_block",
    "entity": "this",
    "block": "mining_block"
}
```

This example will check if the entity provided by the `kaya:this_entity` context parameter has the correct tool for the block provided by the `kaya:mining_block` context parameter.


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
