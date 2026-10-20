#   Equipment Slot

A [string][string] that indicates a slot where an item can be equipped on to.


### Values

Value | Description
------|------------
{% set separator = joiner("\n") %}{% for equipment_slot in equipment_slots %}{{ separator() }}`{{ equipment_slot.name }}` | {{ equipment_slot.description }}{% endfor %}
