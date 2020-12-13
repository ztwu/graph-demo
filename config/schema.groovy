def defineGratefulDeadSchema(graph) {

    mgmt = graph.openManagement()

    Orchestra = mgmt.makeVertexLabel('Orchestra').make()
    Artist = mgmt.makeVertexLabel('Artist').make()
    Work = mgmt.makeVertexLabel('Work').make()
    Concert = mgmt.makeVertexLabel('Concert').make()

    title = mgmt.makePropertyKey('title').dataType(String.class).cardinality(Cardinality.SINGLE).make()
    compositionDate = mgmt.makePropertyKey('compositionYear').dataType(Integer.class).cardinality(Cardinality.SINGLE).make()
    soloInstrument = mgmt.makePropertyKey('soloInstrument').dataType(String.class).cardinality(Cardinality.SINGLE).make()

    mgmt.addProperties(Work, title, compositionDate, soloInstrument)

    name = mgmt.makePropertyKey('name').dataType(String.class).cardinality(Cardinality.SINGLE).make()
    nationality = mgmt.makePropertyKey('nationality').dataType(String.class).cardinality(Cardinality.SINGLE).make()
    gender = mgmt.makePropertyKey('gender').dataType(String.class).cardinality(Cardinality.SINGLE).make()

    mgmt.addProperties(Orchestra, name)
    mgmt.addProperties(Concert, name)
    mgmt.addProperties(Artist, name, nationality, gender)

    COMPOSER = mgmt.makeEdgeLabel('COMPOSER').multiplicity(MANY2ONE).make()
    SOLOIST = mgmt.makeEdgeLabel('SOLOIST').multiplicity(SIMPLE).make()
    CONDUCTOR = mgmt.makeEdgeLabel('CONDUCTOR').multiplicity(SIMPLE).make()
    ORCHESTRA = mgmt.makeEdgeLabel('ORCHESTRA').multiplicity(SIMPLE).make()
    INCLUDES = mgmt.makeEdgeLabel('INCLUDES').multiplicity(SIMPLE).make()

    mgmt.addConnection(COMPOSER, Work, Artist)
    mgmt.addConnection(SOLOIST, Work, Artist)
    mgmt.addConnection(CONDUCTOR, Work, Artist)
    mgmt.addConnection(ORCHESTRA, Concert, Orchestra)
    mgmt.addConnection(INCLUDES, Concert, Work)

    mgmt.commit()

}