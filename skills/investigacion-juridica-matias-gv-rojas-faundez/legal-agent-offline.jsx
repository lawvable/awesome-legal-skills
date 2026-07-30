import { useState, useEffect, useRef, useCallback } from "react";

// ─── KNOWLEDGE BASE COMPLETA LEY 21.719 ────────────────────────────────────
const KB = [
  {
    q: ["vigencia","cuándo","cuando","entra en vigor","fecha"],
    a: `**Vigencia Ley 21.719:**
Publicada: **13 de diciembre de 2024**
Promulgada: **25 de noviembre de 2024**
Vigencia plena: **1 de diciembre de 2026** (mes 24° post publicación)
Última modificación: Ley 21.806 del **05-FEB-2026**
→ *Art. 1° Transitorio*`
  },
  {
    q: ["objeto","ámbito","aplicación","aplica","scope"],
    a: `**Objeto y Ámbito (Art. 1°):**
Regular la forma y condiciones del **tratamiento y protección de datos personales** de personas naturales, conforme al Art. 19 N°4 de la Constitución.

**Aplica a:**
- Toda persona natural o jurídica (incluidos órganos públicos)
- Tratamiento realizado en territorio nacional
- Empresas extranjeras que ofrezcan servicios a residentes en Chile
- Monitoreo de comportamiento de personas en Chile

**NO aplica a:**
- Libertades de emitir opinión e informar (Art. 19 N°12)
- Actividades personales de personas naturales`
  },
  {
    q: ["dato personal","definición","qué es dato","concepto"],
    a: `**Dato Personal (Art. 2° literal f):**
Cualquier información **vinculada o referida a una persona natural identificada o identificable**.

Se considera identificable quien pueda determinarse directa o indirectamente mediante:
- Nombre, RUT, cédula de identidad
- Datos de identidad física, fisiológica, genética
- Datos psíquicos, económicos, culturales o sociales

Para determinar identificabilidad → considerar **todos los medios razonablemente disponibles** en el momento del tratamiento.`
  },
  {
    q: ["sensibles","datos sensibles","categorías especiales","especial protección"],
    a: `**Datos Personales Sensibles (Art. 2° literal g):**
Datos que se refieren a:
- Origen **étnico o racial**
- Afiliación **política, sindical o gremial**
- Situación **socioeconómica**
- Convicciones **ideológicas o filosóficas**
- Creencias **religiosas**
- Datos de **salud y perfil biológico humano**
- Datos **biométricos**
- Vida sexual, **orientación sexual e identidad de género**

→ *Requieren consentimiento EXPRESO (Art. 16°)*
→ *Sanciones agravadas por tratamiento ilícito*`
  },
  {
    q: ["principios","principio","licitud","lealtad","finalidad","proporcionalidad","calidad","responsabilidad","seguridad","transparencia","confidencialidad"],
    a: `**Principios del Tratamiento (Art. 3°):**

**a) Licitud y Lealtad** — Solo tratamiento lícito y leal. El responsable debe acreditar licitud.

**b) Finalidad** — Fines específicos, explícitos y lícitos. No usar con finalidades distintas salvo compatibilidad, contrato o nuevo consentimiento.

**c) Proporcionalidad** — Solo datos necesarios, adecuados y pertinentes. Conservar solo el tiempo necesario; luego suprimir o anonimizar.

**d) Calidad** — Datos exactos, completos, actuales y pertinentes.

**e) Responsabilidad** — El responsable responde legalmente por el cumplimiento.

**f) Seguridad** — Garantizar estándares adecuados: confidencialidad, integridad, disponibilidad y resiliencia.

**g) Transparencia e Información** — Información permanentemente accesible, precisa, clara, inequívoca y gratuita.

**h) Confidencialidad** — Deber de secreto que subsiste después de concluida la relación con el titular.`
  },
  {
    q: ["derechos","arco","acceso","rectificación","supresión","oposición","portabilidad","bloqueo","titular"],
    a: `**Derechos del Titular (Art. 4°):**
Son personales, intransferibles e irrenunciables. No pueden limitarse por acto o convención.

**1. Acceso (Art. 5°)** — Confirmar si sus datos son tratados; acceder a datos, origen, finalidad, destinatarios y período de tratamiento.

**2. Rectificación (Art. 6°)** — Modificar datos inexactos, desactualizados o incompletos. El responsable debe comunicar cambios a terceros.

**3. Supresión (Art. 7°)** — Eliminar datos cuando no sean necesarios, se revoque consentimiento, sean ilícitos, caducos, o por resolución judicial/Agencia.

**4. Oposición (Art. 8°)** — Oponerse al tratamiento basado en interés legítimo, marketing directo, o datos de fuentes públicas.

**5. Portabilidad (Art. 9°)** — Obtener copia en formato electrónico estructurado y transferir a otro responsable (solo tratamiento automatizado + consentimiento).

**6. Bloqueo (Art. 8° ter)** — Suspender temporalmente el tratamiento mientras se resuelve rectificación, supresión u oposición.

→ *Rectificación, supresión y oposición: siempre GRATUITOS*
→ *Acceso: gratuito al menos trimestralmente*`
  },
  {
    q: ["consentimiento","autorización","libre","informado","específico","revocar","revocación"],
    a: `**Consentimiento (Art. 12°):**
Manifestación de voluntad **libre, informada, específica, previa e inequívoca**.

**Formas válidas:**
- Declaración verbal, escrita o electrónica
- Acto afirmativo que dé cuenta de la voluntad

**Características:**
- El responsable **debe probar** que contó con él
- Es **revocable** en cualquier momento, sin expresión de causa
- La revocación **no tiene efectos retroactivos**
- Los medios de otorgamiento/revocación deben ser expeditos, fidedignos, gratuitos y disponibles

**Presunción de no libre otorgamiento:** Cuando se recaba en ejecución de un contrato o servicio donde no es necesario recogerlo.

→ *Para datos sensibles: consentimiento EXPRESO (Art. 16°)*`
  },
  {
    q: ["licitud","fuentes","sin consentimiento","otras fuentes","bases legales","base legal"],
    a: `**Otras Fuentes de Licitud (Art. 13°):**
Es lícito tratar datos SIN consentimiento cuando:

**a)** Datos de obligaciones económicas, financieras, bancarias o comerciales (Título III)

**b)** Necesario para cumplir **obligación legal**

**c)** Necesario para **celebrar o ejecutar un contrato** entre titular y responsable, o medidas precontractuales

**d)** Necesario para satisfacer **intereses legítimos** del responsable o tercero, sin afectar derechos del titular

**e)** Necesario para **formulación, ejercicio o defensa de un derecho** ante tribunales u órganos públicos

→ *El responsable SIEMPRE debe acreditar la licitud*`
  },
  {
    q: ["obligaciones","responsable","deber","deberes","responsabilidades"],
    a: `**Obligaciones del Responsable (Art. 14°):**

- Informar y poner a disposición antecedentes que acrediten la licitud
- Asegurar que datos se recojan de fuentes lícitas con fines explícitos
- Comunicar o ceder información exacta, completa y actual
- Suprimir o anonimizar datos obtenidos para medidas precontractuales
- Cumplir todos los principios y obligaciones de la ley

**Deber de Secreto/Confidencialidad (Art. 14 bis):** Subsiste después de concluida la relación con el titular.

**Deber de Transparencia (Art. 14 ter):** Mantener en sitio web: política de tratamiento, identidad del responsable, domicilio, categorías de datos, medidas de seguridad, derechos del titular, etc.

**Protección desde el diseño y por defecto (Art. 14 quáter):** Medidas técnicas y organizativas desde el diseño y por defecto, tratando solo los datos estrictamente necesarios.

**Medidas de seguridad (Art. 14 quinquies):** Confidencialidad, integridad, disponibilidad y resiliencia; seudonimización y cifrado; capacidad de restaurar acceso.

**Reporte de vulneraciones (Art. 14 sexies):** Reportar a la Agencia sin dilaciones indebidas cuando exista riesgo razonable para derechos de los titulares.`
  },
  {
    q: ["cesión","ceder","transferir","comunicar"],
    a: `**Cesión de Datos Personales (Art. 15°):**
Transferencia de datos de un responsable a otro responsable.

**Requiere:**
- Consentimiento del titular (salvo excepciones)
- Cumplimiento de fines del tratamiento
- Constar por escrito o medio electrónico idóneo
- Individualizar partes, datos, finalidades y estipulaciones

**Puede ceder sin consentimiento cuando:**
- Necesario para cumplir/ejecutar un contrato donde el titular es parte
- Exista interés legítimo del cedente/cesionario (Art. 13° d)
- Lo disponga la ley

**Efectos:** El cesionario adquiere condición de **responsable de datos**. Cesión sin consentimiento cuando era necesario → **NULA**, debe suprimir todos los datos.`
  },
  {
    q: ["agencia","institución","autoridad de control","organismo","fiscalizador"],
    a: `**Agencia de Protección de Datos Personales (Art. 30°):**
Corporación autónoma de derecho público, carácter técnico, descentralizada, con personalidad jurídica y patrimonio propio.
Se relaciona con el Presidente vía **Ministerio de Economía, Fomento y Turismo**.

**Dirección:** Consejo Directivo de 3 consejeros, designados por el Presidente con acuerdo del Senado (2/3 en ejercicio). Duración: **6 años**, dedicación exclusiva.

**Funciones principales (Art. 30 bis):**
- Dictar instrucciones y normas generales
- Fiscalizar cumplimiento de la ley
- Aplicar sanciones
- Resolver reclamaciones de titulares
- Certificar modelos de prevención
- Administrar el Registro Nacional de Sanciones y Cumplimiento
- Determinar países con niveles adecuados de protección`
  },
  {
    q: ["sanciones","multas","infracción","infracciones","leve","grave","gravísima","utm","sanción"],
    a: `**Régimen Sancionatorio (Arts. 34-38):**

**Infracciones LEVES → hasta 5.000 UTM:**
- Incumplir deber de información/transparencia
- Carecer de domicilio electrónico actualizado
- Omitir o responder fuera de plazo solicitudes del titular
- Incumplir instrucciones de la Agencia

**Infracciones GRAVES → hasta 10.000 UTM:**
- Tratar datos sin consentimiento o sin base legal
- Comunicar/ceder datos sin consentimiento cuando es necesario
- Tratar datos con finalidad distinta a la recolectada
- Vulnerar deber de secreto o seguridad
- Tratar datos de NNA con infracción a la ley
- Realizar transferencias internacionales ilegales

**Infracciones GRAVÍSIMAS → hasta 20.000 UTM:**
- Tratamiento fraudulento de datos
- Vulnerar confidencialidad de datos sensibles
- Tratar datos sensibles/NNA a sabiendas en contravención a la ley
- Omitir deliberadamente comunicación de vulneraciones de seguridad
- Incumplir resolución de la Agencia sobre derechos ARCO+

**Reincidencia:** Hasta 3x el monto. Empresa grande reincidente: 2% (grave) o 4% (gravísima) de ingresos anuales, lo que sea mayor.`
  },
  {
    q: ["niños","niñas","adolescentes","menores","nna","infantil"],
    a: `**Datos de Niños, Niñas y Adolescentes (Art. 16 quáter):**

**Definiciones:**
- **Niños/Niñas:** menores de 14 años
- **Adolescentes:** entre 14 y 18 años

**Reglas:**
- Solo se puede tratar atendiendo el **interés superior** y respetando su autonomía progresiva
- **Niños/Niñas (< 14 años):** requiere consentimiento de **padres o representantes legales**
- **Adolescentes (14-18):** pueden consentir como adultos, EXCEPTO datos sensibles de menores de 16 años → requieren consentimiento de padres/representantes
- **Datos sensibles de adolescentes < 16 años:** siempre consentimiento de padres/representantes

**Obligación especial:** Establecimientos educacionales y entidades que traten datos de NNA deben velar por su uso lícito y protección.`
  },
  {
    q: ["biométricos","biométrico","huella","iris","facial","reconocimiento"],
    a: `**Datos Biométricos (Art. 16 ter):**
Datos obtenidos a partir de tratamiento técnico específico, relativos a características **físicas, fisiológicas o conductuales** que permiten identificación única.

**Ejemplos:** Huella digital, iris, rasgos de la mano o faciales, voz.

**Para tratar datos biométricos se debe:**
1. Cumplir con Art. 16° (consentimiento expreso)
2. Informar al titular:
   - Identificación del sistema biométrico usado
   - Finalidad específica del uso
   - Período de utilización
   - Forma de ejercer derechos

**Sin consentimiento:** Solo en los casos del Art. 16 bis inciso 2° (salud en emergencias, etc.)`
  },
  {
    q: ["transferencia internacional","internacional","transfronterizo","extranjero","exterior"],
    a: `**Transferencia Internacional de Datos (Arts. 27-29):**

**Lícita cuando:**
1. País destino tiene **niveles adecuados de protección** (determinado por la Agencia)
2. Amparada por **cláusulas contractuales** o normas corporativas vinculantes con garantías adecuadas
3. El responsable adopta **modelo de cumplimiento certificado**

**Sin adecuación ni garantías (casos específicos no habituales):**
- Consentimiento expreso del titular
- Transferencias bancarias/financieras/bursátiles
- Tratados internacionales ratificados por Chile
- Convenios de cooperación entre órganos públicos
- Autorización legal expresa
- Colaboración judicial internacional
- Ejecución de contrato con el titular
- Medidas urgentes médicas/sanitarias

→ *La Agencia determina países adecuados y aprueba cláusulas modelo*`
  },
  {
    q: ["órganos públicos","sector público","gobierno","estado","organismos","municipio"],
    a: `**Tratamiento por Órganos Públicos (Título IV, Arts. 20-26):**

**Regla general (Art. 20°):** Es lícito cuando se realiza para cumplimiento de funciones legales dentro del ámbito de sus competencias. **No requieren consentimiento** del titular.

**Principios aplicables:** Los del Art. 3° más coordinación, probidad y eficiencia.

**Cesión entre organismos públicos (Art. 22°):** Permitida cuando necesaria para funciones legales de ambos organismos. El receptor solo puede conservarlos por el tiempo necesario para el tratamiento específico.

**Cesión a privados:** Requiere **consentimiento del titular**, salvo funciones de fiscalización o inspección.

**Regímenes especiales (Art. 24°):**
- Prevención e investigación penal
- Seguridad Nacional y defensa
- Situaciones de emergencia/catástrofe declarada
- Información protegida por secreto, reserva o confidencialidad`
  },
  {
    q: ["modelo de prevención","programa de cumplimiento","delegado","encargado de prevención","certificación"],
    a: `**Modelo de Prevención de Infracciones (Arts. 49-53):**
Los responsables pueden adoptar **voluntariamente** un programa de cumplimiento.

**Elementos mínimos:**
a) Designación de **Delegado de Protección de Datos Personales**
b) Definición de medios y facultades del delegado
c) Identificación del tipo de información y bases de datos
d) Identificación de actividades/procesos de riesgo
e) Protocolos y procedimientos preventivos
f) Mecanismos de reporte interno y a la Agencia
g) Sanciones administrativas internas y procedimientos de denuncia

**Certificación:** La Agencia certifica que el modelo cumple requisitos. Vigencia: **3 años**.

**Beneficio:** Haber cumplido diligentemente el modelo es **circunstancia atenuante** de responsabilidad (Art. 36° N°5).`
  },
  {
    q: ["procedimiento","reclamar","reclamación","tutela","plazo","agencia reclamar"],
    a: `**Procedimientos (Arts. 41-43):**

**Procedimiento ante el responsable (Art. 11°):**
- Solicitud escrita al responsable (email/formulario/medio electrónico)
- Plazo respuesta: **30 días corridos** (prorrogable 30 días más)
- Denegación → Agencia en **30 días hábiles**

**Procedimiento administrativo tutela de derechos (Art. 41°):**
- Titular reclama ante la Agencia cuando responsable deniega o no responde
- Agencia notifica al responsable: **30 días corridos** para responder
- Duración máxima del procedimiento: **6 meses**
- Resolución impugnable judicialmente en **15 días hábiles**

**Procedimiento sancionatorio (Art. 42°):**
- Agencia instruye de oficio o a petición de parte
- Formulación de cargos → responsable tiene **15 días hábiles** para descargos
- Plazo máximo: **6 meses**

**Reclamación judicial (Art. 43°):**
- Ante Corte de Apelaciones de Santiago o domicilio del reclamante
- Plazo: **15 días hábiles** desde notificación de resolución`
  },
  {
    q: ["geolocalización","geolocación","ubicación","localización","gps"],
    a: `**Datos de Geolocalización (Art. 16 sexies):**
Pueden tratarse bajo las mismas fuentes de licitud de los Arts. 12° y 13° (consentimiento u otras bases legales).

**El titular SIEMPRE debe ser informado de:**
- Tipo de datos de geolocalización que serán tratados
- Finalidad y duración del tratamiento
- Si los datos se comunicarán o cederán a un tercero para servicios con valor añadido

→ *Mismas reglas generales + deber de información específico*`
  },
  {
    q: ["anonimización","seudonimización","anonimizar","seudonimizar","anonimizado"],
    a: `**Anonimización vs Seudonimización (Art. 2°):**

**Anonimización (literal k):** Procedimiento **IRREVERSIBLE** en virtud del cual el dato no puede vincularse a persona determinada ni permitir su identificación. Un dato anonimizado **deja de ser dato personal**.

**Seudonimización (literal l):** Tratamiento que hace que los datos ya no puedan atribuirse a un titular sin usar **información adicional**, siempre que esa información adicional esté separada y protegida. El dato seudonimizado **sigue siendo dato personal**.

**Importancia práctica:**
- Datos anonimizados → salen del ámbito de la ley
- Datos seudonimizados → siguen protegidos, pero ofrecen mayor seguridad`
  },
  {
    q: ["evaluación de impacto","pia","dpia","privacy impact","impacto"],
    a: `**Evaluación de Impacto en Protección de Datos (Art. 15 ter):**
Requerida cuando el tratamiento pueda producir **alto riesgo** para los derechos de los titulares.

**SIEMPRE obligatoria cuando:**
a) Evaluación sistemática y exhaustiva de aspectos personales mediante decisiones automatizadas/perfiles con efectos jurídicos significativos
b) Tratamiento **masivo o a gran escala**
c) Tratamiento con **observación o monitoreo sistemático** de zona de acceso público
d) Tratamiento de datos sensibles en hipótesis de **excepción del consentimiento**

**La Agencia publicará:**
- Lista orientativa de operaciones que requieren o no evaluación
- Orientaciones mínimas para realizarla

Los responsables pueden **consultar a la Agencia** cuando el resultado indique alto riesgo.`
  },
  {
    q: ["decisiones automatizadas","perfiles","elaboración de perfiles","algoritmo","ia","inteligencia artificial"],
    a: `**Decisiones Individuales Automatizadas y Elaboración de Perfiles (Art. 8° bis):**

**Elaboración de perfiles (Art. 2° literal w):** Tratamiento automatizado para evaluar, analizar o predecir aspectos relativos a: rendimiento profesional, situación económica, salud, preferencias, intereses, fiabilidad, comportamiento, ubicación o movimientos.

**Derecho a NO ser objeto de decisiones automatizadas** que produzcan efectos jurídicos o afecten significativamente al titular.

**Excepciones:**
a) Necesaria para celebrar/ejecutar contrato entre titular y responsable
b) Consentimiento previo y expreso del titular
c) Así lo señale la ley, con salvaguardas

**En TODOS los casos (incluso excepciones) el responsable debe:**
- Asegurar transparencia e información
- Proporcionar explicación de la lógica aplicada
- Permitir intervención humana
- Dar derecho a expresar punto de vista
- Permitir solicitar revisión de la decisión`
  },
  {
    q: ["hola","buenos días","buenas","saludos","ayuda","qué puedes hacer","funciones"],
    a: `¡Hola! Soy el **Agente Legal de Ley 21.719** funcionando 100% offline.

Puedo responder consultas sobre:
- 📋 **Principios** del tratamiento de datos
- 👤 **Derechos ARCO+** del titular
- ⚖️ **Régimen sancionatorio** (infracciones y multas)
- 🏛️ **Agencia de Protección de Datos Personales**
- 📄 **Obligaciones del responsable**
- 🔒 **Datos sensibles** y categorías especiales
- 🌍 **Transferencia internacional** de datos
- 📁 **Carga de archivos**: sube PDF, TXT o HTML y pregúntame sobre su contenido

También puedes **cargar archivos locales** usando el botón 📎 y luego hacerme preguntas sobre ellos.`
  },
];

