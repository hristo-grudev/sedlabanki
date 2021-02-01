import re
import sqlite3


class SedlabankiPipeline:
    conn = sqlite3.connect('sedlabanki.db')
    cursor = conn.cursor()

    def open_spider(self, spider):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS `sedlabanki` (
                                                    title varchar(100),
                                                    description text,
                                                    date text
                                                    )''')
        self.conn.commit()

    def process_item(self, item, spider):
        try:
            title = item['title']
            title = re.sub('"', "'", title)
        except:
            title = ''
        try:
            description = item['description'].strip()
            description = re.sub('"', "'", description)
        except:
            description = ''
        try:
            date = item['date'].strip()
        except:
            date = ''

        self.cursor.execute(f'''select * from sedlabanki where title = "{title}" and date = "{date}"''')
        is_exist = self.cursor.fetchall()

        if len(is_exist) == 0:
            self.cursor.execute(
                f'''insert into `sedlabanki` (`title`, `description`, `date`) values ("{title}", "{description}", "{date}")'''
            )
            self.conn.commit()

        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()
