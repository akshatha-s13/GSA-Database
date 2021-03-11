import factory

from gresq.database.models import Author
from gresq.database.dal import dal

LIST_SIZES = [1, 2, 3]


class EnvironmentConditionsFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Author
        sqlalchemy_session = dal.Session()
        sqlalchemy_session_persistence = "commit"

    dew_point = factory.Faker('pyfloat', positive=False, min_value=-100, max_value=100)
    ambient_temperature = factory.Faker('pyfloat', positive=False, min_value=-100, max_value=100)