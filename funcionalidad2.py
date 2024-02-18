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

