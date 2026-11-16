#   Square Root

Provides the [square root](https://en.wikipedia.org/wiki/Square_root) of a value.


Type ID: `kaya:square_root`[^1]


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`value` | [Float Provider][float_provider] | | The value to get the square root of.


### Example

{% set value = 81 %}
{% set sqrt = sqrt(value) %}

```json
{
    "type": "kaya:square_root",
    "value": 81
}
```

This example provides the square root of {{ value }}, which will be {{ sqrt }}.


### History

<table>
    <tr>
        <td style="text-align: center; vertical-align: middle"><b>Minecraft</b></td>
        <td style="text-align: center; vertical-align: middle"><b>Mod</b></td>
        <td style="vertical-align: middle"><b>Changelog</b></td>
    </tr>
    <tr style="text-align: center; vertical-align: middle">
        <td style="text-align: center; vertical-align: middle">1.21.5</td>
        <td style="text-align: center; vertical-align: middle">0.2.0</td>
        <td style="vertical-align: middle">Added the type.</td>
    </tr>
</table>


[^1]: Aliases: `sqrt`
