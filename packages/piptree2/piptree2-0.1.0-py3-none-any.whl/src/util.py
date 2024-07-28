import sys

from collections import defaultdict
from pkg_resources import (
    DistributionNotFound,
    VersionConflict,
    get_distribution,
    working_set, Requirement,
)


# 辅助方法
def get_set_names(names=None):
    g = set()
    for name in names:
        dist = get_dist(name)
        if dist is None:
            continue
        g.add(dist)
    return g


def get_dict_names(names=None):
    g = defaultdict(set)
    for name in names:
        dist = get_dist(name)
        if dist is None:
            continue
        g[dist]
        for req in requires(dist):
            g[req].add(dist)
    return g


def get_dict_graph():
    g = defaultdict(set)
    for dist in working_set:
        if dist is None:
            continue
        g[dist]
        for req in requires(dist):
            g[req].add(dist)
    return g


def requires(dist) -> list:
    required = []
    # print(f"requires: {dist.requires}")
    # print(f"requires(): {dist.requires()}")
    if dist and dist.requires():
        for req in dist.requires():
            required.append(get_dist(req))
    required.sort(key=lambda x: x.project_name)
    return required


def get_dist(pkg):
    dist = None
    try:
        if isinstance(pkg, str):
            pkg = Requirement.parse(pkg)
        dist = get_distribution(pkg)
    except VersionConflict as e:
        print(e.report(), file=sys.stderr)
        dist = get_distribution(pkg.project_name)
    except DistributionNotFound as e:
        print(e.report(), file=sys.stderr)

    # print(f"pkg: {pkg}")
    # print(f"get_dist: {dist}")
    return dist


def show_tree(dist, depth=0, visited=None):
    if dist is None:
        return
    if visited is None:
        visited = set()
    if dist in visited:
        return
    visited.add(dist)
    show_dist(dist, depth)
    for req in requires(dist):
        show_tree(req, depth + 1, visited)


def show_dist(dist, depth, freeze=True):
    if dist is None:
        return
    if depth == 0:
        print("" + str(dist.as_requirement()))
    else:
        print(" " * 2 * depth + "- " + str(dist.as_requirement()))


WHITELIST = ["pip", "setuptools", "piptree", "wheel"]


def exclude_whitelist(dists):
    return {dist for dist in dists if dist and dist.project_name not in WHITELIST}


def find_all_dead(graph, start):
    while True:
        y = find_dead(graph, start)
        if y == start:
            break
        start = y

    return start


def find_dead(graph, dead):
    node_set = set()
    for node in graph:
        has_child = graph[node]
        # 计算set差集：set1 - set2 在第一个集合中，但不在第二个集合中的元素
        if has_child and not (has_child - dead):
            node_set.add(node)
    # 计算set并集：set1 | set2 两个集合的所有元素，重复的元素只保留一个
    return dead | node_set


# def find_all_dead(graph, start):
#     print()
#     print(f"graph: {graph}")
#     print(f"start: {start}")
#
#     def fixed_point(f, x):
#         while True:
#             y = f(x)
#             if y == x:
#                 return x
#             x = y
#
#     def find_dead(graph, dead):
#         def is_killed_by_us(node):
#             succ = graph[node]
#             return succ and not (succ - dead)
#
#         return dead | set(filter(is_killed_by_us, graph))
#
#     return fixed_point(lambda d: find_dead(graph, d), start)
