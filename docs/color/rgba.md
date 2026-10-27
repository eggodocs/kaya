#   RGBA

Provides an RGBA color (which is then converted to ARGB.)


Type ID: `kaya:rgba`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`red` | [Float][float] | | The red component of the color. The value should be within the range of 0.0 to 1.0.
`green` | [Float][float] | | The green component of the color. The value should be within the range of 0.0 to 1.0.
`blue` | [Float][float] | | The blue component of the color. The value should be within the range of 0.0 to 1.0.
`alpha` | [Float][float] | | The alpha (transparency) component of the color. The value should be within the range of 0.0 to 1.0.


???+ tip

    This type can be inlined as a hexadecimal string. (`#RRGGBBAA`) The string must be prefixed with `#`, otherwise, it will return an error.


### Example

=== "Full"

    ```json
    {
        "type": "kaya:rgba",
        "red": 1.0,
        "green": 1.0,
        "blue": 0.0,
        "alpha": 0.5
    }
    ```

=== "Inlined"

    ```json
    "#ffff0080"
    ```

This example provides a translucent yellow RGBA color.


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
