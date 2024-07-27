import json
from copy import deepcopy


def print_node_cache(node_cache):
    cache = deepcopy(node_cache)
    for key in cache.keys():
        for child_key, v in cache[key].items():
            cache[key][child_key] = {
                "id": v["id"],
                "name": v["name"],
                "type": str(v["type"]),
            }
    print(json.dumps(cache, indent=2))
