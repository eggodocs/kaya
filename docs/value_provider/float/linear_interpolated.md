---
example:
    divisor: 30.0
    delta: 20.0
    start: 10.0
    end: 0.0 
---

#   Linear Interpolated

Interpolates a float value.


Type ID: `neo-apoli:linear_interpolated`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`delta` | [Float Provider][float_provider] | | A float value that indicates the percentage of the interpolation.
`start` | [Float Provider][float_provider] | | The start value for the interpolation.
`end` | [Float Provider][float_provider] | | The end value of the interpolation.


???+ info

    If `delta` is $0$, it will provide the `start` value. If it's $1$, it will provide the `end` value. Otherwise, it'll be clamped to be within the range of $0.0$ to $1.0$.


### Example

```json
{
    "type": "neo-apoli:linear_interpolated",
    "delta": {
        "type": "neo-apoli:quotient",
        "dividend": {
            "type": "neo-apoli:entity/attribute",
            "attribute": "minecraft:armor",
            "entity": "this"
        },
        "divisor": 30.0
    },
    "start": 10.0,
    "end": 0.0
}
```

This example will provide a float value ranging from ${{ example.start }}$ to ${{ example.end }}$ depending on the quotient of the value of the `minecraft:armor` attribute *(from the entity provided by the `neo-apoli:this` context parameter)* divided by ${{ example.divisor }}$.

{% set result = clamped_lerp(example.delta / example.divisor, example.start, example.end) %}

For example, if the attribute has a value of ${{ example.delta }}$, the provided value will be ${{ result }}$ $({{ example.start }} + {{ example.delta }} * ({{ example.end }} - {{ example.start }}) = {{ result }})$


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
