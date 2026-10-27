#   Float { #float_comparison }

Compares the first and second floats.


Type ID: `kaya:float`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`comparator` | [Comparator][comparator] | | Determines how the floats are compared.
`first` | [Float Provider][float_provider] | | The first float to compare to.
`second` | [Float Provider][float_provider] | | The second float to be compared.


### Example

```json
{
    "type": "kaya:float",
    "comparator": "==",
    "first": {
        "type": "kaya:power/cooldown/progress",
        "power": "example:cooldown",
        "entity": "this"
    },
    "second": 1.0
}
```

This example compares the cooldown progress of the `example:cooldown` power to 1.0, essentially checking if it's currently not in the progress of cooling down.


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
