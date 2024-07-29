"""Main function used to compute the imports graph for either fortran or python code."""
import networkx as nx
from math import sqrt
from tucan.imports_main import imports_of_repository

def get_importsgraph(
    path: str,
) -> nx.DiGraph:
    """
    Main function that builds the network X tree graph, this can show the graph with nobvisual
    and / or pyvis.

    Args:
        path (str): Path to the root folder of the code or file
        code_name (str): Name of the code

    Returns:
        graph (obj): NetworkX of the imports_graph
    """
    imports_dict, sizes_dict = imports_of_repository(path)
    
    def _resize(nlocs:int)->int:
        return 1+int(0.5*sqrt(nlocs))
    
    imports_graph = nx.DiGraph()
    for path_, imports_list in imports_dict.items():
        if path_ not in imports_graph:
            imports_graph.add_node(
                    path_,
                    NLOC =_resize(sizes_dict.get(path_,10)),
                    type="file"
                )
        for ref_ in imports_list:
            if  ref_.startswith("__external__"):
                continue

            if ref_ not in imports_graph:
                imports_graph.add_node(
                        ref_,
                        NLOC =_resize(sizes_dict.get(ref_,10)),
                        type="file"
                    )
            imports_graph.add_edge(
                path_,ref_,
            )
    
    return imports_graph

