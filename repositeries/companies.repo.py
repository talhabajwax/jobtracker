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
  except Exception as e:
      return (str(e))  
  finally:
    if cursor is not None :
     cursor.close()
    if conn is not None: 
     conn.close()
    
def delete_company(companyId):
    conn = connect_db()
    cursor = conn.cursor()
    query= """update companies set isActive=0,isDeleted=1 where id in ("%s")
    """
    params=(companyId,)
    cursor.execute(query,params)
    conn.commit()
    cursor.close()
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
  except Exception as e:
      return e
  finally:
    if cursor is not None :
     cursor.close()
    if conn is not None: 
     conn.close()
    
       
def show_company(): 
  conn = None
  cursor = None    
  try:   
    conn = connect_db()
    cursor = conn.cursor()
    query= """select*from companies order by id desc
    """
    cursor.execute(query,)
    data = cursor.fetchall()
    return(data)
  except Exception as e:
      return e
  finally:
    if cursor is not None :
     cursor.close()
    if conn is not None: 
     conn.close()
    