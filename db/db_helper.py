import sqlite3


class DB:

    def connect(self):

        return sqlite3.connect(
            "database.db"
        )


    def insert_user(
        self,
        user_id,
        name,
        job
    ):

        conn = self.connect()

        cursor = conn.cursor()

        cursor.execute(
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

        conn.commit()

        conn.close()


    def get_user(
        self,
        user_id
    ):

        conn = self.connect()

        cursor = conn.cursor()

        cursor.execute(

            """
            SELECT *
            FROM users
            WHERE id=?
            """,

            (
                user_id,
            )

        )

        result = cursor.fetchone()

        conn.close()

        return result