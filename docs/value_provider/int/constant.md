#   Constant

Provides a constant integer value.


Type ID: `kaya:constant`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`value` | [Integer][integer] | | The integer value to provide.


???+ tip

    This type can be inlined by specifying a [integer][integer] value.


### Example

=== "Full"

    ```json
    {
        "type": "kaya:constant",
        "value": 366
    }
    ```

=== "Inlined"

    ```json
    366
    ```

This example provides a constant $366$ integer value.


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
