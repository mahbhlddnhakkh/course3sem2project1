import open3d as o3d
import argparse
from src.share import print_dict_list, rotate_view, get_stock_o3d_data, draw_modes, padding_between

def parse_args():
    # "BunnyMesh" does weird stuff and not rendering with multiple geometries for whatever reason so I just removed it
    existing_meshes = ["ArmadilloMesh", "KnotMesh", "AvocadoModel", "DamagedHelmetModel", "FlightHelmetModel", "MonkeyModel", "SwordModel"]
    parser = argparse.ArgumentParser()
    parser.add_argument("--models", default=[existing_meshes[0]], choices=existing_meshes, nargs="*")
    parser.add_argument("--draw", default=[tuple(draw_modes.keys())[0]], choices=list(draw_modes.keys()), nargs="*")
    return parser.parse_args()

def main():
    args = parse_args()
    meshes = []
    i = 0
    for m in args.models:
        mesh = o3d.io.read_triangle_mesh(get_stock_o3d_data(m).path)
        mesh.translate((padding_between*i, 0.0, 0.0))
        mesh.compute_vertex_normals()
        meshes.append(mesh)
        i+=1
    print_dict_list(args.models, meshes)
    for mode in args.draw:
        print(mode)
        draw_modes[mode](meshes)

if (__name__ == "__main__"):
    main()
