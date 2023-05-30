# !/usr/bin/python
from os.path    \
    import      \
        join,   \
        isdir,  \
        isfile, \
        abspath

from os     \
    import  \
    walk,   \
    rename

from pathlib \
    import Path

is_debugging: bool = False


def main():
    file_path_to_script = Path(__file__)

    directory_to_library = abspath(
        file_path_to_script.parent
    )

    directory_to_dataset = join(
        directory_to_library,
        'dataset'
    )

    rename_wrong_file_format(
        directory_to_dataset
    )


def debug_found(
        found: str
):
    global is_debugging
    if is_debugging:
        print(
            'file: ',
            found
        )


def is_jpeg(file_name: str) -> bool:
    splitted: list = file_name.split('.')

    length_of_array = len(splitted)
    last_position = length_of_array - 1

    if str(splitted[last_position]).lower() == 'jpeg':
        return True

    return False


def rename_wrong_file_format(
        dataset_location: str
):
    print()

    for \
        root, \
        dirs, \
        files \
            in walk(
                dataset_location,
                topdown=False
            ):
        for file in files:
            filename = file

            location_to_file = join(
                root,
                filename
            )

            if is_jpeg(filename):
                previous_filename = filename
                new_filename = replace_extension_with_jpg(filename)

                rename_file(
                    join(root, previous_filename),
                    join(root, new_filename)
                )

            debug_found(
                location_to_file
            )


def replace_extension_with_jpg(file_name: str) -> str:
    return_value: str = ''

    tokens = file_name.split('.')

    count_of_tokens = len(tokens)
    location_of_extension = count_of_tokens - 1

    tokens[location_of_extension] = 'jpg'

    for index in range(len(tokens)):
        current_token: str = tokens[index]

        if index == 0:
            return_value = return_value + current_token
        else:
            return_value = return_value + '.' + current_token

    return return_value


def rename_file(
        source: str,
        destination: str
) -> bool:
    if isfile(source):
        try:
            rename(source, destination)
            return True

        except OSError as error:
            print(error)

    return False


if __name__ == '__main__':
    main()
