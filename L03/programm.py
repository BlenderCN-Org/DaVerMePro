import bpy

#Variablen

#TransformTranslate
transformTranslateX = -2
transformTranslateY = 7
transformTranslateZ = 1

#TransformResize
transforResizeX = 0.805539
transforResizeY = 0.805539
transforResizeZ = 0.805539


for i in range(5):
    bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":(transformTranslateX , transformTranslateY, transformTranslateZ), "constraint_axis":(False, False, True), "constraint_orientation":'NORMAL'})
    bpy.ops.transform.resize(value=(transforResizeX, transforResizeY, transforResizeZ), constraint_axis=(False, False, False))
    bpy.ops.transform.rotate(value=-0.475515, axis=(1, 0, 1), constraint_axis=(True, True, False))


# +++ Old Code +++ 
# Check veränderung

# for i in range(5):
#     bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"mirror":False}, TRANSFORM_OT_translate={"value":(-1.49012e-08, 7.45058e-09, 0.364329), "constraint_axis":(False, False, True), "constraint_orientation":'NORMAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False})
#     bpy.ops.transform.rotate(value=-0.475515, axis=(0, 0, 1), constraint_axis=(True, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)



# Vorlesung behandelt.
# for i in range(5):
#     bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"mirror":False}, TRANSFORM_OT_translate={"value":(-1.49012e-08, 7.45058e-09, 0.364329), "constraint_axis":(False, False, True), "constraint_orientation":'NORMAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False})
#     bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"mirror":False}, TRANSFORM_OT_translate={"value":(-1.49012e-08, 7.45058e-09, 0.364329), "constraint_axis":(False, False, True), "constraint_orientation":'NORMAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False})


