import pandas as pd
import datetime
import os

class PipelineToExcel:
    def __init__(self):
        self.items = []

    def process_item(self, item, spider):
        self.items.append(item)
        return item

    def close_spider(self, spider):
        df = pd.DataFrame(self.items)
        self.makdir()
        df.to_excel(f'./data/{spider.name}{datetime.date.today()}.xlsx', index=False)

    def makdir(self):
        # 获取当前工作目录
        current_directory = os.getcwd()

        # 目标文件夹的路径
        data_directory = os.path.join(current_directory, 'data')
        # 检查是否存在
        if not os.path.exists(data_directory):
            # 如果不存在，创建文件夹
            os.mkdir(data_directory)
            print(f"'{data_directory}' 已创建")


