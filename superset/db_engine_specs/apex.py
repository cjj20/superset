from flask_babel import gettext as __

from superset.db_engine_specs.mysql import MySQLEngineSpec

class ApexEngineSpec(MySQLEngineSpec):
  engine_name = "Apex"
