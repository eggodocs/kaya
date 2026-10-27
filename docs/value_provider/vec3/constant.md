#   Constant

Provides a constant vec3 value.


Type ID: `kaya:constant`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`value` | [Vec3][vec3] | | The vec3 value to provide.


???+ tip

    This type can be inlined by specifying a [vec3][vec3] value.


### Example

=== "Full"

    ```json
    {
        "type": "kaya:constant",
        "value": [
            1.2,
            2.3,
            4.5
        ]
    }
    ```

=== "Inlined"

    ```json
    [
        1.2,
        2.3,
        4.5
    ]
    ```

This example provides a vec3 with X, Y, Z values of 1.2, 2.3, and 4.5 respectively.


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
