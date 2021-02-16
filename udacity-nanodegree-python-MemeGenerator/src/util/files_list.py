import os


def files_list(dir_path: str):
    '''Builds a list of file paths.
    Skips adding file paths if there is an exception.

    :param dir_path:  Top directory to traverse
    :type dir_path:  str

    :returns:  list of files
    :rtype:  list of str
    '''
    paths = []
    try:
        for root, dirs, files in os.walk(dir_path):
            for _file in files:
                paths.append(os.path.join(root, _file))
    except:
        print('console: problem with walking '+dir_path)
    return paths
