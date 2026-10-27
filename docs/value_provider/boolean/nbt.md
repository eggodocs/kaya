#   NBT

Provides the value of the NBT if it's a boolean, or check if the count of the NBT is greater than 1 if it's not a boolean.


Type ID: `kaya:nbt`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`source` | [NBT Provider][nbt_provider] | | The source to get an NBT from.
`path` | [NBT Path]({{ mc.nbt_path }}) | | The path of the desired NBT to get from the source.


### Example

```json
{
    "type": "kaya:nbt",
    "source": {
        "type": "kaya:storage",
        "id": "example:data"// (1)!
    },
    "path": "value"
}
```


1. An example data storage with the following contents:

    ```mcfunction
    {value: true, stuff: [1, 2, 3], string: "Hello world!"}
    ```


This example queries the value of the `value` NBT from the `example:data` data storage.


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
