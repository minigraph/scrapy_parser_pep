from pathlib import Path
import datetime as dt

BASE_DIR = Path(__file__).parent.parent


class PepParsePipeline:
    def open_spider(self, spider):
        self.pep = dict()

    def process_item(self, item, spider):
        status = item['status']
        if status in self.pep.keys():
            self.pep[status] += 1
        else:
            self.pep[status] = 1
        return item

    def close_spider(self, spider):
        total_count = 0
        for status_count in self.pep.values():
            total_count += status_count

        results_dir = BASE_DIR / 'results'
        results_dir.mkdir(exist_ok=True)
        now = dt.datetime.now()
        now_formatted = now.strftime('%Y-%m-%d_%H-%M-%S')
        file_name = f'status_summary_{now_formatted}.csv'
        file_path = results_dir / file_name
        with open(file_path, mode='w', encoding='utf-8') as f:
            f.write('Статус,Количество\n')
            for key, value in self.pep.items():
                f.write('{0},{1}\n'.format(key, value))
            f.write(f'Total,{total_count}\n')

        self.session.close()
