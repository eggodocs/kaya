#   Compare

Compares two objects, where the result will depend on the specified comparison.


Type ID: `kaya:compare`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`comparison` | [Comparison][comparison] | | The comparison to use for comparing two objects.


### Example

```json
{
    "type": "kaya:compare",
    "comparison": {
        "type": "kaya:int",
        "comparator": ">=",
        "first": {
            "type": "kaya:player/food",
            "entity": "this"
        },
        "second": 5
    }
}
```

This example will check if the food level of the player provided by the `kaya:this_entity` context parameter is greater than or equal to 5.


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
