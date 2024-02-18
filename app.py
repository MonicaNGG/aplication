from flask import Flask, render_template, request, redirect
#from flask_mysqldb import MySQL
from .utilidades import Conexion

app = Flask(__name__)

# VARIABLES DE CONEXION
SERVER = 'localhost'
USER = 'MonicaG'
PASSWORD = '1234'
DB = 'nomina'


@app.route('/')
def index():
    data = {}
    cx = Conexion(SERVER, USER, PASSWORD, DB)
    sql = '''
    SELECT idEmpleado,
        Empleados.NombreEmpleado AS Nombre,
        Empleados.DocumentoEmpleado AS Documento, 
        Empleados.CuentaEmpleado AS cuenta,
        Empleados.IngresoEmpleado AS fingreso,
        Empleados.RetiroEmpleado AS fretiro, 
        Areas.NombreArea AS area, 
        Cargos.NombreCargo As cargo 
        FROM Empleados
        INNER JOIN Cargos ON Cargos.idCargo = Empleados.Cargos_idCargos
        INNER JOIN Areas ON Areas.idArea = Empleados.Areas_idAreas
    '''
    empleados = cx.consulta_sp(sql).fetchall()
    cx.cerrar_conexion()

    data['empleados'] = empleados
    return render_template('index.html',data = data)

@app.route('/addempleado', methods = ['GET','POST'])
def addempleado():
    data = {}
    cx = Conexion(SERVER, USER, PASSWORD, DB)
    sql = "SELECT * FROM Areas"
    Areas = cx.consulta_sp(sql).fetchall()
    data['Areas'] = Areas

    sql = "SELECT * FROM Cargos"
    Cargos = cx.consulta_sp(sql).fetchall()    
    data['Cargos'] = Cargos 

    cx.cerrar_conexion()
    
    if request.method == 'POST':
        nombre = request.form['nombre']
        documento = request.form['documento']
        cuenta = request.form['cuenta']
        area = request.form['area']
        cargo = request.form['cargo']
        fingreso = request.form['fingreso']

        fretiro = request.form['fretiro']

        if fretiro == '':
            fretiro = None

        cx = Conexion(SERVER, USER, PASSWORD, DB)

        sql = "INSERT INTO Empleados (NombreEmpleado, DocumentoEmpleado, CuentaEmpleado,Areas_idAreas,Cargos_idCargos, IngresoEmpleado,RetiroEmpleado) VALUES (%s,%s,%s,%s,%s,%s,%s)"

        tupla = (nombre,documento,cuenta,area,cargo,fingreso,fretiro)

        cx.consulta_cp(sql,tupla)
        cx.commit()

        cx.cerrar_conexion()

    return render_template('addempleado.html',data = data)



@app.route('/editempleado/<idEmpleado>',methods = ['GET','POST'])
def editempleado(idEmpleado):
    data = {}
    cx = Conexion(SERVER, USER, PASSWORD, DB)

    sql = "SELECT Empleados.idEmpleado AS idEmpleado, Empleados.NombreEmpleado AS Nombre, Empleados.DocumentoEmpleado AS Documento, Empleados.CuentaEmpleado AS cuenta,Empleados.IngresoEmpleado AS fingreso, Empleados.RetiroEmpleado AS fretiro, Empleados.Areas_idAreas AS area, Empleados.Cargos_idCargos As cargo FROM Empleados WHERE idEmpleado = %s"
    tupla = (idEmpleado,)
    empleado = cx.consulta_cp(sql,tupla).fetchone()
    data['empleado'] = empleado

    sql = "SELECT * FROM Areas"
    Areas = cx.consulta_sp(sql).fetchall()
    data['Areas'] = Areas

    sql = "SELECT * FROM Cargos"
    Cargos = cx.consulta_sp(sql).fetchall()    
    data['Cargos'] = Cargos 
    cx.cerrar_conexion()

    if request.method == 'POST':
        nombre = request.form['nombre']
        documento = request.form['documento']
        cuenta = request.form['cuenta']
        area = request.form['area']
        cargo = request.form['cargo']
        fingreso = request.form['fingreso']

        fretiro = request.form['fretiro']

        if fretiro == '':
            fretiro = None

        cx = Conexion(SERVER, USER, PASSWORD, DB)

        sql = "UPDATE Empleados SET NombreEmpleado = %s, DocumentoEmpleado = %s, CuentaEmpleado = %s,Areas_idAreas = %s,Cargos_idCargos = %s, IngresoEmpleado = %s,RetiroEmpleado = %s WHERE idEmpleado = %s"

        tupla = (nombre,documento,cuenta,area,cargo,fingreso,fretiro,idEmpleado)

        cx.consulta_cp(sql,tupla)
        cx.commit()

        cx.cerrar_conexion()

    return render_template('editempleado.html', data = data)

