import web

db_host = 'mcldisu5ppkm29wf.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
db_name = 'zqz28iwm6adqc0es'
db_user = 'jozn5gylwfg2ss58'
db_pw = 'sl8xe3cgxtfot631'

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )