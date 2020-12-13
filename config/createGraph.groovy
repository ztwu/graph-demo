:load ztwu/schema/schema.groovy
graph = JanusGraphFactory.open('conf/janusgraph-hbase-es.properties')
defineGratefulDeadSchema(graph)