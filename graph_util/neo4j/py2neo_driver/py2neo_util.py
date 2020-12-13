from py2neo import Graph, Node, Subgraph, NodeMatcher, Relationship, RelationshipMatcher

from graph_util.graph_util import GraphUtil


class Py2neoUtil(GraphUtil):

    def init_neo4j(self, uri, auth):
        self.graph = Graph(uri=uri, auth=auth)

    # 单个插入node
    def single_node(self, entityname):
        matcher = NodeMatcher(self.graph)
        node = matcher.match(name=entityname).first()
        print(node)
        if node is None:
            print("create node")
            newnode = Node(name=entityname)
            self.graph.create(newnode)

    # 单个插入包含label的node
    def single_node_label(self, entityname, labelname):

        matcher = NodeMatcher(self.graph)
        node = matcher.match(name=entityname).first()
        if node is None:
            mynode = Node(labelname, name=entityname)
            print("create node",mynode)
            self.graph.create(mynode)
        else:
            node.add_label(labelname)
            print("update node", node)
            self.graph.push(node)
    # 单个插入node标签
    def single_label(self, entityname, labelname):
        matcher = NodeMatcher(self.graph)
        node = matcher.match(name=entityname).first()
        node.add_label(label=labelname)
        self.graph.push(node)

    # 单个插入node属性
    def single_node_properties(self, entitypropertie):
        tx = self.graph.begin()
        nodelist = []

        entityname = entitypropertie["entityname"]
        properties = entitypropertie["properties"]

        matcher = NodeMatcher(self.graph)
        nodes = matcher.match(name=entityname)
        print("nodes-----------", list(nodes))
        # 将返回的“Match”类转成list
        new_nodes = list(nodes)
        ## 添加你要修改的东西
        for node in new_nodes:
            for (key, value) in properties.items():
                node[key] = value
            nodelist.append(node)
            print("node-------",node)
        sub = Subgraph(nodes=nodelist)
        # 调用push更新
        tx.push(sub)
        tx.commit()

    # 单个插入某类type的relation
    def single_node_relation(self, rela, relation):
        entityname1 = relation["entityname1"]
        entityname2 = relation["entityname2"]
        matcher = NodeMatcher(self.graph)
        node1 = matcher.match(name=entityname1).first()
        node2 = matcher.match(name=entityname2).first()
        print("node-----------", node1, node2)

        matcher = RelationshipMatcher(self.graph)
        old_relationship = matcher.match([node1, node2], r_type=rela).first()
        print("old_relationship-----------", old_relationship)

        if old_relationship is None:
            relationship = Relationship(node1, rela, node2, score=100)
            self.graph.create(relationship)

    # 批量插入node
    def batch_node(self, entitys_items):
        tx = self.graph.begin()
        newnodes = []
        matcher = NodeMatcher(self.graph)
        for data in entitys_items:
            node = matcher.match(name=data).first()
            if node is None:
                oneNode = Node()
                oneNode["name"] = data
                newnodes.append(oneNode)
        if len(newnodes)>0:
            print("newnodes---------",newnodes)
            sub = Subgraph(newnodes)
            tx.create(sub)
        tx.commit()

    # 批量插入node属性
    def batch_node_properties(self, entityproperties):
        tx = self.graph.begin()
        nodelist = []
        for data in entityproperties:
            entityname = data["entityname"]
            properties = data["properties"]
            # 找到你要找的Nodes
            matcher = NodeMatcher(self.graph)
            nodes = matcher.match(name=entityname)
            print("nodes-----------",list(nodes))
            # 将返回的“Match”类转成list
            new_nodes = list(nodes)
            ## 添加你要修改的东西
            for node in new_nodes:
                for (key,value) in properties.items():
                    node[key] = value
                print("node----",node)
                nodelist.append(node)
        sub = Subgraph(nodes=nodelist)
        # 调用push更新
        tx.push(sub)
        tx.commit()

    # 批量插入包含label的node
    def bacth_node_label(self, label, entity_labes):
        tx = self.graph.begin()
        newnodelist = []
        oldnodelist = []
        matcher = NodeMatcher(self.graph)
        for data in entity_labes:
            node = matcher.match(name=data).first()
            if node is None :
                oneNode = Node()
                oneNode.add_label(label=label)
                oneNode["name"] = data
                newnodelist.append(oneNode)
            else:
                node.add_label(label=label)
                oldnodelist.append(node)
        if len(newnodelist)>0:
            newsub = Subgraph(newnodelist)
            print("newnodelist----",newnodelist)
            tx.create(newsub)
        if len(oldnodelist)>0:
            oldsub = Subgraph(oldnodelist)
            print("oldnodelist----", oldnodelist)
            tx.push(oldsub)
        tx.commit()

    # 批量插入node标签
    def bacth_labels(self, label, entity_labes):
        tx = self.graph.begin()
        nodelist = []
        for data in entity_labes:
            # 找到你要找的Nodes
            matcher = NodeMatcher(self.graph)
            nodes = matcher.match(name=data)
            print("nodes-----------", list(nodes))
            # 将返回的“Match”类转成list
            new_nodes = list(nodes)
            ## 添加你要修改的东西
            for node in new_nodes:
                node.add_label(label=label)
                nodelist.append(node)
                print(node)
        if len(nodelist)>0:
            sub = Subgraph(nodes=nodelist)
            # 调用push更新
            tx.push(sub)
        tx.commit()

    # 批量插入某类type的relation
    def batch_relations(self, rela, relations):
        tx = self.graph.begin()
        new_relationships = []
        old_relationships = []
        for data in relations:
            entityname1 = data["entityname1"]
            entityname2 = data["entityname2"]
            matcher = NodeMatcher(self.graph)
            node1 = matcher.match(name=entityname1).first()
            node2 = matcher.match(name=entityname2).first()
            # print("node-----------", node1, node2)

            matcher = RelationshipMatcher(self.graph)
            old_relationship = matcher.match([node1, node2], r_type=rela).first()
            print("-------old_relationship", old_relationship)

            if old_relationship is None:
                relationship = Relationship(node1, rela, node2, score=100)
                print("-------relationship",relationship)
                new_relationships.append(relationship)

        if len(new_relationships)>0:
            print("new_relationships--------",new_relationships)
            sub = Subgraph(relationships=new_relationships)
            tx.create(sub)

        tx.commit()