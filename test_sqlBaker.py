import pytest

from sqlBaker import SqlBaker




# @pytest.fixture(scope="module", autouse=True)
# def sql_template_lark():
    
    # path = "./lark/sqlTemplate.lark"
    
    # with open(path, encoding="utf-8") as grammar:
        
        # sql_template_lark = Lark(grammar.read())
        
        # yield sql_template_lark

@pytest.fixture(scope="module", autouse=True)
def sql_template_lark_path():
    
    path = "./lark/sqlTemplate.lark"
    
    yield path

def test_normal_sample01_01(sql_template_lark_path):

    file_path = "./templateSamples/normalSql/sample01.sql"
    param = {}
    result = "\n".join([
        "SELECT",
        "	name,",
        "	name n,",
        "	name AS n,",
        "	sample_table.name,",
        "	sample_table.name q,",
        "	sample_table.name AS q,",
        "	'ww',",
        "	'ww' w,",
        "	'ww' AS w,",
        "	sample_table_a.*",
        "FROM",
        "	sample_table",
        "JOIN",
        "	sample_table_a",
        "ON ",
        "	sample_table.a = sample_table_a.a",
        "INNER JOIN",
        "	sample_table_b",
        "ON ",
        "	sample_table.b = sample_table_b.b",
        "RIGHT JOIN",
        "	sample_table_c",
        "ON ",
        "	sample_table.c = sample_table_c.c",
        "RIGHT OUTER JOIN",
        "	sample_table_d",
        "ON ",
        "	sample_table.d = sample_table_d.d",
        "LEFT JOIN",
        "	sample_table_e",
        "ON ",
        "	sample_table.e = sample_table_e.e",
        "LEFT OUTER JOIN",
        "	sample_table_f",
        "ON ",
        "	sample_table.f = sample_table_f.f",
        "OUTER JOIN",
        "	sample_table_g",
        "ON ",
        "	sample_table.g = sample_table_g.g",
        "FULL OUTER JOIN",
        "	sample_table_h",
        "ON ",
        "	sample_table.h = sample_table_h.h",
        "CROSS JOIN",
        "	sample_table_i",
        "ON ",
        "	sample_table.i = sample_table_i.i",
        "WHERE",
        "	sample_table.name IN ('name', 'namae')",
        "AND",
        "	sample_table.gender = 'mae'",
        "AND",
        "	sample_table.age > 20",
        "OR",
        "	sample_table.age >= 20",
        "OR",
        "	sample_table.age = 20",
        "OR",
        "	sample_table.age <= 20",
        "OR",
        "	sample_table.age < 20",
    ])
    
    sql_baker = SqlBaker(sql_template_lark_path, file_path)
    bake_sql = sql_baker(param)
    
    assert bake_sql == result

def test_normal_sample02_01(sql_template_lark_path):

    file_path = "./templateSamples/normalSql/sample02.sql"
    param = {}
    result = "\n".join([
        "select",
        "	name,",
        "	name n,",
        "	name as n,",
        "	sample_table.name,",
        "	sample_table.name q,",
        "	sample_table.name as q,",
        "	'ww',",
        "	'ww' w,",
        "	'ww' as w,",
        "	sample_table_a.*",
        "from",
        "	sample_table",
        "join",
        "	sample_table_a",
        "on ",
        "	sample_table.a = sample_table_a.a",
        "inner join",
        "	sample_table_b",
        "on ",
        "	sample_table.b = sample_table_b.b",
        "right join",
        "	sample_table_c",
        "on ",
        "	sample_table.c = sample_table_c.c",
        "right outer join",
        "	sample_table_d",
        "on ",
        "	sample_table.d = sample_table_d.d",
        "left join",
        "	sample_table_e",
        "on ",
        "	sample_table.e = sample_table_e.e",
        "left outer join",
        "	sample_table_f",
        "on ",
        "	sample_table.f = sample_table_f.f",
        "outer join",
        "	sample_table_g",
        "on ",
        "	sample_table.g = sample_table_g.g",
        "full outer join",
        "	sample_table_h",
        "on ",
        "	sample_table.h = sample_table_h.h",
        "cross join",
        "	sample_table_i",
        "on ",
        "	sample_table.i = sample_table_i.i",
        "where",
        "	sample_table.name in ('name', 'namae')",
        "and",
        "	sample_table.gender = 'mae'",
        "and",
        "	sample_table.age > 20",
        "or",
        "	sample_table.age >= 20",
        "or",
        "	sample_table.age = 20",
        "or",
        "	sample_table.age <= 20",
        "or",
        "	sample_table.age < 20",
    ])
    
    sql_baker = SqlBaker(sql_template_lark_path, file_path)
    bake_sql = sql_baker(param)
    
    assert bake_sql == result

