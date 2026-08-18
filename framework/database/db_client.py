from sqlalchemy import create_engine, text


class DBClient:

    def __init__(self, connection_string):

        self.engine = create_engine(
            connection_string
        )

    def execute_query(self, query):

        with self.engine.connect() as connection:

            result = connection.execute(
                text(query)
            )

            return result.fetchall()


    def execute_update(self, query):

        with self.engine.begin() as connection:

            connection.execute(
                text(query)
        )

    def close(self):

        self.engine.dispose()            