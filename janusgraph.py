# -*- coding: utf-8 -*-
# @Time    : 2020/9/27 15:32
# @Author  : ztwu4
# @Email   : ztwu4@iflytek.com
# @File    : janusgraph.py
# @Software: PyCharm
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection
from gremlin_python.structure.graph import Graph

graph2 = Graph()
connection2 = DriverRemoteConnection('ws://192.168.56.101:8182/gremlin', 'graph2')
graph2 = graph2.traversal().withRemote(connection2)
graph2.addV("people").property("name",'ztwuceshi').next()
print(graph2.V().toList())

graph = Graph()
connection = DriverRemoteConnection('ws://192.168.56.101:8182/gremlin', 'g')
g = graph.traversal().withRemote(connection)
print(g.V().toList())

graph3 = Graph()
connection3 = DriverRemoteConnection('ws://192.168.56.101:8182/gremlin', 'graph2')
g3 = graph3.traversal().withRemote(connection3)
vlits = g3.V().toList()
for v in vlits:
    print(v)