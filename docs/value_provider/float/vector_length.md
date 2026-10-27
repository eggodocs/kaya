---
x: 33.0
y: 87.0
z: 242.0
---


#   Vector Length

Provides the length of a vector.


Type ID: `kaya:vector/length`


???+ info

    The formula for calculating the length of a vector is as follows: $(Length = \sqrt{X * X + Y * Y + Z * Z})$


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`vector` | [Vec3 Provider][vec3_provider] | | The vector to get the length of.


### Example

```json
{
    "type": "kaya:vector/length",
    "vector": {
        "type": "kaya:entity/position",
        "entity": "this"
    }
}
```

{% set result = sqrt(x * x + y * y + z * z) %}

This example will provide the length of the position vector of an entity *(provided by the `kaya:this_entity` context parameter.)* For example, let's say the entity's position is X: ${{ x }}$, Y: ${{ y }}$, Z: ${{ z }}$. The length of the position vector will be ${{ result }}$.


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
