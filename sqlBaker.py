from lark.tree import Tree
from lark.lexer import Token
from lark import Lark
from enum import Enum, auto
import re
import copy

class SqlBaker:
    
    def __init__(self, lark_path, template_path):
        
        with open(lark_path, encoding="utf-8") as grammar:
            
            self.__lark = Lark(grammar.read())
            
        with open(template_path, encoding="utf-8") as grammar:
            
            self.__sql_template = self.__lark.parse(grammar.read())
        
    def __call__(self, param = {}):
        
        sql_template = copy.deepcopy(self.__sql_template)
        
        #ロジックコメントを処理
        sql_template.children = [
            self.__logic_comment_process(child, param)
            for child in sql_template.children
        ]
        
        #生成されたSQLを成形
        sql_template = self.__sql_normalization(sql_template)
        
        # print(self.__sql_template)
        
        sql_template = self.__remove_tail_ws(sql_template)
        
        #SQLを出力
        sql = self.__tree_parse(sql_template)
        
        #空行は削除
        sql = re.sub('\n([ \t]*\n)+', '\n', sql)
        
        return sql
    
    #ロジックコメントを評価する
    def __logic_comment_process(self, item, param):
        
        #対象がtreeである場合(treeに関してはlarkを参照)
        if type(item) == Tree:
            
            #対象が変数コメントであれば
            if item.data == LogicCommentType.VARIABLE_COMMENT.value:
                
                #変数を評価して、評価した値に置き換える
                python_code, value = item.children
                value.children[0].value=eval(python_code.value, param)
                
                #置き換え前の値がStringの場合はsingleくをーテーションを付ける
                if ValueType.as_type(value.children[0].type) in (ValueType.STRING_VALUE, ):
                    value.children[0].value = f"'{value.children[0].value}'"
                return value
            
            #対象が分岐コメントであれば
            if item.data == LogicCommentType.CONDITION_IF_BLOCK.value:
                #分岐の要素(if, elif, else)とスコープの要素をペアにして回す
                for logic_comment, conditions in zip(item.children[0::2], item.children[1::2]):
                    #分岐の要素が有効であれば
                    if self.__is_execute_scope(logic_comment, param):
                        
                        #分岐コメント自体をスコープの要素に置き換える
                        conditions.children = [
                            self.__logic_comment_process(child, param)
                            for child in conditions.children
                        ]
                        return conditions
                
                #分岐がすべて確認が終わったら(elseがなかったら)何も返さない
                return
                        
            #処理コメントでなければ
            else:
                #内側の要素を確認する
                item.children = [
                    self.__logic_comment_process(child, param)
                    for child in item.children
                ]
        
        
            #最後に中身がNoneだけor空の要素を省く
            item.children = [
                child
                for child in item.children
                if child != None and (type(child) == Token or len([item for item in child.children if item!=None]) != 0)
            ]
                
        return item
        
    #分岐の要素を評価し実行されるスコープか判定する
    def __is_execute_scope(self, logic_comment, param):
    
        #要素が条件付きの場合
        if LogicCommentType.as_type(logic_comment.data) in (LogicCommentType.IF_COMMENT, LogicCommentType.ELIF_COMMENT):
            
            #条件次第なので条件の評価を返す
            python_code = logic_comment.children[0]
            return eval(python_code.value, param)
        
        #elseの要素にたどり着いた場合
        if LogicCommentType.as_type(logic_comment.data)  in (LogicCommentType.ELSE_COMMENT, ):
            
            #実行されるスコープとする
            return True
            
        #いずれの条件も満たさない場合実行されないスコープとする
        return False
        
        
        
    #SQLを成形する
    def __sql_normalization(self, item):
        
        #対象がtreeである場合(treeに関してはlarkを参照)
        if type(item) == Tree:
            if SqlBlockType.as_type(item.data)in (SqlBlockType.WHERE_BLOCK, ):
                item.children = self.__where_block_normalization(item.children)
                print(";",item.children,";")
                if item.children == None:
                    return None
            else:
                item.children = [
                    self.__sql_normalization(child)
                    for child in item.children
                ]
            
            print(":",item.children[-1],":")
            while item.children[-1] is None or (type(item.children[-1]) == Token and item.children[-1].type == "WS"):
                item.children.pop(-1)
            
        return item
            
    def __where_block_normalization(self, children):
    
        #調整後のwhereの条件を入れるlist
        tuned_conditions_child = []
        
        #直前のWSをのぞいた要素
        prev_child = None
        
        #whereの条件を確認
        for child in children[-1].children:
        
            #対象がtokenの場合
            if type(child) == Token:
            
                #論理演算子の場合
                if child.type == "LOGICAL_OPERATOR":

                    #手前が演算子であれば登録
                    if type(prev_child)==Tree and prev_child.data == "condition":
                        tuned_conditions_child.append(child)
                        prev_child = child
                        
                    #登録の有無にかかわらず論理演算子の評価終了
                    continue
                    
                #論理演算子でないtokenは確認せずに登録
                else:
                    tuned_conditions_child.append(child)
                    
            #対象がtokenでない場合(treeの場合)
            else:
                tuned_conditions_child.append(child)
                prev_child = child
                
        #成形後に最後の要素が論理演算子になっている場合
        if type(prev_child) == Token and prev_child.type == "LOGICAL_OPERATOR":
            #最後の論理演算子を確認し
            for i in range(len(tuned_conditions_child)-1,-1,-1):
                if type(tuned_conditions_child[i])==Token and tuned_conditions_child[i].type == "LOGICAL_OPERATOR":
                    #最後の論理演算子以降の要素を切り取る
                    tuned_conditions_child = tuned_conditions_child[:i]
                    break
        
        #成形後の条件部分が存在しなければ
        if len([child for child in tuned_conditions_child if type(child)==Tree or child.type!="WS"])==0:
            children = None
        else:
            children[-1].children = tuned_conditions_child
            
        return children
        
        
    def __remove_tail_ws(self, item):
        
        if type(item) == Tree:
            
            while type(item.children[-1]) == Token and item.children[-1].type == "WS":
                item.children.pop(-1)
            
            print(":",item.children[-1],":")
            item.children = [
                self.__remove_tail_ws(child)
                for child in item.children
            ]
        
        return item
        
    def __tree_parse(self, tree):
        # print(tree.data)
        # print(tree)
        
        sql = ""
        
        for item in tree.children:
            # print(type(item))
            if type(item) == Token:
                sql += self.__token_parse(item)
            elif type(item) == Tree:
                sql += self.__tree_parse(item)
        
        return sql
                
    def __token_parse(self, token):
        # print(dir(token))
        # print(token.title)
        # print(token.value)
        return str(token.value)
    
    def get_sql_template(self):
        return self.__sql_template
        
class LogicCommentType(Enum):
    VARIABLE_COMMENT = "variable_comment"
    CONDITION_IF_BLOCK = "condition_if_block"
    IF_COMMENT = "if_comment"
    ELIF_COMMENT = "elif_comment"
    ELSE_COMMENT = "else_comment"
    END_COMMENT = "end_comment"
    
    def as_type(text):
        
        for item in LogicCommentType:
            if text == item.value:return item
        
        return None
    
class ValueType(Enum):
    INT_VALUE = "INT_VALUE"
    FLOAT_VALUE = "FLOAT_VALUE"
    STRING_VALUE = "STRING_VALUE"
    
    def as_type(text):
    
        for item in ValueType:
            if text == item.value:return item
        
        return None

class SqlBlockType(Enum):
    SELECT_BLOCK = "select_block"
    FROM_BLOCK = "from_block"
    WHERE_BLOCK = "where_block"
    
    def as_type(text):
    
        for item in SqlBlockType:
            if text == item.value:return item
        
        return None