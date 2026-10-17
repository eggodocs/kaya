#   Rotate

Provides a direction rotated on the specified orientation.


Type ID: `neo-apoli:rotate`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`orientation` | [Orientation](#orientation) | | Determines which orientation the direction is rotated.
`direction` | [Direction Provider][direction_provider] | | The direction to rotate.
`axis` | [Axis][axis] | | Determines the axis of the rotation.


[](){ #orientation }

???+ tip "Orientation"

    A [string][string] that determines a rotation of a direction.


    ### Values

    Value | Description
    ------|------------
    `clockwise` | Rotates the direction clockwise.
    `counter_clockwise` | Rotates the direction counter-clockwise.


    ??? info "Rotation of directions"

        Here's a table that lists all the possible orientations and rotations of every direction in every axis:

        === "Clockwise"

            === "X axis"

                Direction | Rotated Direction
                ----------|------------------
                `down` | `south`
                `up` | `north`
                `north` | `down`
                `south` | `up`
                `west` | `west`
                `east` | `east`

            === "Y axis"

                Direction | Rotated Direction
                ----------|------------------
                `down` | `down`
                `up` | `up`
                `north` | `east`
                `south` | `west`
                `west` | `north`
                `east` | `south`

            === "Z axis"

                Direction | Rotated Direction
                ----------|------------------
                `down` | `west`
                `up` | `east`
                `north` | `north`
                `south` | `south`
                `west` | `up`
                `east` | `down`
        
        === "Counter-clockwise"

            === "X axis"

                Direction | Rotated Direction
                ----------|------------------
                `down` | `north`
                `up` | `south`
                `north` | `up`
                `south` | `down`
                `west` | `west`
                `east` | `east`

            === "Y axis"
    
                Direction | Rotated Direction
                ----------|------------------
                `down` | `down`
                `up` | `up`
                `north` | `west`
                `south` | `east`
                `west` | `south`
                `east` | `north`
    
            === "Z axis"
    
                Direction | Rotated Direction
                ----------|------------------
                `down` | `east`
                `up` | `west`
                `north` | `north`
                `south` | `south`
                `west` | `down`
                `east` | `up`


### Example

```json
{
    "type": "neo-apoli:rotate",
    "orientation": "clockwise",
    "direction": "north",
    "axis": "x"
}
```

This example provides the north direction rotated clockwise on the X axis (which will be down.)


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
