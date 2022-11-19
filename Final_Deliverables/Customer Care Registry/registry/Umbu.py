import ibm_db
conn = ibm_db.connect('DATABASE=bludb;HOSTNAME=2f3279a5-73d1-4859-88f0-a6c3e6b4b907.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud;PORT=30756;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=tdn81266;PWD=7LY8okjAouJf3LoO', '', '')
#var="select * from agent"
var="show COLUMNS from agent"
var1=ibm_db.exec_immediate(conn,var)
result=ibm_db.fetch_both(var1)
for i in result:
    print(i,end=" ")
print(result)

#print(ibm_db.execute(var))