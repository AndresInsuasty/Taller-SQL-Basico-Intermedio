# Taller SQL: "El Último Salto" - Tienda de Deportes Extremos

## Contexto del Negocio

Bienvenida/o al taller SQL práctico de **"El Último Salto"**, una tienda especializada en paracaidismo y deportes extremos ubicada en Pasto, Nariño. 

**Productos principales:** Paracaídas (militares, deportivos, emergencia) y accesorios de seguridad (cascos, altímetros, trajes de vuelo, gafas).

**Lógica especial:** Existe un cupón llamado **"ULTIMO_SUSPIRO"** que ofrece un **30% de descuento** exclusivamente a clientes mayores de 60 años (nuestros "saltadores de oro").

**Base de datos:** `tienda.db` contiene 4 tablas normalizadas con datos sintéticos de aproximadamente 1,000+ transacciones de venta en los últimos 2 años.

---

## Instrucciones de Entrega

### 📋 Requisitos Generales

1. **Organización de carpetas**: Crea un repositorio Git con esta estructura:
   ```
   tu-nombre-solucion-sql/
   ├── README.md              # Tu presentación y guía rápida
   ├── soluciones/
   │   ├── 01_ejercicio.sql
   │   ├── 02_ejercicio.sql
   │   ├── ...
   │   └── 30_ejercicio.sql
   └── datos/
       └── tienda.db (copia de la BD original)
   ```

2. **Por cada ejercicio:**
   - Crea un archivo `XX_ejercicio.sql` donde XX es el número (01, 02, etc.)
   - Asegúrate de que el SQL es ejecutable directamente contra `tienda.db`
   - Incluye comentarios explicativos si tu solución es compleja
   - El resultado debe responder la pregunta de negocio

3. **Control de versiones:**
   - Usa `git init` para inicializar tu repositorio
   - Haz commits lógicos por cada ejercicio o grupo de ejercicios
   - Incluye un `.gitignore` que excluya archivos innecesarios
   - Sube a GitHub el codigo generado

4. **Documentación:**
   - En tu `README.md`, explica brevemente cómo ejecutar las soluciones
   - Menciona cualquier supuesto o interpretación que hayas hecho

---

## 🟢 NIVEL 1-2: EJERCICIOS FÁCILES (Consultas Básicas)

Estos ejercicios practican `SELECT`, `WHERE`, `ORDER BY` y funciones de agregación simples como `COUNT()` y `SUM()`.

### Ejercicio 1
**Pregunta:** ¿Cuántos clientes tenemos registrados en total?
```
Pista: COUNT(*) es tu amiga.
```

### Ejercicio 2
**Pregunta:** Enlista todos los productos de la categoría "Paracaídas" con sus precios, ordenados de mayor a menor precio.
```
Pista: Filtra por categoría y ordena descendente.
```

### Ejercicio 3
**Pregunta:** ¿Cuál es el paracaídas más caro que tenemos?
```
Pista: MAX() + WHERE para filtrar categoría.
```

### Ejercicio 4
**Pregunta:** ¿Cuántas transacciones de venta hemos registrado?
```
Pista: COUNT() sobre la tabla ventas.
```

### Ejercicio 5
**Pregunta:** Muestra el nombre, correo y fecha de nacimiento de todos los clientes, ordenados alfabéticamente por nombre.
```
Pista: SELECT simple con ORDER BY.
```

### Ejercicio 6
**Pregunta:** ¿Cuál fue el monto total de ventas en toda la historia?
```
Pista: SUM(total_venta) desde la tabla ventas.
```

### Ejercicio 7
**Pregunta:** Enlista todos los productos de "Accesorios" con precio menor a $500.
```
Pista: WHERE con múltiples condiciones.
```

### Ejercicio 8
**Pregunta:** ¿Cuántas ventas utilizaron el cupón "ULTIMO_SUSPIRO"?
```
Pista: COUNT() con WHERE para el cupón específico.
```

### Ejercicio 9
**Pregunta:** ¿Cuál fue la venta con mayor monto en toda la historia?
```
Pista: MAX(total_venta).
```

### Ejercicio 10
**Pregunta:** Muestra todos los clientes de género "F" (femenino) ordenados por fecha de nacimiento (más viejitas primero).
```
Pista: WHERE genero = 'F' y ORDER BY fecha_nacimiento ASC.
```

### Ejercicio 11
**Pregunta:** ¿Número total de líneas (detalles) de venta registradas?
```
Pista: COUNT(*) sobre detalle_ventas.
```

### Ejercicio 12
**Pregunta:** ¿Cuál es el precio promedio de los productos en stock?
```
Pista: AVG(precio) desde productos.
```

### Ejercicio 13
**Pregunta:** ¿Cuántos productos tenemos en la categoría "Paracaídas"?
```
Pista: COUNT() + WHERE categoria.
```

### Ejercicio 14
**Pregunta:** Muestra todas las ventas realizadas en el año 2025, ordenadas por fecha (más recientes primero).
```
Pista: WHERE + YEAR(), ORDER BY DESC.
```

