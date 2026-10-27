#   Reference

Invokes an action file.


Type ID: `kaya:reference`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`value` | [Identifier]({{ mc.identifier }}) | | The ID of the action to invoke.


### Example

```json
{
    "type": "kaya:reference",
    "value": "example:entity/set_on_fire_for_5_secs"//(1)!
}
```

1. The location of the file is `data/example/kaya/action/entity/set_on_fire_for_5_secs.json` with this as its contents:

    ```json
    {
        "type": "kaya:set_entity_on_fire",
        "ticks": 200,
        "entity": "this"
    }
    ```

This example invokes the `example:entity/set_on_fire_for_5_secs` action.


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
