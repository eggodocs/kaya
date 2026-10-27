#   Constant

Provides a constant boolean value.


Type ID: `kaya:constant`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`value` | Boolean | | The boolean value to provide.


???+ tip

    This type can be inlined by specifying a boolean value.


### Example

=== "Full"

    ```json
    {
        "type": "kaya:constant",
        "value": true
    }
    ```

=== "Inlined"

    ```json
    true
    ```

This example provides a boolean value that's always true.


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
