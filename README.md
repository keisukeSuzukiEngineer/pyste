# pyste
pythonのSQLテンプレートエンジン

# 初めに
これはdomaの記法をリスペクトしたSQLテンプレートエンジンです。
ORマッパーではないのでDBアクセスの機能は含まれていません。

# 使用方法

## インストール
pipでインストールできるように準備中

## SQLファイルの準備
詳細はgit上のフォルダ **/templateSamples** を参照

- 任意のフォルダを決める
- 任意のフォルダ内にSQLファイルを配置
  - 任意のフォルダ内にフォルダを作りSQLファイルを分けてもよい
 
## SQLのテンプレート化

### 今後対応予定な文法
使用可能な構文の具体例は **/templateSamples/normalSql** を参照
以下の構文は今後対応予定
- サブクエリ
- with
- group by
- having
- order by
- offset
- limit
- ダブルクウォーテーションで囲ったカラム名
- ()での条件の優先付け

### 変数埋め込みコメント
`table.column = /* python code */'str'`  
`table.column = /* python code */10`  
SQL文の値の前に、`/*`と`*/`で囲んだpythonのコードを書くことで、そのコードの実行結果で値を置き換えることができる


### 条件分岐コメント
`/*%if python code */`  
`/*%elif python code */`  
`/*%else*/`  
`/*%end*/`  
where句内での使用を想定している。  
SQL文をの一部を囲うことで、囲ったSQL文の一部を使用するかpythonのコードの実行結果で指定できる。
elifとelseはなくてもよく、elifはいくつあっても問題ない。

### 実装予定のコメント
以下の構文は今後追加予定
- 繰り返しコメント
- 置き換えコメント


## SQLの成形
SQLをテンプレートとして処理した結果正しくないSQLになる可能性があるので、一部の文法はテンプレート処理後に成形を行う。  
**before**

    where  
	    //ここに来る条件がif文で削除された想定
    and  
	    table.clolumn = 10  
    and  
	    //ここに来る条件がif文で削除された想定
      
**after**  

    where  
    //手前に条件式がない論理演算論理演算子は削除  
      table.clolumn = 10  
    //後続に条件式がない論理演算論理演算子は削除  


# プログラムからSQLを読み込み
    from templateHolder import get_templates
    
    sql_holder = get_templates({配下にSQLのテンプレートを配置した任意のフォルダのパス})
