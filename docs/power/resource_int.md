#   Resource Int

Provides an integer variable with customizable minimum, maximum, and start values.


Type ID: `kaya:resource/int`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`min` | [Int Provider][int_provider] | | The minimum value of the resource.
`max` | [Int Provider][int_provider] | | The maximum value of the resource.
`start_value` | [Int Provider][int_provider] | *optional* | If specified, this value will be used as the initial value of the resource. Otherwise, the minimum value will be the initial value of the resource.
`on_changed_action` | [Action][action] | *optional* | If specified, this action will be executed when the value of the resource has changed.
`min_action` | [Action][action] | *optional* | If specified, this action will be executed when the value of the resource is equal to its minimum value.
`max_action` | [Action][action] | *optional* | If specified, this action will be executed when the value of the resource is equal to its maximum value.


### Example

```json
{
    "type": "kaya:resource/int",
    "min": -20,
    "max": 80
}
```

This example provides an integer-based resource with a minimum value of -20 and a maximum value of 80.


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
