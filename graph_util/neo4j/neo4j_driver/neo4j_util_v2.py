# -*- coding: utf-8 -*-
# @Time    : 2020/4/14 14:46
# @Author  : ztwu4
# @Email   : ztwu4@iflytek.com
# @File    : http_util.py
# @Software: neo4j操作

from neo4j import GraphDatabase

class Neo4jUtil():

    # 初始化数据库
    def init_neo4j(self, uri, auth):
        print("neo4j uri==",uri)
        print("neo4j auth==",auth)
        self.driver = GraphDatabase.driver(uri=uri, auth=auth)

    # 执行通用的cypher
    def execute_cyphersql(self, cyphersql):
        print("执行sql: ", cyphersql)
        with self.driver.session() as session:
            session.run(cyphersql)

    # 执行通用的cypher,关系查询
    def execute_cyphersql_relation(self, cyphersql):
        print("执行sql: ", cyphersql)
        result = list()
        with self.driver.session() as session:
            rs = session.run(cyphersql)
            records = rs.records()
            for record in records:
                # print(record)
                m = record.get("m")
                n = record.get("n")
                r = record.get("r")

                m_id = m.id
                m_labels = list(m.labels)
                m_properties = {}
                m_properties_temp = list(m.items())
                for item in m_properties_temp:
                    m_properties.setdefault(item[0],item[1])
                start = {
                    "id": m_id,
                    "labels": m_labels,
                    "properties": m_properties
                }

                n_id = n.id
                n_labels = list(n.labels)
                n_properties = {}
                n_properties_temp = list(n.items())
                for item in n_properties_temp:
                    n_properties.setdefault(item[0], item[1])
                end = {
                    "id": n_id,
                    "labels": n_labels,
                    "properties": n_properties
                }

                r_id = r.id
                r_type = r.type
                r_properties = {}
                r_properties_temp = list(r.items())
                for item in r_properties_temp:
                    r_properties.setdefault(item[0], item[1])
                relation = {
                    "id": r_id,
                    "type": r_type,
                    "properties": r_properties
                }

                temp = {
                    "start": start,
                    "end": end,
                    "relation": relation
                }
                result.append(temp)
        print(result)
        return result

    # 执行通用的cypher,实体查询
    def execute_cyphersql_entity(self, cyphersql):
        print("执行sql: ", cyphersql)
        result = list()
        with self.driver.session() as session:
            rs = session.run(cyphersql)
            records = rs.records()
            for record in records:
                for key,value in record.items():
                    properties = {}
                    properties_temp = list(value.items())
                    for item in properties_temp:
                        properties.setdefault(item[0], item[1])
                    temp = {
                        "id": value.id,
                        "labels": list(value.labels),
                        "properties": properties
                    }
                    result.append(temp)
        print(result)
        return result

    # 单个插入node
    def single_node(self, id, entityname):
        with self.driver.session() as session:
            session.write_transaction(self.add_node, id, entityname)

    # 单个插入包含label的node
    def single_node_label(self, id, entityname, labelname):
        with self.driver.session() as session:
            session.write_transaction(self.add_node_label, id, entityname, labelname)

    # 单个插入node标签
    def single_label(self, entitid, labelname):
        with self.driver.session() as session:
            session.write_transaction(self.add_label, entitid, labelname)

    # 单个插入node属性
    def single_node_properties(self, entitypropertie):
        with self.driver.session() as session:
            session.write_transaction(self.add_node_properties, entitypropertie)

    # 单个插入某类type的relation
    def single_node_relation(self, rela, relation):
        with self.driver.session() as session:
            session.write_transaction(self.add_node_rela, rela, relation)

##############################################################################################

    # 批量插入node
    def batch_node(self, entitys_items):
        with self.driver.session() as session:
            session.write_transaction(self.batch_add_node, entitys_items)

    # 批量插入node属性
    def batch_node_properties(self, entityproperties):
        with self.driver.session() as session:
            session.write_transaction(self.batch_add_node_properties, entityproperties)

    # 批量插入包含label的node
    def bacth_node_label(self, label, entity_labes):
        with self.driver.session() as session:
            session.write_transaction(self.batch_add_node_bylable, label, entity_labes)

    # 批量插入node标签
    def bacth_labels(self, label, entity_labes):
        with self.driver.session() as session:
            session.write_transaction(self.batch_add_label, label, entity_labes)

    # 批量插入某类type的relation
    def batch_relations(self, rela, relations):
        with self.driver.session() as session:
            session.write_transaction(self.batch_add_relations, rela, relations)

