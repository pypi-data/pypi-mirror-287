from simple_ddl_parser import DDLParser
import pprint

ddl = """create table Customer (
   Id int IDENTITY(1,1),
)"""

result = DDLParser(ddl).run()
pprint.pprint(result)