def test_normal_sample03_01(sql_template_lark_path):

    file_path = "./templateSamples/normalSql/sample03.sql"
    param = {}
    result = "\n".join([
        "select",
        "	*",
        "from ",
        "	human",
    ])
    
    sql_baker = SqlBaker(sql_template_lark_path, file_path)
    bake_sql = sql_baker(param)
    
    assert bake_sql == result


def test_template_sample01_01(sql_template_lark_path):

    file_path = "./templateSamples/templateSql/sample01.sql"
    param = {
        'age':0,
        'type':"MAN_ONRY"
    }
    result = "\n".join([
        "select ",
        "    * ",
        "from ",
        "    sample",
        "where ",
        "    sample.name = '太郎'",
        "and",
        "    sample.age = '0'",
        "and",
        "    sample.gender = 'man'",
    ])
    
    sql_baker = SqlBaker(sql_template_lark_path, file_path)
    bake_sql = sql_baker(param)
    
    assert bake_sql == result


def test_template_sample01_02(sql_template_lark_path):

    file_path = "./templateSamples/templateSql/sample01.sql"
    param = {
        'age':None,
        'type':"WOMA_ONRY"
    }
    result = "\n".join([
        "select ",
        "    * ",
        "from ",
        "    sample",
        "where ",
        "    sample.name = '太郎'",
        "and",
        "    sample.gender = 'woman'",
    ])
    
    sql_baker = SqlBaker(sql_template_lark_path, file_path)
    bake_sql = sql_baker(param)
    
    assert bake_sql == result


def test_template_sample01_03(sql_template_lark_path):

    file_path = "./templateSamples/templateSql/sample01.sql"
    param = {
        'age':None,
        'type':"FREE"
    }
    result = "\n".join([
        "select ",
        "    * ",
        "from ",
        "    sample",
        "where ",
        "    sample.name = '太郎'",
        "and",
        "    sample.gender in ( 'man', 'woman' )",
    ])
    
    sql_baker = SqlBaker(sql_template_lark_path, file_path)
    bake_sql = sql_baker(param)
    
    assert bake_sql == result



def test_template_sample01_04(sql_template_lark_path):

    file_path = "./templateSamples/templateSql/sample01.sql"
    param = {
        'age':None,
        'type':"wwww"
    }
    result = "\n".join([
        "select ",
        "    * ",
        "from ",
        "    sample",
        "where ",
        "    sample.name = '太郎'",
        "and",
        "    sample.gender = 'unknown'",
    ])
    
    sql_baker = SqlBaker(sql_template_lark_path, file_path)
    bake_sql = sql_baker(param)
    
    assert bake_sql == result


def test_template_sample02_01(sql_template_lark_path):

    file_path = "./templateSamples/templateSql/sample02.sql"
    param = {
        'name':"太郎",
        'age':5,
        'gender':"??"
    }
    result = "\n".join([
        "select ",
        "    * ",
        "from ",
        "    sample",
        "where ",
        "    sample.name = '太郎'",
        "and",
        "    sample.age = 5",
        "and",
        "    sample.gender = '??'",
    ])
    
    sql_baker = SqlBaker(sql_template_lark_path, file_path)
    bake_sql = sql_baker(param)
    
    assert bake_sql == result


def test_template_sample02_02(sql_template_lark_path):

    file_path = "./templateSamples/templateSql/sample02.sql"
    param = {
        'name':None,
        'age':5,
        'gender':"??"
    }
    result = "\n".join([
        "select ",
        "    * ",
        "from ",
        "    sample",
        "where ",
        "    sample.age = 5",
        "and",
        "    sample.gender = '??'",
    ])
    
    sql_baker = SqlBaker(sql_template_lark_path, file_path)
    bake_sql = sql_baker(param)
    
    assert bake_sql == result


def test_template_sample02_03(sql_template_lark_path):

    file_path = "./templateSamples/templateSql/sample02.sql"
    param = {
        'name':"次郎",
        'age':5,
        'gender':None
    }
    result = "\n".join([
        "select ",
        "    * ",
        "from ",
        "    sample",
        "where ",
        "    sample.name = '次郎'",
        "and",
        "    sample.age = 5",
    ])
    
    sql_baker = SqlBaker(sql_template_lark_path, file_path)
    bake_sql = sql_baker(param)
    
    print(bake_sql)
    
    assert bake_sql == result

def test_template_sample02_04(sql_template_lark_path):

    file_path = "./templateSamples/templateSql/sample02.sql"
    param = {
        'name':None,
        'age':None,
        'gender':None
    }
    result = "\n".join([
        "select ",
        "    * ",
        "from ",
        "    sample",
    ])
    
    sql_baker = SqlBaker(sql_template_lark_path, file_path)
    bake_sql = sql_baker(param)
    
    print("--")
    print(bake_sql)
    print("--")
    
    assert bake_sql == result

