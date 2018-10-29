>  Was ist das besondere an den bpy-Collections?

* Edit any data the user interface can (Scenes, Meshes, Particles etc.)
* Modify user preferences, keymaps and themes
* Run tools with own settings
* Create user interface elements such as menus, headers and panels
* Create new tools
* Create interactive tools
* Create new rendering engines that integrate with Blender
* Define new settings in existing Blender data
* Draw in the 3D view using OpenGL commands from Python

> Wie wird ein neues Mesh erzeugt?

* Über den Befehl 
```Python
bpy.ops.mesh.primitive_cube_add(...)
bpy.ops.mesh.primitive_circle_add(...)
...
          circle_add(
                           cone_add(
                           cube_add(
                           cylinder_add(
                           grid_add(
                           ico_sphere_add(
                           monkey_add(
                           plane_add(
                           torus_add(
                           uv_sphere_add(
```

> Wie setze ich das aktuell selektierte Objekt in Python?

??

