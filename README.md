# Project description

### Databse directory : 
Hadi kat defini la configiration necessaire bach ndiro une connexion avec une base de donnee Sqlite, L ORM utilise hnaya how SQLAlchemy
### Repository directory : 
Hadi kan injectew feha wahed la **Session Factory** li saybnaha fl cofiguration, w kat5lina ndiro des transaction avec l bd.
### Service directory : 
Hnaya kaym jouj hwayj, kayn **LLMService** whcich loads an LLM from Hugging face 3nd locally using the transformers API. 
w kayna **CrudService** dial l user, li kan injectew feha repository
### Controller layer wla api layer
hadi kat5lina n definiw des Routers ( controllers ) for each one of the services li devloppinahum wla ghadi n devloppewhum, bach n exposew dkchi l frontend. 

### tests directory
Les test dial l crud ( repository w hta service) derthum b wahed library smitha pytest ( les bonnes pratiques ) 

### MZL MAKAYNCH CONTROLLER DIAL CRUD SERVICES
### MZL MAKAYNCH AUTHENTICATION SERVICE