### Ejercicio 15
**Pregunta:** ¿Cuál es el accesorio más barato disponible?
```
Pista: MIN(precio) + WHERE categoria = 'Accesorios'.
```

---

## 🟡 NIVEL 3-4: EJERCICIOS INTERMEDIOS (JOINS, GROUP BY, HAVING, CTEs, Subconsultas)

Estos ejercicios requieren obligatoriamente:
- **JOINS** (INNER, LEFT, RIGHT según sea necesario)
- **GROUP BY** y **HAVING**
- **WITH (CTEs)** o **Subconsultas**


### Ejercicio 16
**Pregunta:** ¿Cuál es el cliente que más dinero ha gastado en total? Muestra su nombre y monto total.
```
Pista: SUM(total_venta), GROUP BY id_cliente, JOIN con clientes, ORDER BY y LIMIT.
```

### Ejercicio 17
**Pregunta:** ¿Cuánto dinero hemos dejado de ingresar por el cupón "ULTIMO_SUSPIRO"? (Calcula la diferencia entre lo que hubiera sido sin descuento y lo que fue con descuento).
```
Pista: Calcula el total con descuento y sin descuento. Usa subconsultas o CTEs.
Consideración: Si el descuento es 30%, significa 70% del precio original. Invierte: monto_actual / 0.70 - monto_actual.
```

### Ejercicio 18
**Pregunta:** Enlista todos los clientes mayores de 60 años que han hecho compras, mostrando nombre, edad aproximada y total gastado.
```
Pista: DATEDIFF o CAST(strftime() ...) para calcular edad. JOIN con ventas, GROUP BY, HAVING.
```

### Ejercicio 19
**Pregunta:** ¿Cuál es el producto más vendido en cantidad (en términos de unidades, no dinero)?
```
Pista: SUM(cantidad) sobre detalle_ventas, GROUP BY producto, JOIN con productos.
```

### Ejercicio 20
**Pregunta:** Para cada categoría de producto, calcula el ingreso total, cantidad de unidades vendidas y ticket promedio por venta.
```
Pista: GROUP BY categoria, SUM(total_venta), COUNT(*), AVG().
```

### Ejercicio 21
**Pregunta:** ¿Cuáles son los clientes que han usado el cupón "ULTIMO_SUSPIRO" al menos 3 veces?
```
Pista: COUNT() con HAVING para filtrar grupos.
```

### Ejercicio 22
**Pregunta:** Crea una clasificación de clientes por nivel de gasto: 
- "Alto Valor" si gastó más de $5,000
- "Medio Valor" si gastó entre $2,000 y $5,000
- "Bajo Valor" si gastó menos de $2,000

Muestra nombre, categoría de gasto y total gastado.
```
Pista: GROUP BY + CASE WHEN para clasificación.
```

### Ejercicio 23
**Pregunta:** ¿Cuáles son los 5 productos con mayor ingresos acumulado?
```
Pista: JOIN detalle_ventas con productos, SUM(cantidad * precio_unitario), GROUP BY, ORDER BY DESC, LIMIT 5.
```

### Ejercicio 24
**Pregunta:** Para cada mes en 2025, calcula: total de ventas, número de transacciones, y ticket promedio.
```
Pista: strftime('%m', fecha_venta) + GROUP BY mes, AVG(total_venta).
```

### Ejercicio 25
**Pregunta:** ¿Cuál es el cliente que compró la mayor variedad de productos diferentes (no cantidad, sino tipos distintos)?
```
Pista: COUNT(DISTINCT id_producto), GROUP BY id_cliente, ORDER BY DESC, LIMIT 1.
```

### Ejercicio 26
**Pregunta:** Identifica clientes que compraron SOLO paracaídas (nunca compraron accesorios). Muestra nombre y total gastado.
```
Pista: Subconsulta o CTE para filtrar clientes cuyas compras contienen SOLO la categoría "Paracaídas".
```

### Ejercicio 27
**Pregunta:** ¿Cuál es la diferencia en ingresos entre el mes con mayor venta y el mes con menor venta en 2025?
```
Pista: CTE para calcular ingresos por mes, luego MAX() - MIN().
```

### Ejercicio 28
**Pregunta:** Crea un reporte de "clientes de riesgo": aquellos cuya última compra fue hace más de 180 días a partir de hoy. Muestra nombre, correo y fecha de última compra.
```
Pista: MAX(fecha_venta) por cliente, HAVING MAX(fecha_venta) < DATE('now', '-180 days').
```

### Ejercicio 29
**Pregunta:** ¿Cuál es el porcentaje de ventas (por ingresos) que provienen del cupón "ULTIMO_SUSPIRO"?
```
Pista: SUM(total_venta) con y sin cupón, luego calcula (ventas_con_cupón / total) * 100.
```

### Ejercicio 30
**Pregunta:** Genera un análisis demográfico: para cada rango de edad (18-29, 30-39, ..., 70+), cuenta clientes únicos, número de transacciones y ingresos totales. Ordena por rango de edad.
```
Pista: CASE WHEN para rangos de edad, GROUP BY rango, múltiples agregaciones.
```

