import re


def serialize_lines(query_result):
    serialized_dict = dict()
    line_dict = dict()
    query_num = 1
    for row in query_result:
        for key in row[0].__dict__:
            if key == "_sa_instance_state":
                continue
            if re.search("_time$", key) is not None:
                line_dict[key] = row[0].__dict__[key].strftime("%H:%M:%S")
            else:
                line_dict[key] = row[0].__dict__[key]
        serialized_dict[f"Line {query_num}"] = line_dict
        query_num += 1
    if len(serialized_dict) == 1:
        return line_dict
    return serialized_dict
