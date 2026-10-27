#   Selector

Provides an entity from a target selector.


Type ID: `kaya:selector`


???+ warning

    The specified target selector can only select **a single entity**. Use the `limit` target selector argument and set its value to 1. *(e.g: `limit=1`)*


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`selector` | [Target Selector]({{ mc.target_selector }}) | | The target selector to get an entity from.


### Example

```json
{
    "type": "kaya:selector",
    "selector": "@e[sort = random, limit = 1]"
}
```

This example selects a random entity from the world.


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
