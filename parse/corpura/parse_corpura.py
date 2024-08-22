import sys
import os
import time
from sqlalchemy.exc import OperationalError

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
)

from db.models.corpus_model import Corpus
from run import db, app
from logger.logger import Logger, LogLevels

corpura_file_path = "../../src/data/corpura"


def find_and_parse_folders(file_path):
    Logger.log("Starting folder scan for Corpura Dataset...", LogLevels.INFO)

    folders = [f.path for f in os.scandir(file_path) if f.is_dir()]

    Logger.log("Starting parsing for Corpura Dataset...", LogLevels.INFO)

    with app.app_context():
        try:
            corpura_in_db = Corpus.query.all()
        except OperationalError as e:
            Logger.log(f"OperationalError occurred: {str(e)}", LogLevels.ERROR)
            db.create_all()
            corpura_in_db = []

        for folder in folders:

            corpus_name = folder.split("/")[-1].strip()
            corpus_name = folder.split("\\")[-1].strip()

            corpura_exists = any(
                db_corpus.name == corpus_name for db_corpus in corpura_in_db
            )

            if corpura_exists:
                Logger.log(
                    f"Corpus '{corpus_name}' already in database.", LogLevels.INFO
                )
            else:
                corpus_to_add = Corpus(
                    id=len(corpura_in_db) + 1,
                    name=corpus_name,
                    file_path=folder,
                    zip_file_path=folder + ".zip",
                )

                db.session.add(corpus_to_add)
                db.session.commit()
                Logger.log(
                    f"Corpus '{corpus_name}' added to the database.", LogLevels.INFO
                )

                corpura_in_db = Corpus.query.all()


if __name__ == "__main__":
    find_and_parse_folders(corpura_file_path)
