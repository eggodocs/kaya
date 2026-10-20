#   Slot ID

Provides the integer ID of a slot range that refers to a single slot.


Type ID: `neo-apoli:slot_id`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`slot` | [Slot]({{ mc.slot_identifier }}) | | The ID of the slot to get the integer ID of.


### Example

```json
{
    "type": "neo-apoli:slot_id",
    "slot": "player.crafting.0"
}
```

This example will provide the integer ID of the `player.crafting.0` slot *(which will be $500$.)*


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