##############################################################################################

    #批量插入node
    def batch_add_node(self, tx, entitys_items):
        print("---------entitys_items", entitys_items)
        cyphersql = """
                    UNWIND {{entitys_items}} as row
                    MERGE (n {{entityid: row.entityid, name: row.entityname }})
                    """.format(entitys_items=entitys_items)
        print("执行cypher-----", cyphersql)
        tx.run(cyphersql, entitys_items=entitys_items)

    # 批量插入node+label
    def batch_add_node_bylable(self, tx, label, entitys_items):
        print("---------entitys_items", entitys_items)
        cyphersql = """
                    UNWIND {{entitys_items}} as row
                    MERGE (n:{label} {{entityid: row.entityid, name: row.entityname}})
                    """.format(entitys_items=entitys_items, label=label)
        print("执行cypher-----", cyphersql)
        tx.run(cyphersql, entitys_items=entitys_items, label=label)

    # 批量插入node标签
    def batch_add_label(self, tx, labelname, entitys_items):
        print(entitys_items, "---", entitys_items)
        cyphersql = """
                    UNWIND {{entitys_items}} as entityid
                    MATCH (n {{entityid: entityid}})
                    SET n:{labelname}
                    """.format(entitys_items=entitys_items, labelname=labelname)
        print("执行cypher-----", cyphersql)
        tx.run(cyphersql, entitys_items=entitys_items, labelname=labelname)

    # 批量插入node属性
    def batch_add_node_properties(self, tx, entityproperties):
        print("---entityproperties", entityproperties)
        cyphersql = """
                    UNWIND {{entityproperties}} as row
                    MATCH (n {{entityid: row.entityid}})
                    SET n += row.properties
                    """.format(entityproperties=entityproperties)
        print("执行cypher-----", cyphersql)
        tx.run(cyphersql, entityproperties=entityproperties)

    # 批量插入某类type的relation
    def batch_add_relations(self, tx, rela, relations):
        print("---relations", relations)
        cyphersql = """
                    UNWIND {{relations}} as row
                    MATCH (n {{entityid: row.entityid1}})
                    MATCH (m {{entityid: row.entityid2}})
                    MERGE (n)-[r:{rela}]->(m)
                """.format(relations=relations, rela=rela)
        print("执行cypher-----", cyphersql)
        tx.run(cyphersql, relations=relations, rela=rela)

    # 单个插入node
    def add_node(self, tx, id, entityname):
        print("entityname",entityname)
        tx.run("MERGE (n {entityid: $id, name: $entityname }) ", id=id, entityname=entityname)

    # 单个插入node+label
    def add_node_label(self, tx, id, entityname, labelname):
        entity = {"entityname": entityname, "id": id}
        print("entity", entity)
        cyphersql = """
                    WITH {{entity}} as entity
                    MERGE (n:{labelname} {{entityid: entity.id, name: entity.entityname}})
                    """.format(entity=entity, labelname=labelname)
        print("执行cypher-----", cyphersql)
        tx.run(cyphersql, entity=entity, labelname=labelname)

    # 单个插入node属性
    def add_node_properties(self, tx, entitypropertie):
        print("----------------entitypropertie",entitypropertie)
        cyphersql = """
                    WITH {{entitypropertie}} as row
                    MATCH (n {{entityid: row.entityid}})
                    SET n += row.properties
                    """.format(entitypropertie=entitypropertie)
        print("执行cypher-----", cyphersql)
        tx.run(cyphersql, entitypropertie=entitypropertie)

    # 单个插入node标签
    def add_label(self, tx, entityid, labelname):
        print(entityid,"---",labelname)
        cyphersql = """
                    WITH {{entityid}} as entityid
                    MATCH (n {{entityid: entityid}})
                    SET n:{labelname}
                    """.format(entityid=entityid, labelname=labelname)
        print("执行cypher-----", cyphersql)
        tx.run(cyphersql, entityid=entityid, labelname=labelname)

    # 单个插入relation
    def add_node_rela(self, tx, rela, relation):
        print("---relation", relation)
        cyphersql = """
                    WITH {{relation}} as row
                    MATCH (n {{entityid: row.entityid1}})
                    MATCH (m {{entityid: row.entityid2}})
                    MERGE (n)-[r:{rela}]->(m)
                    """.format(relation=relation, rela=rela)
        print("执行cypher-----", cyphersql)
        tx.run(cyphersql, relation=relation, rela=rela)

if __name__ == '__main__':
    from tools.config_util import ConfigUtil
    config_util = ConfigUtil()
    uri, username, password = config_util.get_database("neo4j")
    neo4j_util = Neo4jUtil()
    neo4j_util.init_neo4j(uri=uri, auth=(username, password))

    # neo4j_util.single_node("003","user03")
    # neo4j_util.single_node_label("001", "user01", "用户")
    # neo4j_util.single_node_label("002", "user02", "用户")
    # neo4j_util.single_node_properties({"entityid":"001","properties":{"age":24, "en_name":"ztwu4"}})
    # neo4j_util.single_label("003","职工")
    # neo4j_util.single_node_relation("同事",{"entityid1":"001","entityid2":"002"})

    # neo4j_util.batch_node([
    #     {"entityid":"005", "entityname":"user05"},
    #     {"entityid":"006", "entityname":"user06"}
    # ])

    neo4j_util.bacth_node_label("学生",[
        {"entityid": "005", "entityname": "user07"},
        {"entityid": "006", "entityname": "user08"}
    ])