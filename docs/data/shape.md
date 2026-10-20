#   Shape

A [string][string] that determines the shape of an area, which can be used for getting block positions and/or entities.


{% if shapes %}
{% set aliased = {} %}

### Values

Value | Description
------|------------
{%- for i in range(shapes|count) %}
{%- set shape = shapes[i] %}
{%- set key = i + 1 %}
`{{ shape.name}}`[^{{ key }}] | {{ shape.description}}
{%- if shape.aliases %}
{%- do aliased.update({key: shape.aliases}) %}
{%- endif %}
{%- endfor %}
{% endif %}

{% if aliased %}
{%- for key, aliases in aliased.items() %}
[^{{ key }}]: Aliases: {{ aliases|string_transform("`{}`")|join(", ") }}
{%- endfor %}
{% endif %}
