#   Constant

Provides a constant box value.


Type ID: `kaya:constant`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`min` | [Vec3][vec3] | | Determines the minimum bounds of the box.
`max` | [Vec3][vec3] | | Determines the maximum bounds of the box.


???+ tip

    This type can be inlined by specifying an [array][array] of 6 [floats][float].


### Example

=== "Full"

    ```json
    {
        "type": "kaya:constant",
        "min": {
            "x": 0.0,
            "y": 0.0,
            "z": 0.0
        },
        "max": [
            4.0,
            4.0,
            4.0
        ]
    }
    ```

=== "Inlined"

    ```json
    [
        0.0,
        0.0,
        0.0,
        4.0,
        4.0,
        4.0
    ]
    ```

This example provides a box that's 4 blocks tall, 4 blocks wide, and 4 blocks deep (with a volume of 64 blocks.)


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
