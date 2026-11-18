#   Square Root Inverse

Provides an inversed [square root](https://en.wikipedia.org/wiki/Square_root) by dividing 1.0 with the square root of a value.


Type ID: `kaya:square_root/inverse`[^1]


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`value` | [Float Provider][float_provider] | | The value to get the square root of.


### Example

{% set value = 9 %}
{% set sqrt = sqrt(value) %}
{% set inv_sqrt = inv_sqrt(value)%}

```json
{
    "type": "kaya:square_root/inverse",
    "value": {{ value }}
}
```

This example will provide the inverse square root of {{ inv_sqrt }}, with {{ sqrt }} being the square root value.


### History

<table>
    <tr>
        <td style="text-align: center; vertical-align: middle"><b>Mod</b></td>
        <td style="vertical-align: middle"><b>Changelog</b></td>
    </tr>
    <tr style="text-align: center; vertical-align: middle">
        <td style="text-align: center; vertical-align: middle">0.2.0</td>
        <td style="vertical-align: middle">Added the type.</td>
    </tr>
</table>


[^1]: Aliases: `inv_sqrt`
