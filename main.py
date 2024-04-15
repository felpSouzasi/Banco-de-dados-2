from database import Database
from writeAJson import writeAJson
from MotoristaDAO import MotoristaDAO
from cli import MotoristaCLI

db = Database(database="relatorio_05", collection="pessoas")
personModel = MotoristaDAO(database=db)


personCLI = MotoristaCLI(personModel)
personCLI.run()