// ─── SEARCH ENGINE OFFLINE ──────────────────────────────────────────────────
function searchKB(query) {
  const q = query.toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "");
  
  // Score each KB entry
  const scored = KB.map(entry => {
    let score = 0;
    for (const keyword of entry.q) {
      const kw = keyword.normalize("NFD").replace(/[\u0300-\u036f]/g, "");
      if (q.includes(kw)) score += kw.length * 2;
      else if (kw.split(" ").some(w => q.includes(w) && w.length > 3)) score += 3;
    }
    return { entry, score };
  }).filter(x => x.score > 0).sort((a, b) => b.score - a.score);

  if (scored.length > 0) return scored[0].entry.a;
  
  // Fallback: partial match
  const words = q.split(/\s+/).filter(w => w.length > 3);
  for (const word of words) {
    const found = KB.find(e => e.q.some(k => k.includes(word)));
    if (found) return found.a;
  }
  
  return null;
}

// ─── FILE TEXT EXTRACTOR ────────────────────────────────────────────────────
function extractTextFromHTML(html) {
  const tmp = document.createElement("div");
  tmp.innerHTML = html;
  return tmp.innerText || tmp.textContent || "";
}

function chunkText(text, size = 2000) {
  const chunks = [];
  for (let i = 0; i < text.length; i += size) chunks.push(text.slice(i, i + size));
  return chunks;
}

