#   Parameter Exists

Checks if a specified context parameter exists on the context. Useful for checking if a provided optional context parameter exists. 


Type ID: `neo-apoli:parameter_exists`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`parameter` | [Context Parameter][context_parameter] | | The context parameter to check.


### Example

```json
{
    "type": "neo-apoli:parameter_exists",
    "parameter": {
        "type": "neo-apoli:block",
        "block": "crafting_block"
    }
}
```

This example checks if the `neo-apoli:crafting_block` context parameter exists on the context.


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
