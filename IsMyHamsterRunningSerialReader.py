import serial
import sqlite3
import datetime



def openSerial(port):
    ser = serial.Serial()
    ser.baudrate = 9600
    ser.port = 'COM6'
    ser.timeout = 60

    ser.open()
    return ser

def createConnection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def dothis(out):
    now = datetime.datetime.now()
    out = int(out)
    print(str(out) + " " + str(now))
    c.execute('INSERT INTO "Spins" VALUES (?,?)',(out,now))
    conn.commit()


if __name__ == '__main__':
    ser = openSerial('COM6')
    db = 'IsMyHamsterRunning.db'

    conn = createConnection(db)
    c = conn.cursor()

    
    
    while True:
        out = ser.readline().strip().decode('utf-8')
        if out == 'Start' or out == '': continue
        
        try:
            dothis(out)
        except Exception as e:
            print(e)
            f = open('errorlog.txt','a')
            f.write('\n%s'%e)
            f.close()
            
                
        
        
