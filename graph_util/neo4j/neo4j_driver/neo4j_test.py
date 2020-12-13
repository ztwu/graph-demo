from graph_util.neo4j.neo4j_driver.neo4j_util import Neo4jUtil

neo4jutil = Neo4jUtil()
neo4jutil.init_neo4j(uri="bolt://192.168.1.101:7687",auth=("neo4j", "123456"))

entityname1 = "ztwu_node_01\""
entityname2 = "ztwu_node_02\""
labelname1 = "ZTWU"
labelname2 = "ZTWU"
labelname = "ZTWU0"
entitypropertie1 = {'entityname': "ztwu_node_01\"",'properties':{"prop":"whm_01"}}
entitypropertie2 = {'entityname': "ztwu_node_02\"",'properties':{"prop":"whm_02"}}
rela_single = "测试"
relation_single = {'entityname1': "ztwu_node_01\"",'entityname2':"ztwu_node_02\""}

entitys_items = ["ztwu_node_03\"", "ztwu_node_04'"]
entitylabel = 'WHM'
entityproperties = [{'entityname': "ztwu_node_03\"",'properties':{"testbatch":"pro3"}},
                    {'entityname': "ztwu_node_04'",'properties':{"testbatch":"pro4"}}]
entity_labes = ["ztwu_node_05\"","ztwu_node_06'"]
rela = "测试202002131"
relations = [{'entityname1': "ztwu_node_03\"",'entityname2':"ztwu_node_04'"},
             {'entityname1': "ztwu_node_04'", 'entityname2': "ztwu_node_03\""}]

neo4jutil.single_node(entityname1)
neo4jutil.single_node_properties(entitypropertie1)
neo4jutil.single_node(entityname2)
neo4jutil.single_node_properties(entitypropertie2)
neo4jutil.single_node_relation(rela_single, relation_single)
neo4jutil.single_node_label(entityname1, labelname1)
neo4jutil.single_node_label(entityname2, labelname2)
neo4jutil.single_label(entityname1, labelname)
neo4jutil.single_label(entityname2, labelname)

neo4jutil.batch_node(entitys_items)
neo4jutil.batch_node_properties(entityproperties)
neo4jutil.bacth_node_label(entitylabel,entity_labes)
neo4jutil.bacth_labels(entitylabel,entitys_items)
neo4jutil.batch_relations(rela,relations)