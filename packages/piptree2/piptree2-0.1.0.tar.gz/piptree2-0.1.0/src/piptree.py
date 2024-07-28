import subprocess
from src.util import *


# 命令行方法
def list_dists(names):
    if len(names) > 0:
        graph = get_dict_names(names)
    else:
        graph = get_dict_graph()

    if graph:
        for node in graph:
            if graph[node]:
                continue
            show_tree(node)


def remove_dists(names, yes=True):
    if len(names) <= 0:
        return
    dists = get_set_names(names)
    graph = get_dict_graph()

    all_dead = find_all_dead(graph, dists)
    # print(f"all_dead: {len(all_dead)}")
    yes_dead = exclude_whitelist(all_dead)
    # print(f"yes_dead: {len(yes_dead)}")

    def confirm(prompt):
        return input(prompt) == "y"

    if dists and (yes or confirm("Uninstall (y/N)? ")):
        pip_cmd = ["pip"]
        if sys.executable:
            pip_cmd = [sys.executable, "-m", "pip"]
        if yes_dead:
            subprocess.check_call(pip_cmd + ["uninstall", "-y"] + [d.project_name for d in yes_dead])


if __name__ == '__main__':
    list_dists([])
    # remove_dists(['requests', 'fastapi'])
