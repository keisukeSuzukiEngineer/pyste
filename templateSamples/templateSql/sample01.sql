select 
    * 
from 
    sample
where 
    sample.name = '太郎'
and
    /*%if age != None */
    sample.age = /* age */'10'
    /*%end*/
and
    /*%if type == "MAN_ONRY" */
    sample.gender = 'man'
    /*%elif type == "WOMA_ONRY"*/
    sample.gender = 'woman'
    /*%elif type == "FREE"*/
    sample.gender in ( 'man', 'woman' )
    /*%else*/
    sample.gender = 'unknown'
    /*%end*/