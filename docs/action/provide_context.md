#   Provide Context

Invokes an action with the provided context parameters.


Type ID: `kaya:provide_context`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`action` | [Action][action] | | The action to invoke.
`parameters` | [Context Parameter Map][context_parameter_map] | | The context parameters to provide.


### Example

```json
{
    "type": "kaya:provide_context",
    "action": {
        "type": "kaya:reference",
        "value": "example:entity/add_local_velocity"// (1)!
    },
    "parameters": {
        "example:entity_to_launch": {
            "type": "kaya:entity",
            "entity": "this"
        },
        "example:velocity": {
            "type": "kaya:vec3",
            "value": [
                0.0,
                4.0,
                0.0
            ]
        }
    }
}
```

1. The location of the file is `data/example/kaya/action/entity/add_local_velocity.json` with this as its contents:
   
    ```json
    {
        "type": "kaya:add_velocity",
        "method": "single",
        "space": "local",
        "entity": "example:entity_to_launch",
        "velocity": {
            "type": "kaya:context",
            "parameter": "example:velocity"
        }
    }
    ```

This example will invoke the referenced `example:entity/add_local_velocity` action and provide the context parameters that it uses.


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
