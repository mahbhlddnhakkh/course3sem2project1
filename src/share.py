import open3d as o3d
import numpy as np
import time

spin_deg = 1.0*np.pi/180.0
fps = 60.0
padding_between = 200.0

def vis_spin(gs):
    # https://www.open3d.org/docs/release/tutorial/visualization/non_blocking_visualization.html
    vis = o3d.visualization.Visualizer()
    vis.create_window()
    for g in gs:
        vis.add_geometry(g)
    running = True
    while (running):
        i = 0
        for g in gs:
            g.rotate(g.get_rotation_matrix_from_axis_angle([0, spin_deg, 0.0]))
            vis.update_geometry(g)
            i+=1
        running = vis.poll_events()
        vis.update_renderer()

def o3dvis_spin(gs):
    def tick():
        app = o3d.visualization.gui.Application.instance
        tick_return = app.run_one_tick()
        if tick_return:
            vis.post_redraw()
        return tick_return
    # https://github.com/isl-org/Open3D/issues/2869
    # https://github.com/isl-org/Open3D/issues/5067
    app = o3d.visualization.gui.Application.instance
    app.initialize()
    vis = o3d.visualization.O3DVisualizer()
    app.add_window(vis)
    i = 0
    for g in gs:
        vis.add_geometry(str(i), g)
        i += 1
    vis.reset_camera_to_default()
    running = True
    while (running):
        i = 0
        for g in gs:
            vis.remove_geometry(str(i))
            g.rotate(g.get_rotation_matrix_from_axis_angle([0, spin_deg, 0.0]))
            vis.add_geometry(str(i), g)
            i+=1
        running = tick()
        time.sleep(1.0/fps)

draw_modes = {
    "vis_spin": vis_spin,
    "o3dvis_spin": o3dvis_spin,
    "draw_geometries": lambda gs: o3d.visualization.draw_geometries(gs),
    "draw": lambda gs: o3d.visualization.draw(gs),
    #"draw_geometries_rotate": lambda gs: o3d.visualization.draw_geometries_with_animation_callback(gs, rotate_view), # replace with vis_spin
    "draw_geometries_wireframe": lambda gs: o3d.visualization.draw_geometries(gs, mesh_show_wireframe=True),
    "draw_geometries_back_face": lambda gs: o3d.visualization.draw_geometries(gs, mesh_show_back_face=True),
    "draw_geometries_wireframe_back_face": lambda gs: o3d.visualization.draw_geometries(gs, mesh_show_wireframe=True, mesh_show_back_face=True),
}

def print_dict_list(names, values) -> None:
    d = tuple(zip(names, values))
    if (len(d) == 0):
        print({})
        return
    print("{'%s': %s" % (d[0][0], d[0][1]), end="")
    for i in range(1, len(d)):
        print(", '%s': %s" % (d[i][0], d[i][1]), end="")
    print("}")

def rotate_view(vis, *args, **kwargs) -> bool:
    ctr = vis.get_view_control()
    ctr.rotate(1.0, 0.0)
    return False

def get_stock_o3d_data(name):
    return eval(f"o3d.data.{name}")()