---

## 📊 Esquema de la Base de Datos

Consulta este esquema si necesitas entender la estructura:

```sql
-- Clientes: información demográfica
CREATE TABLE clientes (
    id_cliente INTEGER PRIMARY KEY,
    nombre TEXT,
    correo TEXT,
    fecha_nacimiento DATE,
    genero TEXT
);

-- Productos: catálogo
CREATE TABLE productos (
    id_producto INTEGER PRIMARY KEY,
    nombre TEXT,
    categoria TEXT,        -- "Paracaídas" o "Accesorios"
    precio REAL,
    stock INTEGER
);

-- Ventas: transacciones principales
CREATE TABLE ventas (
    id_venta INTEGER PRIMARY KEY,
    id_cliente INTEGER,    -- FK a clientes
    fecha_venta DATE,
    total_venta REAL,
    cupon_usado TEXT       -- NULL o "ULTIMO_SUSPIRO"
);

-- Detalle de Ventas: líneas de cada transacción
CREATE TABLE detalle_ventas (
    id_detalle INTEGER PRIMARY KEY,
    id_venta INTEGER,      -- FK a ventas
    id_producto INTEGER,   -- FK a productos
    cantidad INTEGER,
    precio_unitario REAL
);
```

---

## 🛠️ Cómo Ejecutar las Soluciones

### Opción 1: Con `sqlite3` en línea de comandos
```bash
cd tu-nombre-solucion-sql/soluciones
sqlite3 ../datos/tienda.db < 01_ejercicio.sql
```

### Opción 2: Con cualquier IDE SQL (DBeaver, DataGrip, etc.)
1. Abre `tienda.db`
2. Copia el contenido del archivo `.sql` en el editor de consultas
3. Ejecuta

### Opción 3: Con Python (si lo prefieres)
```python
import sqlite3
conn = sqlite3.connect('tienda.db')
cursor = conn.cursor()
with open('01_ejercicio.sql', 'r') as f:
    cursor.executescript(f.read())
for row in cursor.fetchall():
    print(row)
```

---

## 💡 Consejos y Buenas Prácticas

1. **Lee bien la pregunta:** Asegúrate de entender qué se pide antes de escribir SQL.
2. **Visualiza el flujo:** Dibuja (mentalmente o en papel) cómo se relacionan las tablas.
3. **Ordena resultados sensatamente:** Si pides El cliente que más gastó, ordena descendente.
4. **Usa alias:** Para tablas largas usa `c` para `clientes`, `v` para `ventas`, etc.
5. **Comenta código complejo:** Si tu JOIN tiene varias condiciones, explica por qué.
6. **Valida resultados:** ¿Tiene sentido el resultado? ¿Son cifras razonables?

---

## 📈 Niveles de Dificultad Esperados

| Ejercicio | Dificultad | Conocimientos Requeridos |
|-----------|-----------|--------------------------|
| 1-15 | 🟢 Fácil | SELECT, WHERE, ORDER BY, COUNT, SUM, MIN, MAX, AVG |
| 16-30 | 🟡 Intermedio | JOINS, GROUP BY, HAVING, CTEs (WITH), Subconsultas, CASE WHEN |

---

## ✅ Rubrica de Evaluación (orientativa)

- **Corrección SQL:** ¿El query ejecuta sin errores? ¿Responde la pregunta?
- **Eficiencia:** ¿Usa índices implícitamente (por ejemplo, en JOINs)?
- **Claridad:** ¿El código es legible con nombres sensatos?
- **Documentación:** ¿Incluyes comentarios si es necesario?
- **Organización Git:** ¿El repo está bien estructurado y los commits son coherentes?

---

## 🎓 Recursos Adicionales

- **SQLite Docs:** https://www.sqlite.org/lang.html
- **SQL Tutorial:** https://youtube.com/playlist?list=PLuAKekN0nRzxQFTiDMOl-7mFEPZThWhID&si=O3fXcE2_G79yKwny
- **Regex en SQLite:** Para búsquedas avanzadas, SQLite soporta GLOB y LIKE.

---

## 📝 Preguntas Frecuentes

**P: ¿Puedo usar CTEs o solo subconsultas?**  
R: Ambas están permitidas. CTEs (WITH) suele ser más legible con datos grandes.

**P: ¿Qué pasa si mi edad calculada no es exacta?**  
R: Es normal. Usa `CAST(strftime('%Y', 'now') - strftime('%Y', fecha_nacimiento) AS INT)` para aproximación.

**P: ¿Puedo modificar la base de datos?**  
R: No. Trabaja solo con SELECT. Los ejercicios son de lectura.

**P: ¿Necesito optimizar JOINs?**  
R: No es obligatorio, pero es buena práctica.

---

## 🚀 ¡Listo para Empezar!

1. Crea tu directorio de soluciones
2. Copia `tienda.db` a tu carpeta `datos/`
3. Resuelve los ejercicios en orden
4. Haz commits en git
5. Entrega tu repositorio

**¡Buena suerte, saltador! 🪂**
