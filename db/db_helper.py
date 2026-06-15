import sqlite3


class DB:

    def __init__(

        self

    ):

        self.conn = (

            sqlite3.connect(
                "database.db"
            )

        )

        self.cursor = (

            self.conn.cursor()

        )


    def insert_user(

        self,

        user_id,

        name,

        job

    ):

        self.cursor.execute(

            """
            INSERT INTO users
            VALUES(
                ?,
                ?,
                ?
            )
            """,

            (

                user_id,

                name,

                job

            )

        )

        self.conn.commit()


    def get_user(

        self,

        user_id

    ):

        self.cursor.execute(

            """
            SELECT *
            FROM users
            WHERE id=?
            """,

            (

                user_id,

            )

        )

        return (

            self.cursor.fetchone()

        )


    def cleanup(

        self,

        user_id

    ):

        self.cursor.execute(

            """
            DELETE
            FROM users
            WHERE id=?
            """,

            (
                user_id,
            )

        )

        self.conn.commit()


    def close(

        self

    ):

        self.conn.close()