#   Making a Power

???+ tip

    Before continuing, make sure you've read the ['Getting Started'](getting_started.md) page, as this page will be covering the creation of a power, which will involve JSON and a data pack.


Powers are used to give an entity an "ability". The functionality of the "ability" that will be given to the entity will entirely depend on the type of the power you'll define.

Powers must be created and/or placed in the `data/<namespace>/kaya/power` directory of your data pack for the mod to be able to recognize it as such.

Generally, all powers support the fields found in the [index page for powers](../power/index.md). For the other fields which define more specific functionality of the power, you'll have to look at the page corresponding to the type you want to use.


## Tutorial

Let's say that we want to create a power that would damage entities within a radius of a cubic area, relative to where a block is broken; we'll call it "Pressure". We'll start off by creating a JSON file in the `data/tutorial/kaya/power` directory of a data pack.

It's recommended that you use a name that is either the same, or at least similar/related to the power you're creating, so in this case, we'll be creating a JSON file named `pressure.json` (with `.json` being the file extension.)


???+ info

    The full path for the file will look like `data/tutorial/kaya/power/pressure.json`. The power will then be referred to as `tutorial:pressure`.
    
    You can change the name of the `tutorial` directory if you'd like, but for this tutorial, it'll be kept as is.


Since we want to execute an action when a block is broken by the entity holding the power, the [Callback Block Break (Power Type)](../power/callback_block_break.md) is the one we're looking for. The contents of the JSON file should look something like this:

```json
{
    "type": "kaya:callback/block/break",
    "name": "Pressure",
    "description": "You're strong enough to cause shockwaves when breaking a block, damaging nearby entities."
}
```

I added the `name` and `description` field to demonstrate how you can add yours. You'll be able to see the defined name when granting the power and the description if you have another mod that uses Kaya that can view powers.

As is, the power is incomplete! It's missing the `on_break_action` field, which is required. The field defines the [action][action] that we want to happen when the entity holding the power has broken a block.

In this case, we'll want to use the [Area of Effect (Action Type)](../action/area_of_effect.md) since it can use an area to target entities or blocks. 

Since we want a cubic area that targets entities within a specific radius, we'll use the [Radius (Area Type)](../area/radius.md), specify `"entity"` as the `target` of the area, and specify a `shape` of `"cube"`:

```json
{
    "type": "kaya:callback/block/break",
    "on_break_action": {
        "type": "kaya:area_of_effect",
        "area": {
            "type": "kaya:radius",
            "target": "entity",
            "shape": "cube"
        }
    },
    "name": "Pressure",
    "description": "You're strong enough to cause shockwaves when breaking a block, damaging nearby entities."
}
```

As is, we're still missing crucial parts of the area, such as its position and its radius.

In this case, since we want the area to be relative to where the block was broken, we can use the `kaya:broken_block` context parameter provided by the [Callback Block Break (Power Type)](../power/callback_block_break.md). We'll give it an 8 blocks radius as well:

```json
{
    "type": "kaya:callback/block/break",
    "on_break_action": {
        "type": "kaya:area_of_effect",
        "area": {
            "type": "kaya:radius",
            "target": "entity",
            "shape": "cube",
            "position": {
                "type": "kaya:block/position",//(1)!
                "block": "kaya:broken_block"//(2)!
            },
            "radius": 8
        }
    },
    "name": "Pressure",
    "description": "You're strong enough to cause shockwaves when breaking a block, damaging nearby entities."
}
```


1. Since the `position` field requires a [vec3 provider][vec3_provider], we need to define a [vec3 provider][vec3_provider] that can accept a block.<br><br>In this case, we'll use the [Block Position (Vec3 Provider Type)](../value_provider/vec3/block_position.md).
2. The `block` field requires a [block provider][block_provider], but some providers can implicitly use a specific type when certain data types are specified.<br><br>In this case, it'll implictly use the [Context (Block Provider Type)](../value_provider/meta/context.md).


Now that the area is fully defined, we'll need to define the [action][action] that we want to execute on the entities within the area. Since we want to damage the entities, we'll use the [Damage Entity (Action Type)](../action/damage_entity.md).

To damage the entities within the area, we can use the `kaya:entity_in_area` context parameter provided by the [Area of Effect (Action Type)](../action/area_of_effect.md), which would, as its name suggest, refer to the entity within the area:

```json
{
    "type": "kaya:callback/block/break",
    "on_break_action": {
        "type": "kaya:area_of_effect",
        "area": {
            "type": "kaya:radius",
            "target": "entity",
            "shape": "cube",
            "position": {
                "type": "kaya:block/position",
                "block": "kaya:broken_block"
            },
            "radius": 8
        },
        "action": {
            "type": "kaya:damage_entity",
            "damage_type": "minecraft:generic",
            "amount": 4.0,
            "victim": "kaya:entity_in_area"//(1)!
        }
    },
    "name": "Pressure",
    "description": "You're strong enough to cause shockwaves when breaking a block, damaging nearby entities."
}
```


1. The `victim` field requires an [entity provider][entity_provider], but as mentioned earlier, entity providers can also implicitly use the [Context (Entity Provider Type)](../value_provider/meta/context.md).


Now with everything defined, this should now damage entities within an 8 radius cubic area whenever the entity holding the power breaks any block.

Hopefully, this tutorial has helped you understand the process of making powers and showcased the flexibility of Kaya. It's encouraged that you check out other pages for [powers][power], [actions][action], [conditions][condition], and [value providers][value_provider] to further familiarize yourself with Kaya's context system.
