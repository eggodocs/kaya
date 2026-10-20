#   Equipment Slot Group

A [string][string] that determines a group of equipment slots.

{% set hand_slots = [] %}
{% set armor_slots = [] %}
{% set other_slots = [] %}

{% for equipment_slot in equipment_slots %}
{% if equipment_slot.type == "hand" %}
{% do hand_slots.append(equipment_slot) %}
{% elif equipment_slot.type == "humanoid_armor" %}
{% do armor_slots.append(equipment_slot) %}
{% else %}
{% do other_slots.append(equipment_slot) %}
{% endif %}
{% endfor %}


### Values

Value | Description
------|------------
`any` | Any equipment slot.
{%- if hand_slots -%}
{% for hand_slot in hand_slots %}
`{{ hand_slot.name }}` | {{ hand_slot.description }}
{%- endfor -%}
{% endif %}
`hand` | Any equipment slot that's a hand slot.
{%- if armor_slots -%}
{% for armor_slot in armor_slots %}
`{{ armor_slot.name }}` | {{ armor_slot.description }}
{%- endfor -%}
{% endif %}
`armor` | Any equipment slot that's an armor slot.
{%- if other_slots -%}
{% for other_slot in other_slots %}
`{{ other_slot.name }}` | {{ other_slot.description }}
{%- endfor -%}
{% endif %}
