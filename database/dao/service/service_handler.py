from Common.time_utils import get_now
from database.db_connection import execute

service_table_name = 'service'


def get_all_first_level_service():
    sql_text = "SELECT id, name FROM {} WHERE level = 1 ORDER BY name".format(service_table_name)

    return execute(sql_text)


def get_all_second_level_service():
    sql_text = '''SELECT
                      one.id   AS father_id,
                      one.name AS father_name,
                      two.id,
                      two.name,
                      two.attribute,
                      two.attributeState
                    FROM service one, service two
                    WHERE two.father = one.id
                      AND two.level = 2
                    ORDER BY one.name, two.name'''

    execute(sql_text)


def add_first_level_service(service_name):
    time_now = get_now()
    sql_text = '''INSERT INTO {}(name, createdTime, father, level) VALUES('{}','{}',{},{})''' \
        .format(service_table_name, service_name, time_now, -1, 1)

    return execute(sql_text)


def add_second_level_service(service_name, father_id, attribute, attribute_state):
    time_now = get_now()
    sql_text = '''INSERT INTO {}(name, createdTime, father, level, attribute, attributeState) 
                VALUES('{}','{}',{},{},'{}', '{}')''' \
        .format(service_table_name, service_name, time_now, father_id, 2, attribute, attribute_state)

    return execute(sql_text)


def update_service(service_id, service_name, father_id=-1, attribute='', attribute_state=''):
    if father_id == -1:
        sql_text = '''UPDATE {} SET name = '{}' where id = {}'''.format(service_table_name, service_name, service_id)

    else:
        sql_text = '''UPDATE {} SET name = '{}', attribute = '{}', attributeState = '{}' where id = {}''' \
            .format(service_table_name, service_name, attribute, attribute_state, service_id)

    execute(sql_text)


def delete_service(service_id):
    sql_text = '''DELETE FROM {} where id = {}'''.format(service_table_name, service_id)

    execute(sql_text)


def get_second_service_by_father(father_id):
    sql_text = '''SELECT
                      one.id   AS father_id,
                      one.name AS father_name,
                      two.id,
                      two.name,
                      two.attribute,
                      two.attributeState
                    FROM service one, service two
                    WHERE two.father = one.id
                      AND one.id = {}
                      AND two.level = 2
                    ORDER BY one.name, two.name''' \
        .format(father_id)
    return execute(sql_text)


def get_second_service_count_by_father(father_id):
    if father_id == -1:
        return 0

    sql_text = '''select count(1) from {} where father_id = {}'''.format(service_table_name, father_id)
    count = execute(sql_text)

    return count