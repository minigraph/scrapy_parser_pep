from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from pathlib import Path
import datetime as dt

BASE_DIR = Path(__file__).parent.parent
Base = declarative_base()


class Pep(Base):
    __tablename__ = 'pep'
    id = Column(Integer, primary_key=True)
    number = Column(Integer, unique=True)
    name = Column(String(300))
    status = Column(String(50))


class PepParsePipeline:
    def open_spider(self, spider):
        engine = create_engine('sqlite:///sqlite.db')
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
        self.session = Session(engine)

    def process_item(self, item, spider):
        pep = Pep(
            number=item['number'],
            name=item['name'],
            status=item['status'],
        )
        self.session.add(pep)
        self.session.commit()
        return item

    def close_spider(self, spider):
        total_count, results = 0, dict()
        peps_status = [i[0] for i in self.session.query(Pep.status).distinct()]
        for pep_status in peps_status:
            record_count = self.session.query(Pep).filter(
                Pep.status == pep_status
            ).count()
            results[pep_status] = record_count
            total_count += record_count

        results_dir = BASE_DIR / 'results'
        results_dir.mkdir(exist_ok=True)
        now = dt.datetime.now()
        now_formatted = now.strftime('%Y-%m-%d_%H-%M-%S')
        file_name = f'status_summary_{now_formatted}.csv'
        file_path = results_dir / file_name
        with open(file_path, mode='w', encoding='utf-8') as f:
            f.write('Статус,Количество\n')
            for key, value in results.items():
                f.write('{0},{1}\n'.format(key, value))
            f.write(f'Total,{total_count}\n')

        self.session.close()
