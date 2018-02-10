import sys
import os

from elasticsearch import Elasticsearch


def get_files_list(path='./data', extension='.txt'):
    """
    Returns list of files with a given extension

    :param path:
    :param extension:

    :returns List of relative file_names
    """
    directory = os.scandir(path)
    files_list = []
    for dirc in directory:
        if dirc.is_file():
            lala, extension1 = os.path.splitext(dirc.name)
            if extension1 == extension:
                files_list.append(dirc.name)
    return files_list


if __name__ == "__main__":
    directory = get_files_list()
    import pdb; pdb.set_trace()
    es = Elasticsearch(host='localhost', port=9200)