function searchInFile(text, query) {
  const q = query.toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "");
  const lines = text.split(/\n/).map(l => l.trim()).filter(Boolean);
  const results = [];
  
  const words = q.split(/\s+/).filter(w => w.length > 3);
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i].toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "");
    const matchCount = words.filter(w => line.includes(w)).length;
    if (matchCount > 0) {
      const ctx = lines.slice(Math.max(0, i - 1), i + 3).join(" ");
      results.push({ ctx, score: matchCount, i });
    }
  }
  
  results.sort((a, b) => b.score - a.score);
  const top = results.slice(0, 4).map(r => r.ctx);
  
  if (top.length === 0) return null;
  return `**Encontrado en el archivo cargado:**\n\n${top.map((t, i) => `[${i + 1}] ${t}`).join("\n\n")}`;
}

// ─── COMPONENTS ─────────────────────────────────────────────────────────────
const LEY_DATA = {
  numero: "21.719", nombre: "Protección y Tratamiento de Datos Personales",
  publicacion: "13-DIC-2024", vigencia: "01-DIC-2026",
  articulos: 55, titulos: 8, principios: 8, derechos: 6,
};

const SIDEBAR_ITEMS = [
  { id: "dashboard", icon: "⬛", label: "Dashboard" },
  { id: "chat", icon: "◈", label: "Agente Legal" },
  { id: "ley", icon: "§", label: "Ley 21.719" },
  { id: "metricas", icon: "▦", label: "Métricas" },
  { id: "sanciones", icon: "⚠", label: "Sanciones" },
  { id: "derechos", icon: "✦", label: "Derechos" },
];

