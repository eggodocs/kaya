#   Block

Encodes the block as NBT and uses it as the provided value.


Type ID: `kaya:block`


???+ info

    The block is encoded in the following format:

    ```mcfunction
    #   The 'entity' NBT is only present if the block is a block entity
    {pos: [<int>, <int>, <int>], state: {Name: "<block_id>", Properties: { /* block state properties */ }}, entity: {id: "<block_entity_id">, /* data of the block entity */}}
    ```


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`block` | [Block Provider][block_provider] | | The block to encode as NBT.


### Example

```json
{
    "type": "kaya:block",
    "block": "selected_block"
}
```

This example encodes the block provided by the `kaya:selected_block` context parameter and provides it as the NBT value.


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
