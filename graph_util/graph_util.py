from abc import ABCMeta,abstractmethod

class GraphUtil(metaclass=ABCMeta):

    @abstractmethod
    def init_neo4j(self, uri, auth):
        pass

    @abstractmethod
    # 单个插入node
    def single_node(self, entityname):
        pass

    @abstractmethod
    # 单个插入包含label的node
    def single_node_label(self, entityname, labelname):
        pass

    @abstractmethod
    # 单个插入node标签
    def single_label(self, entityname, labelname):
        pass

    @abstractmethod
    # 单个插入node属性
    def single_node_properties(self, entitypropertie):
        pass

    @abstractmethod
    # 单个插入某类type的relation
    def single_node_relation(self, rela, relation):
        pass

    @abstractmethod
    # 批量插入node
    def batch_node(self, entitys_items):
        pass

    @abstractmethod
    # 批量插入node属性
    def batch_node_properties(self, entityproperties):
        pass

    @abstractmethod
    # 批量插入包含label的node
    def bacth_node_label(self, label, entity_labes):
        pass

    @abstractmethod
    # 批量插入node标签
    def bacth_labels(self, label, entity_labes):
        pass

    @abstractmethod
    # 批量插入某类type的relation
    def batch_relations(self, rela, relations):
        pass

