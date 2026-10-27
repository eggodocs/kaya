#   Welcome to Kaya's documentation!

This page contains the surface level information regarding this library, how it works, and what it provides for users to make data packs with. 

Kaya is a library that allows attaching "powers" to entities via data packs. This is a rewrite of the Apoli project by Apace.


##  General information

This library provides the following:


- A vanilla-esque context system which allows for certain types to interconnect with each other.
- Data-driven powers which gives an entity a certain "ability" when granted. These provide the context needed by other types to function.
- Actions and conditions that uses the context system to affect and check the state of the objects of a world respectively.
- Value providers of various types that uses the context system to provide a dynamic value, like providing the attribute value of an entity for a field.


!!! warning

    Kaya is **not** compatible with Apoli, nor does it have a translation layer for migrating old Apoli data, as it's a rewrite from the ground up.