@app.route('/editsalario/<idEmpleado>',methods = ['GET','POST'])
def editsalario(idEmpleado):
    data = {}
    cx = Conexion(SERVER, USER, PASSWORD, DB)

    sql = "SELECT idEmpleado, NombreEmpleado AS Nombre FROM Empleados WHERE idEmpleado = %s"
    tupla = (idEmpleado,)
    empleado = cx.consulta_cp(sql,tupla).fetchone()
    data['empleado'] = empleado

    sql = '''
            SELECT Devengados.idDevengado AS id,
                Devengados.NombreDevengado AS Nombre,
                Devengados.CodigoDevengado AS codigo,
                Empleados_has_Devengados.Valor AS Valor,
                Empleados_has_Devengados.Observacion AS Observacion,
                CAST(Empleados_has_Devengados.aplica AS INT) AS aplica
            FROM Empleados
            LEFT JOIN Empleados_has_Devengados ON Empleados_has_Devengados.Empleados_idEmpleado = Empleados.idEmpleado 
            RIGHT JOIN Devengados ON Devengados.idDevengado = Empleados_has_Devengados.Devengados_idDevengado
            WHERE Empleados_has_Devengados.Empleados_idEmpleado = %s
            '''
    tupla = (idEmpleado,)
    devengados = list(cx.consulta_cp(sql,tupla).fetchall())

    sql  = "SELECT idDevengado AS id, CodigoDevengado AS codigo, NombreDevengado AS Nombre FROM Devengados"
    dv = cx.consulta_sp(sql).fetchall()
    codigosdv = [k['codigo'] for k in devengados]

    for d in dv:
        if d['codigo'] not in codigosdv:
            devengados.append(d)
    data['devengados'] = devengados

    sql = '''SELECT Descuentos.idDescuento AS id,
                Descuentos.NombreDescuento AS Nombre,
                Descuentos.CodigoDescuento AS codigo,
                Empleados_has_Descuentos.Valor AS Valor,
                Empleados_has_Descuentos.Observacion AS Observacion,
                CAST(Empleados_has_Descuentos.aplica AS INT) AS aplica
            FROM Empleados
            LEFT JOIN Empleados_has_Descuentos ON Empleados_has_Descuentos.Empleados_idEmpleado = Empleados.idEmpleado 
            LEFT JOIN Descuentos ON Descuentos.idDescuento = Empleados_has_Descuentos.Descuentos_idDescuento
            WHERE Empleados_has_Descuentos.Empleados_idEmpleado = %s'''
    tupla = (idEmpleado,) 
    descuentos = list(cx.consulta_cp(sql,tupla).fetchall())

    sql  = "SELECT idDescuento AS id, CodigoDescuento AS codigo, NombreDescuento AS Nombre FROM Descuentos"
    ds = cx.consulta_sp(sql).fetchall()
    codigosds = [k['codigo'] for k in descuentos]

    for d in ds:
        if d['codigo'] not in codigosds:
            descuentos.append(d)

    data['descuentos'] = descuentos


    cx.cerrar_conexion()

    if request.method == 'POST':
        dic = request.form
        cx = Conexion(SERVER, USER, PASSWORD, DB)

        for key in dic:
            #print(dic.getlist(key))
            id = dic.getlist(key)[0]
            valor = dic.getlist(key)[1]
            observacion = dic.getlist(key)[2]
            if 'on' in dic.getlist(key):
                aplica = 1
            else:
                aplica = 0
            
            if key[0] == 'D':
                sql = "INSERT INTO Empleados_has_Devengados (Empleados_idEmpleado, Devengados_idDevengado, Valor, Observacion, aplica) VALUES (%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE Empleados_idEmpleado = %s, Devengados_idDevengado = %s, Valor = %s, Observacion = %s, aplica = %s"
                tupla = (idEmpleado,id,valor,observacion,aplica, idEmpleado,id,valor,observacion,aplica)
                cx.consulta_cp(sql,tupla)
                cx.commit()
                #print('devengados')
            else:
                sql = "INSERT INTO Empleados_has_Descuentos (Empleados_idEmpleado, Descuentos_idDescuento, Valor, Observacion, aplica) VALUES (%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE Empleados_idEmpleado = %s, Descuentos_idDescuento = %s, Valor = %s, Observacion = %s, aplica = %s"
                tupla = (idEmpleado,id,valor,observacion,aplica,idEmpleado,id,valor,observacion,aplica)
                cx.consulta_cp(sql,tupla)
                cx.commit()              
                #print('descuentos')
        return redirect(idEmpleado)
        
        cx.cerrar_conexion()


    return render_template('editsalario.html', data = data) 


