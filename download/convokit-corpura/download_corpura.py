import convokit
import os
import sys
import threading
import concurrent.futures
import multiprocessing

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
)

from logger.logger import Logger, LogLevels


def download_convokit_corpus(link, save_dir):
    try:
        # Ensure the save directory exists
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        # Download the corpus
        corpus = convokit.download(link, data_dir=save_dir)

        Logger.log(
            f"Downloaded and saved corpus '{link}' to '{save_dir}'", LogLevels.DEBUG
        )

    except Exception as e:
        Logger.log(f"Failed to download corpus '{link}': {e}", LogLevels.DEBUG)


def download_multiple_convokit_corpura(links, save_dir):
    num_cores = multiprocessing.cpu_count() * 2

    with concurrent.futures.ThreadPoolExecutor(max_workers=num_cores) as executor:
        futures = [
            executor.submit(download_convokit_corpus, link, save_dir) for link in links
        ]

        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                Logger.log(f"An error occurred: {e}", LogLevels.ERROR)


if __name__ == "__main__":
    corpus_links = [
        "conversations-gone-awry-corpus",
        "conversations-gone-awry-cmv-corpus",
        "movie-corpus",
        "parliament-corpus",
        "supreme-corpus",
        "wiki-corpus",
        "tennis-corpus",
        "reddit-corpus-small",
        "chromium-corpus",
        "winning-args-corpus",
        "reddit-coarse-discourse-corpus",
        "persuasionforgood-corpus",
        "iq2-corpus",
        "friends-corpus",
        "switchboard-corpus",
        "wikipedia-politeness-corpus",
        "stack-exchange-politeness-corpus",
        "diplomacy-corpus",
        "gap-corpus",
        "wiki-articles-for-deletion-corpus",
        "casino-corpus",
        "spolin-corpus",
    ]
    save_directory = "../../src/data/corpura"

    download_multiple_convokit_corpura(corpus_links, save_directory)
