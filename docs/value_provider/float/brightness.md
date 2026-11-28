#   Brightness

Provides the brightness level at a specific position.


Type ID: `kaya:brightness`


???+ info

    The brightness value is calculated using the following formula:
    
    $$
    Brightness = AmbientLight + (1 - AmbientLight) \times LightLevel \div (60 - 3 \times LightLevel)
    $$

    Where:

    - $AmbientLight$ is the ambient light specified in the dimension's definition.
    - $LightLevel$ is the highest light level between the block and sky light level at the specified position.


??? tip "Brightness values for the vanilla dimensions"

    Here's a table of light levels with their corresponding brightness values in each vanilla dimension:

    {% for dimension, ambient_light in dimension_ambient_lights.items() %}
    === "`{{ dimension }}`"

        Light level | Brightness
        ------------|-----------
        {% for light_level, brightness in brightness_dict(ambient_light).items() %}${{ light_level }}$ | ${{ brightness }}$
        {% endfor %}

    {% endfor %}


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`position` | [Vec3 Provider][vec3_provider] | | The position to get the brightness from.


### Example

```json
{
    "type": "kaya:brightness",
    "position": {
        "type": "kaya:entity/position",
        "entity": "this",
        "anchor": "eyes"
    }
}
```
