from graph_util.neo4j.py2neo_driver.py2neo_util import Py2neoUtil

neo4jutil = Py2neoUtil()
neo4jutil.init_neo4j(uri="bolt://192.168.1.101:7687",auth=("neo4j", "123456"))

entitys_items = ["20200214_ztwu_node_031\"", "20200214_ztwu_node_041'"]
entitylabel = '20200214_WHM10'
entityproperties = [{'entityname': "20200214_ztwu_node_03\"",'properties':{"testbatch112":"pro23222"}},
                    {'entityname': "20200214_ztwu_node_04'",'properties':{"testbatch112":"pro242222"}}]
entity_labes = ["20200214_ztwu_node_07\"","20200214_ztwu_node_08'"]
rela = "20200214_测试11"
relations = [{'entityname1': "20200214_ztwu_node_03\"",'entityname2':"20200214_ztwu_node_04'"},
             {'entityname1': "20200214_ztwu_node_04'", 'entityname2': "20200214_ztwu_node_03\""}]

entityname1 = "20200214_ztwu_node_011\""
entityname2 = "20200214_ztwu_node_02\""
labelname1 = "20200214_ZTWU5"
labelname2 = "20200214_ZTWU5"
labelname = "20200214_ZTWU0"
entitypropertie1 = {'entityname': "20200214_ztwu_node_01\"",'properties':{"prop":"whm_0111"}}
entitypropertie2 = {'entityname': "20200214_ztwu_node_02\"",'properties':{"prop":"whm_0211"}}
rela_single = "20200214_测试2"
relation_single = {'entityname1': "20200214_ztwu_node_01\"",'entityname2':"20200214_ztwu_node_02\""}

# neo4jutil.batch_node(entitys_items)
# neo4jutil.bacth_labels(entitylabel,entitys_items)
# neo4jutil.bacth_node_label(entitylabel,entity_labes)
# neo4jutil.batch_node_properties(entityproperties)
neo4jutil.batch_relations(rela,relations)

# neo4jutil.single_node(entityname1)
# neo4jutil.single_node_properties(entitypropertie1)
# neo4jutil.single_node(entityname2)
# neo4jutil.single_node_properties(entitypropertie2)
# neo4jutil.single_node_relation(rela_single, relation_single)
# neo4jutil.single_node_label(entityname1, labelname1)
# neo4jutil.single_node_label(entityname2, labelname2)
# neo4jutil.single_label(entityname1, labelname)
# neo4jutil.single_label(entityname2, labelname)