import re
import pymysql
import numpy as np


class PipelineToSqlOne:
    def __init__(self, mysql_host, mysql_port, mysql_database, mysql_user, mysql_password):
        self.mysql_host = mysql_host
        self.mysql_port = mysql_port
        self.mysql_database = mysql_database
        self.mysql_user = mysql_user
        self.mysql_password = mysql_password
        self.items = []

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mysql_host=crawler.settings.get('MYSQL_HOST'),
            mysql_port=crawler.settings.get('MYSQL_PORT'),
            mysql_database=crawler.settings.get('MYSQL_DATABASE'),
            mysql_user=crawler.settings.get('MYSQL_USER'),
            mysql_password=crawler.settings.get('MYSQL_PASSWORD')
        )

    def open_spider(self, spider):
        self.connection = pymysql.connect(
            host=self.mysql_host,
            user=self.mysql_user,
            password=self.mysql_password,
            database=self.mysql_database,
            port=self.mysql_port
        )
        self.cursor = self.connection.cursor()

    def process_item(self, item, spider):
        self.items.append(item)
        return item

    def remove_illegal_characters(self, text):
        # 移除非法字符的函数
        return re.sub(r'[\x00-\x1F\x7F-\x9F]', '', text)

    def clean_data(self, item):
        for key, value in item.items():
            if value == '':
                item[key] = None
            elif isinstance(value, float) and np.isnan(item[key]):
                item[key] = None
        return item

    def generate_insert_sql(self, table_name, items):
        # Extract the keys from the first item to create column names
        columns = ', '.join([f'`{key}`' for key in items[0].keys()])
        columns = columns.replace('%', '%%')
        values_placeholder = ', '.join(['%s' for _ in items[0].values()])

        # Create the SQL insert statement
        sql = f"""
        INSERT INTO {table_name}
        ({columns})
        VALUES ({values_placeholder})
        """

        # Generate the list of values tuples for executemany
        values_list = [tuple(item.values()) for item in items]

        return sql, values_list

    def close_spider(self, spider):
        sql, values_list = self.generate_insert_sql(spider.name, self.items)
        self.cursor.executemany(sql, values_list)

        self.connection.commit()
        self.cursor.close()
        self.connection.close()


class PipelineToSqlMany:
    def __init__(self, mysql_host, mysql_port, mysql_database, mysql_user, mysql_password, batch_size=100):
        self.mysql_host = mysql_host
        self.mysql_port = mysql_port
        self.mysql_database = mysql_database
        self.mysql_user = mysql_user
        self.mysql_password = mysql_password
        self.items = []
        self.batch_size = batch_size

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mysql_host=crawler.settings.get('MYSQL_HOST'),
            mysql_port=crawler.settings.get('MYSQL_PORT'),
            mysql_database=crawler.settings.get('MYSQL_DATABASE'),
            mysql_user=crawler.settings.get('MYSQL_USER'),
            mysql_password=crawler.settings.get('MYSQL_PASSWORD'),
            batch_size=crawler.settings.get('BATCH_SIZE', 5000)
        )

    def open_spider(self, spider):
        self.connection = pymysql.connect(
            host=self.mysql_host,
            user=self.mysql_user,
            password=self.mysql_password,
            database=self.mysql_database,
            port=self.mysql_port
        )
        self.cursor = self.connection.cursor()

    def process_item(self, item, spider):
        self.items.append(item)
        if len(self.items) >= self.batch_size:
            self.insert_items(spider.name)
        return item

    def generate_insert_sql(self, table_name, items):
        if not items:
            return None, None

        # Extract the keys from the first item to create column names
        columns = ', '.join([f'`{key}`' for key in items[0].keys()])
        columns = columns.replace('%', '%%')
        values_placeholder = ', '.join(['%s' for _ in items[0].values()])

        # Create the SQL insert statement
        sql = f"""
        INSERT INTO {table_name}
        ({columns})
        VALUES ({values_placeholder})
        """

        # Generate the list of values tuples for executemany
        values_list = [tuple(item.values()) for item in items]

        return sql, values_list

    def insert_items(self, table_name):
        sql, values_list = self.generate_insert_sql(table_name, self.items)
        if sql and values_list:
            try:
                self.cursor.executemany(sql, values_list)
                self.connection.commit()
            except pymysql.MySQLError as e:
                print(e)
                self.connection.rollback()  # Rollback in case of error
            else:
                self.items = []

    def close_spider(self, spider):
        if self.items:
            self.insert_items(spider.name)
        self.cursor.close()
        self.connection.close()
