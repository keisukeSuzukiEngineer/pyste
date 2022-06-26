import pytest
from templateHolder import get_templates

template_base_path = "./templateSamples"


@pytest.fixture(scope="module", autouse=True)
def sql_holder():
    
    sql_holder = get_templates(template_base_path)
    
    yield sql_holder


def test_singleton(sql_holder):
    
    sql_holder2 = get_templates(template_base_path)
    
    assert sql_holder is sql_holder2
    

def test_has_dir(sql_holder):
    assert "normalSql" in dir(sql_holder)
    assert "templateSql" in dir(sql_holder)

def test_has_template(sql_holder):
    assert "sample01" in dir(sql_holder.normalSql)
    assert "sample02" in dir(sql_holder.normalSql)
    assert "sample03" in dir(sql_holder.normalSql)
    
    assert "sample01" in dir(sql_holder.templateSql)
    assert "sample02" in dir(sql_holder.templateSql)
    
def test_bake(sql_holder):
    
    param = {}
    result = "\n".join([
        "select",
        "	*",
        "from ",
        "	human",
    ])
    
    sql = sql_holder.normalSql.sample03(param)
    
    assert sql == result