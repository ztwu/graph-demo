from neo4j import GraphDatabase

from graph_util.graph_util import GraphUtil


class Neo4jUtil(GraphUtil):

    def init_neo4j(self, uri, auth):
        print("neo4j uri==",uri)
        print("neo4j auth==",auth)
        self.driver = GraphDatabase.driver(uri=uri, auth=auth)

    # 单个插入node
    def single_node(self, entityname):
        with self.driver.session() as session:
            session.write_transaction(self.add_node, entityname)

    # 单个插入包含label的node
    def single_node_label(self, entityname, labelname):
        with self.driver.session() as session:
            session.write_transaction(self.add_node_label, entityname, labelname)

    # 单个插入node标签
    def single_label(self, entityname, labelname):
        with self.driver.session() as session:
            session.write_transaction(self.add_label, entityname, labelname)

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
                    MERGE (n {{name: row}})
                    """.format(entitys_items=entitys_items)
        print("执行cypher-----", cyphersql)
        tx.run(cyphersql, entitys_items=entitys_items)

    # 批量插入node+label
    def batch_add_node_bylable(self, tx, label, entitys_items):
        print("---------entitys_items", entitys_items)
        cyphersql = """
                    UNWIND {{entitys_items}} as row
                    MERGE (n:{label} {{name: row}})
                    """.format(entitys_items=entitys_items, label=label)
        print("执行cypher-----", cyphersql)
        tx.run(cyphersql, entitys_items=entitys_items, label=label)

    # 批量插入node标签
    def batch_add_label(self, tx, labelname, entitys_items):
        print(entitys_items, "---", entitys_items)
        cyphersql = """
                    UNWIND {{entitys_items}} as entitiy
                    MATCH (n {{name: entitiy}})
                    SET n:{labelname}
                    """.format(entitys_items=entitys_items, labelname=labelname)
        print("执行cypher-----", cyphersql)
        tx.run(cyphersql, entitys_items=entitys_items, labelname=labelname)

    # 批量插入node属性
    def batch_add_node_properties(self, tx, entityproperties):
        print("---entityproperties", entityproperties)
        cyphersql = """
                    UNWIND {{entityproperties}} as row
                    MATCH (n {{name: row.entityname}})
                    SET n += row.properties
                    """.format(entityproperties=entityproperties)
        print("执行cypher-----", cyphersql)
        tx.run(cyphersql, entityproperties=entityproperties)

    # 批量插入某类type的relation
    def batch_add_relations(self, tx, rela, relations):
        print("---relations", relations)
        cyphersql = """
                    UNWIND {{relations}} as row
                    MATCH (n {{name: row.entityname1}})
                    MATCH (m {{name: row.entityname2}})
                    MERGE (n)-[r:{rela}]->(m)
                """.format(relations=relations, rela=rela)
        print("执行cypher-----", cyphersql)
        tx.run(cyphersql, relations=relations, rela=rela)

    # 单个插入node
    def add_node(self, tx, entityname):
        print("entityname",entityname)
        tx.run("MERGE (n { name: $entityname }) ", entityname=entityname)

    # 单个插入node+label
    def add_node_label(self, tx, entityname, labelname):
        print("entityname", entityname)
        cyphersql = """
                    WITH {{entityname}} as entityname
                    MERGE (n:{labelname} {{name: entityname}})
                    """.format(entityname=entityname, labelname=labelname)
        print("执行cypher-----", cyphersql)
        tx.run(cyphersql, entityname=entityname, labelname=labelname)

    # 单个插入node属性
    def add_node_properties(self, tx, entitypropertie):
        print("----------------entitypropertie",entitypropertie)
        cyphersql = """
                    WITH {{entitypropertie}} as row
                    MATCH (n {{name: row.entityname}})
                    SET n += row.properties
                    """.format(entitypropertie=entitypropertie)
        print("执行cypher-----", cyphersql)
        tx.run(cyphersql, entitypropertie=entitypropertie)

    # 单个插入node标签
    def add_label(self, tx, entitiy, labelname):
        print(entitiy,"---",labelname)
        cyphersql = """
                    WITH {{entitiy}} as entitiy
                    MATCH (n {{name: entitiy}})
                    SET n:{labelname}
                    """.format(entitiy=entitiy, labelname=labelname)
        print("执行cypher-----", cyphersql)
        tx.run(cyphersql, entitiy=entitiy, labelname=labelname)

    # 单个插入relation
    def add_node_rela(self, tx, rela, relation):
        print("---relation", relation)
        cyphersql = """
                    WITH {{relation}} as row
                    MATCH (n {{name: row.entityname1}})
                    MATCH (m {{name: row.entityname2}})
                    MERGE (n)-[r:{rela}]->(m)
                    """.format(relation=relation, rela=rela)
        print("执行cypher-----", cyphersql)
        tx.run(cyphersql, relation=relation, rela=rela)