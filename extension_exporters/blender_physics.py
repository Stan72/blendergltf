def export_physics(obj):
    body = obj.rigid_body
    physics = {
        'collisionShape': body.collision_shape.upper(),
        'mass': body.mass,
        'static': body.type == 'PASSIVE',
        'dimensions': obj.dimensions[:],
    }

    if body.collision_shape in ('CONVEX_HULL', 'MESH'):
        physics['mesh'] = 'mesh_' + obj.data.name

    return physics

def export(state):
    data_pairs = [
        (obj, state['output']['nodes'][state['refmap'][('objects', obj.name)]])
        for obj in state['input']['objects']
        if obj.rigid_body
    ]


    state['extensions_used'].append('BLENDER_physics')
    for obj, node in data_pairs:
        node['extensions'] = node.get('extensions', {})
        node['extensions']['BLENDER_physics'] = export_physics(obj)
        print(node)