const QUICK_QA = [
  "¿Cuándo entra en vigencia?",
  "¿Qué son datos sensibles?",
  "¿Cuáles son las sanciones?",
  "¿Qué derechos tiene el titular?",
  "¿Qué es el consentimiento?",
  "¿Qué hace la Agencia?",
  "¿Qué es la elaboración de perfiles?",
  "¿Qué es la evaluación de impacto?",
];

const DERECHOS_DATA = [
  { nombre: "Acceso", art: "Art. 5°", color: "#4FC1FF", desc: "Confirmar si sus datos son tratados; acceder a datos, origen, finalidad, destinatarios y período de tratamiento." },
  { nombre: "Rectificación", art: "Art. 6°", color: "#C3E88D", desc: "Modificar datos inexactos, desactualizados o incompletos. El responsable comunica cambios a terceros." },
  { nombre: "Supresión", art: "Art. 7°", color: "#F78C6C", desc: "Eliminar datos cuando no sean necesarios, se revoque consentimiento, sean ilícitos, caducos, o por resolución judicial/Agencia." },
  { nombre: "Oposición", art: "Art. 8°", color: "#C792EA", desc: "Oponerse al tratamiento basado en interés legítimo, marketing directo, o datos de fuentes públicas." },
  { nombre: "Portabilidad", art: "Art. 9°", color: "#FFCB6B", desc: "Obtener copia en formato electrónico estructurado y transferir a otro responsable (tratamiento automatizado + consentimiento)." },
  { nombre: "Bloqueo", art: "Art. 8° ter", color: "#89DDFF", desc: "Suspender temporalmente el tratamiento mientras se resuelve rectificación, supresión u oposición." },
];

const INFRACTION_DATA = [
  { tipo: "Leves", multa: "≤ 5.000 UTM", color: "#C3E88D", pct: 33, ejemplos: "Falta de transparencia, sin domicilio electrónico, omitir respuesta al titular" },
  { tipo: "Graves", multa: "≤ 10.000 UTM", color: "#F78C6C", pct: 66, ejemplos: "Tratar datos sin consentimiento, vulnerar seguridad, tratar datos NNA ilegalmente" },
  { tipo: "Gravísimas", multa: "≤ 20.000 UTM", color: "#FF5370", pct: 100, ejemplos: "Tratamiento fraudulento, vulnerar datos sensibles, incumplir resolución Agencia" },
];

function MiniBar({ value, max, color }) {
  const pct = Math.round((value / max) * 100);
  return (
    <div style={{ background: "#1e2530", borderRadius: 2, height: 6, width: "100%", overflow: "hidden" }}>
      <div style={{ width: `${pct}%`, height: "100%", background: color, borderRadius: 2, transition: "width 1.2s ease" }} />
    </div>
  );
}

function TerminalLine({ text, delay = 0, type = "info" }) {
  const [vis, setVis] = useState(false);
  useEffect(() => { const t = setTimeout(() => setVis(true), delay); return () => clearTimeout(t); }, [delay]);
  const colors = { info: "#4FC1FF", success: "#C3E88D", warn: "#F78C6C", error: "#FF5370", dim: "#546E7A" };
  if (!vis) return null;
  return (
    <div style={{ color: colors[type] || "#cdd3de", fontFamily: "monospace", fontSize: 12, lineHeight: 1.7, padding: "1px 0" }}>
      {text}
    </div>
  );
}

function ChatBubble({ role, text, typing }) {
  const [displayed, setDisplayed] = useState(typing ? "" : text);
  const [done, setDone] = useState(!typing);
  useEffect(() => {
    if (!typing) { setDisplayed(text); setDone(true); return; }
    let i = 0; setDisplayed("");
    const iv = setInterval(() => {
      i++; setDisplayed(text.slice(0, i));
      if (i >= text.length) { clearInterval(iv); setDone(true); }
    }, 8);
    return () => clearInterval(iv);
  }, [text, typing]);

  const isUser = role === "user";
  const parts = displayed.split(/(\*\*[^*]+\*\*)/g);

  return (
    <div style={{ display: "flex", justifyContent: isUser ? "flex-end" : "flex-start", marginBottom: 12, animation: "fadeIn 0.2s ease" }}>
      {!isUser && (
        <div style={{ width: 28, height: 28, borderRadius: "50%", background: "linear-gradient(135deg,#4FC1FF,#C792EA)", display: "flex", alignItems: "center", justifyContent: "center", fontSize: 12, marginRight: 8, flexShrink: 0, marginTop: 2 }}>§</div>
      )}
      <div style={{
        maxWidth: "80%", padding: "10px 14px",
        borderRadius: isUser ? "14px 14px 2px 14px" : "14px 14px 14px 2px",
        background: isUser ? "#1d3557" : "#1e2530",
        border: isUser ? "1px solid #4FC1FF44" : "1px solid #30363d",
        color: "#cdd3de", fontSize: 13, lineHeight: 1.7, whiteSpace: "pre-wrap",
        fontFamily: "monospace",
      }}>
        {parts.map((p, i) =>
          p.startsWith("**") && p.endsWith("**")
            ? <strong key={i} style={{ color: "#4FC1FF" }}>{p.slice(2, -2)}</strong>
            : p
        )}
        {!done && <span style={{ animation: "blink 1s infinite", color: "#4FC1FF" }}>▋</span>}
      </div>
    </div>
  );
}

