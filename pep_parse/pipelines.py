from collections import defaultdict
from pathlib import Path
import datetime as dt


BASE_DIR = Path(__file__).parent.parent
RESULTS_DIR = BASE_DIR / 'results'
FILE_DATE_FORMAT = '%Y-%m-%d_%H-%M-%S'


def CreateResultDir():
    RESULTS_DIR.mkdir(exist_ok=True)


class PepParsePipeline:
    def open_spider(self, spider):
        self.pep = defaultdict(int)

    def process_item(self, item, spider):
        self.pep[item['status']] += 1
        return item

    def close_spider(self, spider):
        total_count = 0
        for status_count in self.pep.values():
            total_count += status_count

        now = dt.datetime.now()
        now_formatted = now.strftime(FILE_DATE_FORMAT)
        file_name = f'status_summary_{now_formatted}.csv'
        file_path = RESULTS_DIR / file_name
        with open(file_path, mode='w', encoding='utf-8') as f:
            f.write('Статус,Количество\n')
            for key, value in self.pep.items():
                f.write('{0},{1}\n'.format(key, value))
            f.write(f'Total,{total_count}\n')


CreateResultDir()