@app.route('/recibo/<idEmpleado>',methods = ['GET'])
def recibo(idEmpleado):
    data = {}
    cx = Conexion(SERVER, USER, PASSWORD, DB)


    sql = '''
    SELECT idEmpleado,
        Empleados.NombreEmpleado AS Nombre,
        Empleados.DocumentoEmpleado AS Documento, 
        Empleados.CuentaEmpleado AS cuenta,
        Empleados.IngresoEmpleado AS fingreso,
        Empleados.RetiroEmpleado AS fretiro, 
        Areas.NombreArea AS area, 
        Cargos.NombreCargo As cargo 
        FROM Empleados
        INNER JOIN Cargos ON Cargos.idCargo = Empleados.Cargos_idCargos
        INNER JOIN Areas ON Areas.idArea = Empleados.Areas_idAreas
        WHERE idEmpleado = %s
    '''

    tupla = (idEmpleado,)
    empleado = cx.consulta_cp(sql,tupla).fetchone()
    data['empleado'] = empleado

    sql = '''
            SELECT Devengados.idDevengado AS id,
                Devengados.NombreDevengado AS Nombre,
                Devengados.CodigoDevengado AS codigo,
                Empleados_has_Devengados.Valor AS Valor,
                Empleados_has_Devengados.Observacion AS Observacion,
                CAST(Empleados_has_Devengados.aplica AS INT) AS aplica
            FROM Empleados
            LEFT JOIN Empleados_has_Devengados ON Empleados_has_Devengados.Empleados_idEmpleado = Empleados.idEmpleado 
            RIGHT JOIN Devengados ON Devengados.idDevengado = Empleados_has_Devengados.Devengados_idDevengado
            WHERE Empleados_has_Devengados.Empleados_idEmpleado = %s
            '''
    tupla = (idEmpleado,)
    devengados = list(cx.consulta_cp(sql,tupla).fetchall())

    data['devengados'] = devengados

    sql = '''SELECT Descuentos.idDescuento AS id,
                Descuentos.NombreDescuento AS Nombre,
                Descuentos.CodigoDescuento AS codigo,
                Empleados_has_Descuentos.Valor AS Valor,
                Empleados_has_Descuentos.Observacion AS Observacion,
                CAST(Empleados_has_Descuentos.aplica AS INT) AS aplica
            FROM Empleados
            LEFT JOIN Empleados_has_Descuentos ON Empleados_has_Descuentos.Empleados_idEmpleado = Empleados.idEmpleado 
            LEFT JOIN Descuentos ON Descuentos.idDescuento = Empleados_has_Descuentos.Descuentos_idDescuento
            WHERE Empleados_has_Descuentos.Empleados_idEmpleado = %s'''
    tupla = (idEmpleado,) 
    descuentos = list(cx.consulta_cp(sql,tupla).fetchall())

    data['descuentos'] = descuentos

    data['total'] = sum( [k['Valor'] for k in devengados]) - sum([k['Valor'] for k in descuentos])

    cx.cerrar_conexion()

    return render_template('recibo.html', data = data) 

if __name__ == '__main__':
    app.run(debug=True)