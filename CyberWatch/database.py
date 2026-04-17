import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="toledinho06",
        database="cyberwatch",
        port = 3306
    )
def get_logs():
    conm = get_connection()
    cursor = conm.cursor(dictionary=True)

    cursor.execute("SELECT * FROM logs ORDER BY event_time DESC")
    rows = cursor.fetchall()
    
    cursor.close()
    conm.close()

    return rows
def insert_alerts(alert_time, host_name, user_name, rule_name, severity, description, source_ip):
    conm = get_connection()
    cursor = conm.cursor()

    query = """
        INSERT INTO alerts
        (alert_time, host_name, user_name, rule_name, severity, description, source_ip)
        values
        (%s, %s, %s, %s, %s, %s, %s)
        """

    values = (
        alert_time,
        host_name,
        user_name,
        rule_name,
        severity,
        description,
        source_ip
    )
    cursor.execute(query, values)
    conm.commit()
    
    cursor.close()
    conm.close()
def get_alerts():
    conm = get_connection()
    cursor = conm.cursor(dictionary=True)

    cursor.execute("SELECT * FROM alerts ORDER BY alert_time DESC")
    rows = cursor.fetchall()

    cursor.close()
    conm.close()

    return rows
def clear_alerts():
    conm = get_connection()
    cursor = conm.cursor()

    cursor.execute("DELETE FROM alerts")
    conm.commit()

    cursor.close()
    conm.close()