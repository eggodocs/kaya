#   Random Chance

Generates a random number between 0.0 and 1.0, and executes an action if it's less than a specified chance.


Type ID: `neo-apoli:random_chance`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`success_action` | [Action][action] | | The action to execute if the chance is less than the random number. 
`fail_action` | [Action][action] | *optional* | If specified, this action will be executed if the chance is greater or equal to the random number.
`chance` | [Float Provider][float_provider] | | The success rate as a number. The value is clamped within the range of 0.0 to 1.0.


??? tip

    You can convert an integer chance value to float by using the following formula: $(Chance = Value / 100)$ (e.g: $(65 / 100 = 0.65)$)


### Example

```json
{
    "type": "neo-apoli:random_chance",
    "success_action": {
        "type": "neo-apoli:set_entity_on_fire",
        "ticks": 200,
        "entity": "this"
    },
    "chance": 0.50
}
```

This example will set the entity provided by the `neo-apoli:this_entity` context parameter on fire for 10 seconds at a 50% chance.


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
