# -*- coding: utf-8 -*-
# @Time    : 2020/9/27 15:32
# @Author  : ztwu4
# @Email   : ztwu4@iflytek.com
# @File    : janusgraph.py
# @Software: PyCharm
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection
from gremlin_python.structure.graph import Graph, Vertex, Edge

# graph2 = Graph()
# connection2 = DriverRemoteConnection('ws://192.168.56.101:8182/gremlin', 'graph2')
# graph2 = graph2.traversal().withRemote(connection2)
# graph2.addV("people").property("name",'ztwuceshi').next()
# print(graph2.V().toList())
#
graph = Graph()
connection = DriverRemoteConnection('ws://192.168.56.101:8182/gremlin', 'g')
g = graph.traversal().withRemote(connection)
# g.addV('god3').property('name', 'yuxj1').property('age', 111).next()
# g.addV('god3').property('name', 'yuxj2').property('age', 222).next()
# g.V().has("name","yuxj1").as_("a").V().has("name","yuxj2").addE('createdBy').to('a').property('acl','public').next()

# for v in g.V().hasLabel("god3").toList():
#     print(v, v.id, v.label, g.V(v.id).properties("name"))
#     properties = g.V(v.id).properties()
#     for p in properties:
#         print(p.key, p.value, p)

# for e in g.E().toList():
#     print(e.id["@value"]["relationId"], e.label, e.inV, e.outV)
    # properties = g.E('gm6-smo-4get-oe9kw').properties()
    # print(properties)
    # for p in properties:
    #     print(p)
    #     print(p.key, p.value, p)

print(g.V().has("name","yuxj1").outE().path())
print(g.V().has("name","yuxj1").outE("createdBy").V().has("name","yuxj2").as_("x").otherV().is_("x"))

# graph3 = Graph()
# connection3 = DriverRemoteConnection('ws://192.168.56.101:8182/gremlin', 'graph2')
# g3 = graph3.traversal().withRemote(connection3)
# vlits = g3.V().toList()
# for v in vlits:
#     print(v)
