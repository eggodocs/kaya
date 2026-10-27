#   Storage

Provides the NBT of a data storage.


Type ID: `kaya:storage`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
id | [Identifier]({{ mc.identifier }}) | | The ID of the data storage.


### Example

```json
{
    "type": "kaya:storage",
    "id": "example:data"// (1)!
}
```

1. An example data storage with the following contents:

    ```mcfunction
    {value: true, stuff: [1, 2, 3], string: "Hello world!"}
    ```

This example provides the entire contents of the `example:data` data storage.


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
