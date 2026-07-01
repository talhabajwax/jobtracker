from database import connect_db


def save_company(name,website,location):
  conn = None
  cursor = None
  try:
    conn = connect_db()
    cursor = conn.cursor()
    query ='''INSERT INTO companies (name, website,location)
    VALUES (%s, %s,%s) '''
    params=(name, website,location)
    cursor.execute(query,params)
    conn.commit()
    new_company_id=cursor.lastrowid
    return(new_company_id)
  
  finally:
    if cursor is not None :
     cursor.close()
    if conn is not None: 
     conn.close()
    
def delete_company(companyId,user_id):
  conn=None
  cursor=None
  try:
    conn = connect_db()
    cursor = conn.cursor()
    query= """update companies set isActive=0,isDeleted=1 where id = %s and user_id=%s
    """
    params=(companyId,user_id)
    cursor.execute(query,params)
    conn.commit()
    affected_rows=cursor.rowcount
    return(affected_rows)
  finally:
    if cursor is not None :
     cursor.close()
    if conn is not None: 
     conn.close()
    
def update_company(companyName,companyLocation,companySite,companyId):
  conn = None
  cursor = None
  try:
    conn = connect_db()
    cursor = conn.cursor()
    query= """update companies set name=(%s),location=(%s),website=(%s) where id = (%s)
    """
    params=(companyName,companyLocation,companySite,companyId)
    cursor.execute(query,params)
    conn.commit()
    affected_rows=cursor.rowcount
    return(affected_rows)
 
  finally:
    if cursor is not None :
     cursor.close()
    if conn is not None: 
     conn.close()
    
       
def show_company(user_id): 
  conn = None
  cursor = None    
  try:   
    conn = connect_db()
    cursor = conn.cursor()
    query= """select c.name from applications a
    join companies c on c.id=a.company_id
    where a.user_id= %s
    """
    params=(user_id,)
    cursor.execute(query,params)
    data = cursor.fetchall()
    return(data)
 
  finally:
    if cursor is not None :
     cursor.close()
    if conn is not None: 
     conn.close()
    