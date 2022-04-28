# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql


class LianjiaPipeline:

    def process_item(self, item, spider):
        print(dict(item))
        return item


class LianjiaMysqlPipeline:
    def open_spider(self, spider):
        self.db = pymysql.connect(user='root',
                                  password='hechuan520',
                                  host='127.0.0.1',
                                  port=3306,
                                  database='sell'
                                  )
        # 创建游标
        self.cursor = self.db.cursor()

    # def create_table(self, spider):
    #     sql_table = '''
    #                     create table if not exists lianjia(title varchar(100),house_type varchar(100),
    #                     area varchar(100),total_price varchar(100)) default charset=utf8;
    #             '''
    #     self.cursor.execute(sql_table)

    def process_item(self, item, spider):
        insert_sql = '''    
                   insert into lianjia(title,house_type, area, total_price) values (%s,%s,%s,%s);
                   '''
        self.cursor.execute(insert_sql, [item['title'], item['house_type'], item['area'], item['total_price']])
        # 提交到数据库执行
        try:
            self.db.commit()
        except:
            print('error!')
            self.db.rollback()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.db.close()
