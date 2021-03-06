from src.data_processing import data_loader
from src.data_processing import relevance_loader
from src.data_processing import query_loader
from src.data_processing import wiki_data_entity_loader
from src.data_processing.wiki_api_categories import WikiApiCategories
'''
loader = data_loader.data_loader()
relevance = relevance_loader.relevance_loader()
print(relevance.data)
queries = query_loader.query_loader()
print(queries.data)

for i in range(loader.start, loader.end):
    loader.load_preprocessed_data()
    tables = loader.get_table_ids(data=loader.currentData)
    #Use an inner loop to get the individual data
    for j in range(0, len(tables)):
        id = tables[j]
        print(loader.currentData[id])
'''

entities = wiki_data_entity_loader.WikiDataEntityLoader()
entity = entities.retrieveEntityByName("Douglas Adams")
related_entities = entities.retrieveRelatedEntities(entity["id"], 10)
print(len(related_entities))
categoriesLoader = WikiApiCategories()
print(categoriesLoader.get_data(entity["title"]))
print(categoriesLoader.getCategoryByEntityId(entity["id"]))

