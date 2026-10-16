#   Reference

Invokes an action file.


Type ID: `neo-apoli:reference`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`value` | [Identifier]({{ mc.identifier }}) | | The ID of the action to invoke.
`parameters` | [Context Parameter Map][context_parameter_map] | *optional* | If specified, these context parameters will be provided to the context for invoking the action.


### Example

=== "Simple"

    ```json
    {
        "type": "neo-apoli:reference",
        "value": "example:entity/set_on_fire_for_5_secs"//(1)!
    }
    ```

    1. The location of the file is `data/example/neo-apoli/action/entity/set_on_fire_for_5_secs.json` with this as its contents:

        ```json
        {
            "type": "neo-apoli:set_entity_on_fire",
            "ticks": 200,
            "entity": "this"
        }
        ```

    This example invokes the `example:entity/set_on_fire_for_5_secs` action.


=== "Complex"

    ```json
    {
        "type": "neo-apoli:reference",
        "value": "example:entity/add_local_velocity"/*(1)!*/,
        "parameters": {
            "example:entity_to_launch": {
                "type": "neo-apoli:entity",
                "entity": "this"
            },
            "example:velocity": {
                "type": "neo-apoli:vec3",
                "value": [
                    0.0,
                    4.0,
                    0.0
                ]
            }
        }
    }
    ```

    1. The location of the file is `data/example/neo-apoli/action/entity/add_local_velocity.json` with this as its contents:
   
        ```json
        {
            "type": "neo-apoli:add_velocity",
            "method": "single",
            "space": "local",
            "entity": "example:entity_to_launch",
            "velocity": {
                "type": "neo-apoli:context",
                "parameter": "example:velocity"
            }
        }
        ```

    This example provides the context parameters (specifically used by the action) before invoking the `example:entity/add_local_velocity` action.


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
        <td style="vertical-align: middle">Added the power type.</td>
    </tr>
</table>
