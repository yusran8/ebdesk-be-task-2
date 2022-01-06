import mysql.connector

class Mysql_connector():
    def __init__(self):
        self.db = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            passwd = 'TerminateItself99',
            database = 'ebdesk',
            
        )

    def insert(self, datas):
        cursor = self.db.cursor()

        for data in datas:
            channel_id = data['channel_id']
            title = data['title']
            channel_name = data['channel_name']
            waktu_publish = data['waktu_publish']

            sql = "insert into videos(channel_id, title, channel_name, waktu_publish) values(%s, %s, %s, %s)"
            value = (channel_id, title, channel_name, waktu_publish)

            cursor.execute(sql, value)
            cursor.execute('commit')
