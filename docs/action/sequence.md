#   Sequence

Execute multiple actions from top to bottom.


Type ID: `neo-apoli:sequence`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`actions` | [Array][array] of [Actions][action] | | The actions to execute sequentially.


!!! tip

    This action type can be inlined by specifying an array of objects.


### Example

=== "Full"

    ```json
    {
        "type": "neo-apoli:sequence",
        "actions": [
            {
                "type": "neo-apoli:set_entity_on_fire",
                "ticks": 80,
                "entity": "this"
            },
            {
                "type": "neo-apoli:add_velocity",
                "method": "single",
                "space": "world",
                "entity": "this",
                "velocity": [
                    0.0,
                    4.0,
                    0.0
                ]
            }
        ]
    }
    ```

=== "Inlined"

    ```json
    [
        {
            "type": "neo-apoli:set_entity_on_fire",
            "ticks": 80,
            "entity": "this"
        },
        {
            "type": "neo-apoli:add_velocity",
            "method": "single",
            "space": "world",
            "entity": "this",
            "velocity": [
                0.0,
                4.0,
                0.0
            ]
        }
    ]
    ```

This example will set the entity from the `neo-apoli:this_entity` context parameter on fire for 4 seconds and launch them up into the sky.


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
