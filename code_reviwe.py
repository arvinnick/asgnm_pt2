############
#
# Code Review
#
# Please do a code review for the following snippet.
# Add your review suggestions inline as python comments
#
############
from typing import Optional, Any


def get_value(data, key, default,  # __modification__ added type hints
              lookup: Optional = None,  # __modification__ added type hints
              mapper: Optional[callable] = None) -> Any:  # __modification__ added type hints
    """
    Finds the value from data associated with key, or default if the key isn't present.
    If a lookup enum is provided, this value is then transformed to its enum value.
    If a mapper function is provided, this value is then transformed by applying mapper to it.
    """
    return_value = data.get(key)  # __modification__ used get method to avoid KeyError
    if not return_value:  # __modification__ "" and None are evaluated as false when in a condition
        return_value = default
    if lookup:
        return_value = lookup.get(return_value, return_value)  # __modification__ used get method to avoid KeyError
    if mapper:
        return_value = mapper(return_value)
    return return_value


def ftp_file_prefix(namespace: str) -> str:  # __modification__ added type hints
    """
    Given a namespace string with dot-separated tokens, returns the string with the final token replaced by 'ftp'.
    Example: a.b.c => a.b.ftp
    """

    last_dot_index = namespace.rfind('.')  # __modification__ readability improvement
    if last_dot_index == -1:  # __modification__ Handle no dot found scenario or raise an exception if it's
        #                                        inappropriate to return 'ftp'
        return 'ftp'
    base_string = namespace[:last_dot_index]  # __modification__ readability improvement
    return '{}.ftp'.format(base_string)  # __modification__ performance improvement using format instead of splitting
    #                                                       and re joining the string


def string_to_bool(boolean_string: str) -> bool:  # __modification__ added type hints, used "boolean_string" instead of
    #                                                                instead of "string" to avoid confusion
    """
    Returns True if the given string is 'true' case-insensitive, False if it is 'false' case-insensitive.
    Raises ValueError for any other input.
    """
    if boolean_string.lower() == 'true':
        return True
    elif boolean_string.lower() == 'false':  # __modification__ used elif instead of if
        return False
    else:  # __modification__ used else to be consistent with the documentation
        raise ValueError(f'String {boolean_string} is neither true nor false')


def config_from_dict(conf_dict: dict) -> tuple:  # __modification__ added type hints, renamed the argument to avoid
    #                                                              the conflict with the builtin type "dict"
    """
    Given a dict representing a row from a namespaces csv file, returns a DAG configuration as a pair whose first
    element is the DAG name and whose second element is a dict describing the DAG's properties
    """
    namespace = conf_dict['Namespace']
    return (conf_dict['Airflow DAG'],
            {"earliest_available_delta_days": 0,
             "lif_encoding": 'json',
             "earliest_available_time":
                 get_value(conf_dict, 'Available Start Time', '07:00'),
             "latest_available_time":
                 get_value(conf_dict, 'Available End Time', '08:00'),
             "require_schema_match":
                 get_value(conf_dict, 'Requires Schema Match', 'True',
                           mapper=string_to_bool),
             "schedule_interval":
                 get_value(conf_dict, 'Schedule', '1 7 * * * '),
             "delta_days":
                 get_value(conf_dict, 'Delta Days', 'DAY_BEFORE',
                           lookup=conf_dict.get("Delta Days")),  # __modification__ DeltaDays is not defined, and it
             # is not a DAG property as well. Thus, I assume that the developer means to find a value in cell of the
             # row. But this code review will require clarification for sure.
             "ftp_file_wildcard":
                 get_value(conf_dict, 'File Naming Pattern', None),
             "ftp_file_prefix":
                 get_value(conf_dict, 'FTP File Prefix',
                           ftp_file_prefix(namespace)),
             "namespace": namespace
             }
            )