// ─── MAIN APP ───────────────────────────────────────────────────────────────
export default function App() {
  const [activeTab, setActiveTab] = useState("dashboard");
  const [messages, setMessages] = useState([
    { role: "assistant", text: "Hola. Soy el Agente Legal de la Ley 21.719 — modo offline.\n\nPuedes preguntarme sobre la ley o **cargar un archivo** (PDF, TXT, HTML) usando el botón 📎 para consultarlo.", typing: false }
  ]);
  const [input, setInput] = useState("");
  const [sidebarOpen, setSidebarOpen] = useState(true);
  const [loadedFiles, setLoadedFiles] = useState([]);
  const [fileTexts, setFileTexts] = useState([]);
  const [thinking, setThinking] = useState(false);
  const [dragOver, setDragOver] = useState(false);
  const chatEndRef = useRef(null);
  const fileInputRef = useRef(null);

  useEffect(() => { chatEndRef.current?.scrollIntoView({ behavior: "smooth" }); }, [messages]);

  const processFile = useCallback(async (file) => {
    return new Promise((resolve) => {
      const reader = new FileReader();
      const name = file.name;
      const ext = name.split(".").pop().toLowerCase();

      reader.onload = (e) => {
        let text = "";
        if (ext === "pdf") {
          // For PDF: use text representation (binary → readable parts)
          const raw = e.target.result;
          // Extract readable text from PDF binary
          const matches = raw.match(/\(([^\)]{4,})\)/g) || [];
          text = matches.map(m => m.slice(1, -1)).join(" ");
          if (text.length < 100) text = raw.replace(/[^\x20-\x7E\n\r\t\u00C0-\u024F]/g, " ").replace(/\s+/g, " ");
        } else if (ext === "html" || ext === "htm") {
          text = extractTextFromHTML(e.target.result);
        } else {
          text = e.target.result;
        }
        resolve({ name, text: text.trim(), size: file.size, ext });
      };

      if (ext === "pdf") {
        reader.readAsBinaryString(file);
      } else {
        reader.readAsText(file, "UTF-8");
      }
    });
  }, []);

  const handleFiles = useCallback(async (files) => {
    const fileArr = Array.from(files);
    for (const file of fileArr) {
      const result = await processFile(file);
      setLoadedFiles(prev => [...prev, result.name]);
      setFileTexts(prev => [...prev, result]);
      setMessages(prev => [...prev, {
        role: "assistant",
        text: `✅ Archivo cargado: **${result.name}**\n${result.text.length > 100 ? `Texto extraído: ~${Math.round(result.text.length / 1000)}K caracteres\n\nAhora puedes preguntarme sobre el contenido de este archivo.` : "⚠️ No se pudo extraer texto. Prueba con un archivo TXT o HTML."}`,
        typing: false
      }]);
    }
  }, [processFile]);

  const handleDrop = useCallback((e) => {
    e.preventDefault();
    setDragOver(false);
    handleFiles(e.dataTransfer.files);
  }, [handleFiles]);

  const sendMessage = useCallback((text) => {
    const q = (text || input).trim();
    if (!q || thinking) return;
    setInput("");
    setMessages(prev => [...prev, { role: "user", text: q, typing: false }]);
    setThinking(true);

    setTimeout(() => {
      let answer = null;

      // Search in loaded files first if question seems to be about file content
      if (fileTexts.length > 0) {
        for (const ft of fileTexts) {
          const found = searchInFile(ft.text, q);
          if (found) { answer = found; break; }
        }
      }

      // Fall back to KB
      if (!answer) answer = searchKB(q);

      // Generic fallback
      if (!answer) {
        const hasFiles = fileTexts.length > 0;
        answer = `No encontré información específica sobre "${q}" en mi base de conocimiento de la Ley 21.719${hasFiles ? " ni en los archivos cargados" : ""}.

**Sugerencias:**
- Reformula la pregunta usando términos legales más específicos
- Consulta sobre: principios, derechos ARCO+, sanciones, consentimiento, datos sensibles, Agencia, transferencia internacional${hasFiles ? "" : "\n- Carga un archivo PDF, TXT o HTML con el texto de la ley usando el botón 📎"}`;
      }

      setMessages(prev => [...prev, { role: "assistant", text: answer, typing: true }]);
      setThinking(false);
    }, 400 + Math.random() * 300);
  }, [input, thinking, fileTexts]);

  return (
    <div
      style={{ display: "flex", height: "100vh", background: "#0d1117", fontFamily: "monospace", color: "#cdd3de", overflow: "hidden" }}
      onDragOver={e => { e.preventDefault(); setDragOver(true); }}
      onDragLeave={() => setDragOver(false)}
      onDrop={handleDrop}
    >
      <style>{`
        @keyframes blink{0%,100%{opacity:1}50%{opacity:0}}
        @keyframes fadeIn{from{opacity:0;transform:translateY(5px)}to{opacity:1;transform:none}}
        @keyframes pulse{0%,100%{opacity:0.6}50%{opacity:1}}
        ::-webkit-scrollbar{width:5px}
        ::-webkit-scrollbar-track{background:#0d1117}
        ::-webkit-scrollbar-thumb{background:#30363d;border-radius:3px}
        .nav-item:hover{background:#1e2530!important;color:#4FC1FF!important}
        .pill:hover{background:#1d3557!important;border-color:#4FC1FF!important;color:#4FC1FF!important}
        .art-row:hover{background:#1a2233!important}
        input:focus{border-color:#4FC1FF!important;outline:none}
      `}</style>

      {/* DRAG OVERLAY */}
      {dragOver && (
        <div style={{ position: "fixed", inset: 0, background: "#0d111788", border: "2px dashed #4FC1FF", zIndex: 999, display: "flex", alignItems: "center", justifyContent: "center", flexDirection: "column", gap: 12 }}>
          <div style={{ fontSize: 48 }}>📂</div>
          <div style={{ fontSize: 18, color: "#4FC1FF" }}>Suelta el archivo aquí</div>
          <div style={{ fontSize: 12, color: "#8b949e" }}>PDF · TXT · HTML</div>
        </div>
      )}

      {/* SIDEBAR */}
      <div style={{ width: sidebarOpen ? 196 : 46, background: "#161b22", borderRight: "1px solid #21262d", display: "flex", flexDirection: "column", transition: "width 0.2s", flexShrink: 0 }}>
        <div style={{ padding: "11px 8px", borderBottom: "1px solid #21262d", display: "flex", alignItems: "center", gap: 8 }}>
          <div style={{ width: 28, height: 28, borderRadius: 6, background: "linear-gradient(135deg,#4FC1FF,#C792EA)", display: "flex", alignItems: "center", justifyContent: "center", fontSize: 14, flexShrink: 0 }}>§</div>
          {sidebarOpen && <span style={{ fontSize: 10, fontWeight: "bold", color: "#4FC1FF", letterSpacing: 1 }}>LEY 21719</span>}
        </div>
        <div style={{ flex: 1, padding: "6px 4px" }}>
          {SIDEBAR_ITEMS.map(item => (
            <div key={item.id} className="nav-item" onClick={() => setActiveTab(item.id)}
              style={{ display: "flex", alignItems: "center", gap: 10, padding: "7px 9px", borderRadius: 5, marginBottom: 2, cursor: "pointer", background: activeTab === item.id ? "#1e2530" : "transparent", color: activeTab === item.id ? "#4FC1FF" : "#8b949e", fontSize: 13, transition: "all 0.15s" }}>
              <span style={{ fontSize: 15, flexShrink: 0 }}>{item.icon}</span>
              {sidebarOpen && <span style={{ fontSize: 11 }}>{item.label}</span>}
            </div>
          ))}
        </div>
        {/* Files loaded indicator */}
        {sidebarOpen && loadedFiles.length > 0 && (
          <div style={{ padding: "8px 10px", borderTop: "1px solid #21262d" }}>
            <div style={{ fontSize: 9, color: "#546E7A", marginBottom: 4 }}>ARCHIVOS CARGADOS</div>
            {loadedFiles.map(f => (
              <div key={f} style={{ fontSize: 10, color: "#C3E88D", padding: "2px 0", overflow: "hidden", textOverflow: "ellipsis", whiteSpace: "nowrap" }}>📄 {f}</div>
            ))}
          </div>
        )}
        <div style={{ padding: "6px 4px", borderTop: "1px solid #21262d" }}>
          <div className="nav-item" onClick={() => setSidebarOpen(!sidebarOpen)}
            style={{ display: "flex", alignItems: "center", gap: 10, padding: "7px 9px", borderRadius: 5, cursor: "pointer", color: "#546E7A", fontSize: 13 }}>
            <span style={{ fontSize: 15 }}>{sidebarOpen ? "◀" : "▶"}</span>
            {sidebarOpen && <span style={{ fontSize: 10 }}>Colapsar</span>}
          </div>
        </div>
      </div>

      {/* MAIN */}
      <div style={{ flex: 1, display: "flex", flexDirection: "column", overflow: "hidden" }}>
        {/* TOPBAR */}
        <div style={{ height: 38, background: "#161b22", borderBottom: "1px solid #21262d", display: "flex", alignItems: "center", padding: "0 14px", gap: 8, flexShrink: 0 }}>
          <div style={{ display: "flex", gap: 5 }}>
            {["#FF5370","#F78C6C","#C3E88D"].map((c,i) => <div key={i} style={{ width: 9, height: 9, borderRadius: "50%", background: c }} />)}
          </div>
          <span style={{ color: "#546E7A", fontSize: 10, marginLeft: 6 }}>legal-agent-offline</span>
          <span style={{ color: "#30363d" }}>—</span>
          <span style={{ color: "#4FC1FF", fontSize: 10 }}>{SIDEBAR_ITEMS.find(s => s.id === activeTab)?.label}</span>
          <div style={{ flex: 1 }} />
          <div style={{ display: "flex", alignItems: "center", gap: 6 }}>
            {loadedFiles.length > 0 && <span style={{ fontSize: 9, color: "#C3E88D", background: "#C3E88D22", border: "1px solid #C3E88D44", borderRadius: 4, padding: "2px 6px" }}>{loadedFiles.length} archivo{loadedFiles.length > 1 ? "s" : ""}</span>}
            <span style={{ fontSize: 9, color: "#546E7A", background: "#21262d", borderRadius: 4, padding: "2px 6px" }}>OFFLINE</span>
            <div style={{ width: 7, height: 7, borderRadius: "50%", background: "#C3E88D", animation: "pulse 2s infinite" }} />
          </div>
        </div>

        {/* CONTENT */}
        <div style={{ flex: 1, overflow: "auto", padding: 18 }}>

          {/* ── DASHBOARD ── */}
          {activeTab === "dashboard" && (
            <div style={{ animation: "fadeIn 0.3s ease" }}>
              <div style={{ marginBottom: 18 }}>
                <div style={{ fontSize: 9, color: "#546E7A", marginBottom: 3 }}>// PANEL PRINCIPAL · MODO OFFLINE</div>
                <div style={{ fontSize: 22, color: "#4FC1FF", fontWeight: "bold" }}>Ley N° 21.719</div>
                <div style={{ fontSize: 12, color: "#8b949e" }}>Protección y Tratamiento de Datos Personales · Chile · {LEY_DATA.publicacion}</div>
              </div>
              <div style={{ background: "#161b22", border: "1px solid #21262d", borderRadius: 8, padding: "9px 14px", marginBottom: 14, display: "flex", gap: 20, flexWrap: "wrap" }}>
                {[["PUBLICACIÓN","13-DIC-2024","#C3E88D"],["VIGENCIA","01-DIC-2026","#F78C6C"],["MINISTERIO","SEGPRES","#4FC1FF"],["MODIFICA","Ley 19.628","#C792EA"],["ÚLTIMA MOD.","Ley 21.806","#FFCB6B"]].map(([l,v,c]) => (
                  <div key={l}><span style={{ color: "#546E7A", fontSize: 9 }}>{l} </span><span style={{ color: c, fontSize: 11 }}>{v}</span></div>
                ))}
              </div>
              <div style={{ display: "grid", gridTemplateColumns: "repeat(4,1fr)", gap: 10, marginBottom: 14 }}>
                {[["Artículos",55,55,"#4FC1FF"],["Títulos",8,10,"#C3E88D"],["Principios",8,10,"#F78C6C"],["Derechos",6,8,"#C792EA"]].map(([l,v,m,c]) => (
                  <div key={l} style={{ background: "#161b22", border: "1px solid #21262d", borderRadius: 8, padding: 12 }}>
                    <div style={{ fontSize: 9, color: "#546E7A", marginBottom: 5 }}>{l.toUpperCase()}</div>
                    <div style={{ fontSize: 30, fontWeight: "bold", color: c, marginBottom: 8 }}>{v}</div>
                    <MiniBar value={v} max={m} color={c} />
                  </div>
                ))}
              </div>
              <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 12 }}>
                <div style={{ background: "#161b22", border: "1px solid #21262d", borderRadius: 8, padding: 14 }}>
                  <div style={{ fontSize: 9, color: "#546E7A", marginBottom: 10 }}>// TERMINAL — RESUMEN</div>
                  {[
                    ["$ cat ley-21719 --summary","dim",0],
                    ["→ Objeto: protección datos personales personas naturales","info",200],
                    ["→ Ámbito: nacional + extraterritorial (Art. 1° bis)","info",400],
                    ["→ Principios: 8 (licitud, finalidad, proporcionalidad...)","success",600],
                    ["→ Derechos ARCO+: acceso, rect., supresión, oposición...","success",800],
                    ["→ Agencia: corporación autónoma de derecho público","warn",1000],
                    ["→ Sanciones: 5K / 10K / 20K UTM (leve/grave/gravísima)","error",1200],
                    ["✓ Sistema listo — modo offline activado","success",1400],
                  ].map(([t,ty,d]) => <TerminalLine key={t} text={t} type={ty} delay={d} />)}
                </div>
                <div style={{ background: "#161b22", border: "1px solid #21262d", borderRadius: 8, padding: 14 }}>
                  <div style={{ fontSize: 9, color: "#546E7A", marginBottom: 10 }}>// DERECHOS DEL TITULAR (Art. 4°)</div>
                  {DERECHOS_DATA.map((d,i) => (
                    <div key={d.nombre} style={{ display: "flex", alignItems: "center", gap: 9, padding: "5px 0", borderBottom: i < 5 ? "1px solid #21262d" : "none" }}>
                      <div style={{ width: 18, height: 18, borderRadius: 3, background: d.color, display: "flex", alignItems: "center", justifyContent: "center", fontSize: 9, color: "#000", fontWeight: "bold" }}>{i+1}</div>
                      <span style={{ fontSize: 12, color: "#cdd3de" }}>{d.nombre}</span>
                      <div style={{ flex: 1 }} />
                      <span style={{ fontSize: 10, color: "#546E7A" }}>{d.art}</span>
                    </div>
                  ))}
                </div>
              </div>
            </div>
          )}

          {/* ── CHAT ── */}
          {activeTab === "chat" && (
            <div style={{ display: "flex", flexDirection: "column", height: "calc(100vh - 110px)", animation: "fadeIn 0.3s ease" }}>
              <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between", marginBottom: 10 }}>
                <div style={{ fontSize: 9, color: "#546E7A" }}>// AGENTE LEGAL OFFLINE — Ley 21.719</div>
                <div style={{ display: "flex", gap: 6, alignItems: "center" }}>
                  {fileTexts.map(f => (
                    <span key={f.name} style={{ fontSize: 9, color: "#C3E88D", background: "#C3E88D11", border: "1px solid #C3E88D33", borderRadius: 4, padding: "2px 6px" }}>📄 {f.name.slice(0, 20)}</span>
                  ))}
                </div>
              </div>

              {/* Pills */}
              <div style={{ display: "flex", gap: 5, flexWrap: "wrap", marginBottom: 10 }}>
                {QUICK_QA.map(q => (
                  <button key={q} className="pill" onClick={() => sendMessage(q)}
                    style={{ background: "#161b22", border: "1px solid #30363d", borderRadius: 20, padding: "3px 9px", color: "#8b949e", fontSize: 10, cursor: "pointer", transition: "all 0.15s", fontFamily: "monospace" }}>
                    {q}
                  </button>
                ))}
              </div>

              {/* Messages */}
              <div style={{ flex: 1, overflow: "auto", background: "#161b22", border: "1px solid #21262d", borderRadius: 8, padding: 14, marginBottom: 10 }}>
                {messages.map((m, i) => <ChatBubble key={i} {...m} />)}
                {thinking && (
                  <div style={{ display: "flex", alignItems: "center", gap: 8, color: "#546E7A", fontSize: 12 }}>
                    {[0,1,2].map(j => <div key={j} style={{ width: 6, height: 6, borderRadius: "50%", background: "#4FC1FF", animation: `blink 1s ${j*0.2}s infinite` }} />)}
                    <span>Buscando...</span>
                  </div>
                )}
                <div ref={chatEndRef} />
              </div>

              {/* Input row */}
              <div style={{ display: "flex", gap: 8 }}>
                <input type="file" ref={fileInputRef} multiple accept=".pdf,.txt,.html,.htm" style={{ display: "none" }}
                  onChange={e => handleFiles(e.target.files)} />
                <button onClick={() => fileInputRef.current?.click()}
                  title="Cargar archivo (PDF, TXT, HTML)"
                  style={{ background: "#161b22", border: "1px solid #30363d", borderRadius: 6, padding: "0 12px", color: "#8b949e", cursor: "pointer", fontSize: 16, flexShrink: 0 }}>
                  📎
                </button>
                <input value={input} onChange={e => setInput(e.target.value)}
                  onKeyDown={e => e.key === "Enter" && sendMessage()}
                  placeholder="Pregunta sobre Ley 21.719 o el archivo cargado..."
                  style={{ flex: 1, background: "#161b22", border: "1px solid #30363d", borderRadius: 6, padding: "9px 13px", color: "#cdd3de", fontSize: 12, fontFamily: "monospace", outline: "none", transition: "border-color 0.15s" }} />
                <button onClick={() => sendMessage()} disabled={thinking}
                  style={{ background: thinking ? "#21262d" : "#1d3557", border: "1px solid #4FC1FF", borderRadius: 6, padding: "9px 18px", color: "#4FC1FF", cursor: thinking ? "not-allowed" : "pointer", fontSize: 11, fontFamily: "monospace", flexShrink: 0 }}>
                  ENVIAR
                </button>
              </div>
              <div style={{ fontSize: 9, color: "#546E7A", textAlign: "center", marginTop: 5 }}>
                Arrastra archivos PDF · TXT · HTML aquí o usa 📎 · Funciona 100% offline
              </div>
            </div>
          )}

          {/* ── LEY ── */}
          {activeTab === "ley" && (
            <div style={{ animation: "fadeIn 0.3s ease" }}>
              <div style={{ fontSize: 9, color: "#546E7A", marginBottom: 12 }}>// ESTRUCTURA LEY 21.719</div>
              <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 10, marginBottom: 14 }}>
                {[
                  ["I","Derechos del titular","4-11","#4FC1FF"],
                  ["II","Tratamiento de datos personales","12-16 sexies","#C3E88D"],
                  ["III","Obligaciones financieras/comerciales","17-19","#F78C6C"],
                  ["IV","Tratamiento por órganos públicos","20-26","#C792EA"],
                  ["V","Transferencia internacional","27-29","#FFCB6B"],
                  ["VI","Agencia de Protección de Datos","30-32 bis","#89DDFF"],
                  ["VII","Infracciones, sanciones y procedimientos","33-53","#FF5370"],
                  ["VIII","Congreso, Poder Judicial y autónomos","54-55","#82AAFF"],
                ].map(([n,t,a,c]) => (
                  <div key={n} style={{ background: "#161b22", border: `1px solid ${c}33`, borderLeft: `3px solid ${c}`, borderRadius: 7, padding: 11 }}>
                    <div style={{ display: "flex", justifyContent: "space-between", marginBottom: 3 }}>
                      <span style={{ fontSize: 9, color: c }}>TÍTULO {n}</span>
                      <span style={{ fontSize: 9, color: "#546E7A" }}>Arts. {a}</span>
                    </div>
                    <div style={{ fontSize: 12, color: "#cdd3de" }}>{t}</div>
                  </div>
                ))}
              </div>
              <div style={{ background: "#161b22", border: "1px solid #21262d", borderRadius: 8, padding: 12 }}>
                <div style={{ fontSize: 9, color: "#546E7A", marginBottom: 8 }}>// ARTÍCULOS CLAVE</div>
                {[
                  ["Art. 1°","Objeto y ámbito de aplicación","BASE","#4FC1FF"],
                  ["Art. 3°","Principios del tratamiento","CORE","#C3E88D"],
                  ["Art. 12°","Regla general del consentimiento","CONSENT","#C792EA"],
                  ["Art. 13°","Otras fuentes de licitud","LICITUD","#F78C6C"],
                  ["Art. 14°","Obligaciones del responsable","OBLIG","#89DDFF"],
                  ["Art. 15 ter","Evaluación de impacto","DPIA","#FFCB6B"],
                  ["Art. 16°","Datos personales sensibles","SENS","#FF5370"],
                  ["Art. 30°","Agencia de Protección de Datos","AGENCIA","#82AAFF"],
                  ["Art. 35°","Sanciones","SANCIÓN","#FF5370"],
                ].map(([num,titulo,tag,c],i) => (
                  <div key={num} className="art-row" onClick={() => { setActiveTab("chat"); sendMessage(`Explícame el ${num} sobre ${titulo}`); }}
                    style={{ display: "flex", alignItems: "center", gap: 10, padding: "7px 5px", borderBottom: i < 8 ? "1px solid #21262d" : "none", cursor: "pointer", borderRadius: 4, transition: "background 0.15s" }}>
                    <span style={{ fontSize: 10, color: "#4FC1FF", width: 58, flexShrink: 0 }}>{num}</span>
                    <span style={{ fontSize: 12, color: "#cdd3de", flex: 1 }}>{titulo}</span>
                    <span style={{ fontSize: 9, background: `${c}22`, color: c, border: `1px solid ${c}44`, borderRadius: 3, padding: "2px 5px" }}>{tag}</span>
                  </div>
                ))}
                <div style={{ fontSize: 9, color: "#546E7A", marginTop: 6, textAlign: "center" }}>Clic en un artículo para consultarlo en el Agente Legal</div>
              </div>
            </div>
          )}

          {/* ── MÉTRICAS ── */}
          {activeTab === "metricas" && (
            <div style={{ animation: "fadeIn 0.3s ease" }}>
              <div style={{ fontSize: 9, color: "#546E7A", marginBottom: 12 }}>// MÉTRICAS — LEY 21.719</div>
              <div style={{ display: "grid", gridTemplateColumns: "repeat(3,1fr)", gap: 10, marginBottom: 14 }}>
                {[["Artículos",55,"#4FC1FF"],["Títulos",8,"#C3E88D"],["Principios",8,"#F78C6C"],["Derechos ARCO+",6,"#C792EA"],["Disp. Transitorias",8,"#FFCB6B"],["Tipos Infracciones",3,"#FF5370"]].map(([l,v,c]) => (
                  <div key={l} style={{ background: "#161b22", border: "1px solid #21262d", borderRadius: 7, padding: 14, textAlign: "center" }}>
                    <div style={{ fontSize: 34, fontWeight: "bold", color: c }}>{v}</div>
                    <div style={{ fontSize: 11, color: "#8b949e", marginTop: 4 }}>{l}</div>
                  </div>
                ))}
              </div>
              <div style={{ background: "#161b22", border: "1px solid #21262d", borderRadius: 8, padding: 14 }}>
                <div style={{ fontSize: 9, color: "#546E7A", marginBottom: 12 }}>// TIMELINE LEGISLATIVO</div>
                {[
                  ["NOV 2024","Promulgación por Presidente Boric","#C3E88D"],
                  ["13-DIC-2024","Publicación en Diario Oficial","#4FC1FF"],
                  ["JUN 2025","Reglamentos deben dictarse (6 meses)","#F78C6C"],
                  ["JUL 2025","Ley 21.755 modifica Art. transitorio 2°","#FFCB6B"],
                  ["FEB 2026","Ley 21.806 modifica Art. cuarto transitorio","#C792EA"],
                  ["JUN 2026","Designación Consejo Directivo Agencia","#89DDFF"],
                  ["01-DIC-2026","ENTRADA EN VIGENCIA PLENA","#FF5370"],
                ].map(([f,e,c],i,arr) => (
                  <div key={i} style={{ display: "flex", gap: 10, marginBottom: 8 }}>
                    <div style={{ display: "flex", flexDirection: "column", alignItems: "center" }}>
                      <div style={{ width: 10, height: 10, borderRadius: "50%", background: c, flexShrink: 0 }} />
                      {i < arr.length - 1 && <div style={{ width: 1, height: 18, background: "#21262d", margin: "2px 0" }} />}
                    </div>
                    <div>
                      <div style={{ fontSize: 9, color: c }}>{f}</div>
                      <div style={{ fontSize: 12, color: "#cdd3de" }}>{e}</div>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          )}

          {/* ── SANCIONES ── */}
          {activeTab === "sanciones" && (
            <div style={{ animation: "fadeIn 0.3s ease" }}>
              <div style={{ fontSize: 9, color: "#546E7A", marginBottom: 12 }}>// RÉGIMEN SANCIONATORIO — Arts. 34-38</div>
              {INFRACTION_DATA.map(inf => (
                <div key={inf.tipo} style={{ background: "#161b22", border: `1px solid ${inf.color}33`, borderLeft: `3px solid ${inf.color}`, borderRadius: 8, padding: 14, marginBottom: 10 }}>
                  <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: 7 }}>
                    <span style={{ fontSize: 13, color: inf.color, fontWeight: "bold" }}>Infracciones {inf.tipo}</span>
                    <span style={{ fontSize: 12, color: inf.color }}>{inf.multa}</span>
                  </div>
                  <div style={{ background: "#0d1117", borderRadius: 3, height: 7, marginBottom: 9, overflow: "hidden" }}>
                    <div style={{ width: `${inf.pct}%`, height: "100%", background: inf.color, borderRadius: 3 }} />
                  </div>
                  <div style={{ fontSize: 11, color: "#8b949e" }}>{inf.ejemplos}</div>
                </div>
              ))}
              <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 10 }}>
                <div style={{ background: "#161b22", border: "1px solid #21262d", borderRadius: 8, padding: 12 }}>
                  <div style={{ fontSize: 9, color: "#C3E88D", marginBottom: 8 }}>▼ ATENUANTES (Art. 36)</div>
                  {["Reparación unilateral al titular","Colaboración con la Agencia","Sin sanciones previas","Autodenuncia ante la Agencia","Modelo certificado de prevención vigente"].map(a => (
                    <div key={a} style={{ fontSize: 11, color: "#8b949e", padding: "3px 0", borderBottom: "1px solid #21262d" }}>+ {a}</div>
                  ))}
                </div>
                <div style={{ background: "#161b22", border: "1px solid #21262d", borderRadius: 8, padding: 12 }}>
                  <div style={{ fontSize: 9, color: "#FF5370", marginBottom: 8 }}>▲ AGRAVANTES (Art. 36)</div>
                  {["Reincidencia (2+ veces en 30 meses)","Carácter continuado de la infracción","Riesgo a derechos y libertades del titular"].map(a => (
                    <div key={a} style={{ fontSize: 11, color: "#8b949e", padding: "3px 0", borderBottom: "1px solid #21262d" }}>! {a}</div>
                  ))}
                  <div style={{ fontSize: 9, color: "#546E7A", marginTop: 8 }}>Empresa grande reincidente: hasta 2% (grave) o 4% (gravísima) de ingresos anuales</div>
                </div>
              </div>
            </div>
          )}

          {/* ── DERECHOS ── */}
          {activeTab === "derechos" && (
            <div style={{ animation: "fadeIn 0.3s ease" }}>
              <div style={{ fontSize: 9, color: "#546E7A", marginBottom: 12 }}>// DERECHOS DEL TITULAR — Arts. 4-11</div>
              {DERECHOS_DATA.map(d => (
                <div key={d.nombre} style={{ background: "#161b22", border: `1px solid ${d.color}33`, borderLeft: `3px solid ${d.color}`, borderRadius: 8, padding: 13, marginBottom: 9 }}>
                  <div style={{ display: "flex", justifyContent: "space-between", marginBottom: 5 }}>
                    <span style={{ fontSize: 13, color: d.color, fontWeight: "bold" }}>Derecho de {d.nombre}</span>
                    <span style={{ fontSize: 10, color: "#546E7A" }}>{d.art}</span>
                  </div>
                  <div style={{ fontSize: 12, color: "#8b949e", lineHeight: 1.6 }}>{d.desc}</div>
                </div>
              ))}
              <div style={{ background: "#161b22", border: "1px solid #21262d", borderRadius: 8, padding: 11, marginTop: 2 }}>
                <div style={{ fontSize: 9, color: "#546E7A", marginBottom: 5 }}>// PROCEDIMIENTO (Art. 11°)</div>
                <div style={{ fontSize: 12, color: "#8b949e", lineHeight: 1.7 }}>
                  Plazo respuesta: <span style={{ color: "#4FC1FF" }}>30 días corridos</span> (prorrogable 30 días) · Gratuito: rectificación, supresión, oposición · Acceso gratuito al menos trimestralmente · Ante denegación: reclamar ante Agencia en <span style={{ color: "#F78C6C" }}>30 días hábiles</span>
                </div>
              </div>
            </div>
          )}

        </div>
      </div>
    </div>
  );
}
