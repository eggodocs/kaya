#   Play Sound

Plays a sound event at a position.


Type ID: `neo-apoli:play_sound`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`sound` | [Sound Event]({{ mc.sound_event }}) | | The sound event to play.
`category` | [Sound Category](https://minecraft.wiki/w/Sound#Categories) | `"master"` | The category of the sound.
`targets` | [Array][array] of [Entity Providers][entity_provider] | *optional* | If specified, only these entities will be able to hear the played sound.
`position` | [Vec3 Provider][vec3_provider] | | The position where the sound will be played.
`volume` | [Float Provider][float_provider] | `1.0` | The volume of the sound. The value will have a minimum bound of 0.0.
`pitch` | [Float Provider][float_provider] | `1.0` | The pitch of the sound. The value will be clamped within the range of 0.0 to 2.0.
`min_volume` | [Float Provider][float_provider] | `0.0` | The minimum volume of the sound. The value will be clamped within the range of 0.0 to 1.0.


### Example

```json
{
	"type": "neo-apoli:play_sound",
	"sound": "minecraft:entity.bat.takeoff",
	"category": "neutral",
	"position": {
		"type": "neo-apoli:entity/position",
		"entity": "this"
	},
	"volume": 0.5,
	"pitch": {
		"type": "neo-apoli:random/uniform",
		"min": 0.0,
		"max": 1.0
	}
}
```

This example will play the `minecraft:entity.bat.takeoff` sound event at the position of the entity provided by the `neo-apoli:this_entity` context parameter with a volume of 0.5 and a random pitch (with the range of 0.0 to 1.0.)


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
