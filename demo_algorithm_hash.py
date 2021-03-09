#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/9 15:53
# @Author : way
# @Site : 
# @Describe: 一致性哈希算法

class ConsistentHash(object):

    def __init__(self, nodes=None, n_number=3):
        self._n_number = n_number  # 每一个节点对应多少个虚拟节点，这里默认是3个
        self._node_dict = {}  # { node_hash: node }
        self._sort_list = []  # [ node_hash ]
        if nodes:
            for node in nodes:
                self.add_node(node)

    def add_node(self, node):
        for i in range(self._n_number):
            key = hash(f'{node}#{i}')
            self._node_dict[key] = node
            self._sort_list.append(key)
        self._sort_list.sort()

    def remove_node(self, node):
        for i in range(self._n_number):
            key = hash(f'{node}#{i}')
            del self._node_dict[key]
            self._sort_list.remove(key)

    def get_node(self, key_str):
        if self._sort_list:
            key = hash(key_str)
            for node_key in self._sort_list:
                if key <= node_key:
                    return self._node_dict[node_key]
            return self._node_dict[self._sort_list[0]]
        else:
            return None


if __name__ == "__main__":
    from faker import Faker

    node_list = []
    for i in range(10):
        node = f'172.16.1.{i}'
        node_list.append(node)
    yhash = ConsistentHash(node_list, 100)

    f = Faker(locale='zh_CN')
    result = {}
    for _ in range(10000):
        save_node = yhash.get_node(f.name())
        result[save_node] = result.get(save_node, 0) + 1

    for node in node_list:
        print(f'{node} 保存的记录数为 {result[node]}')
