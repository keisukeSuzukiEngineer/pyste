select 
    * 
from 
    sample
where 
    /*%if name != None */
    sample.name = /* name */'太郎'
    /*%end*/
and
    /*%if age != None */
    sample.age = /* age */10
    /*%end*/
and
    /*%if gender != None */
    sample.gender = /* gender */'man'
    /*%end*/