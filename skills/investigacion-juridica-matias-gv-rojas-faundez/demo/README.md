# Legalizes 🇨🇱

**Asistente Legal con Inteligencia Artificial para Chile**

Legalizes es una plataforma SaaS fullstack que permite a abogados, estudiantes de derecho, empresas y personas naturales consultar normativa chilena, recibir asesoría legal fundamentada y generar documentos legales profesionales.

## 🏛️ Base Normativa

- **CC** - Código Civil
- **CPC** - Código de Procedimiento Civil
- **CPP** - Código Procesal Penal
- **CT** - Código Tributario
- **Ley 21.719** - Ley de Protección de Datos Personales

## 🚀 Características

### Asistente Legal IA
- Consultas en lenguaje natural
- Respuestas fundamentadas con citas normativas
- Contexto de conversaciones
- Especializado en derecho chileno

### Buscador Normativo
- 37+ normas chilenas vigentes
- Búsqueda por código, categoría y contenido
- Visualización detallada de artículos
- Filtros avanzados

### Generador de Documentos
- Plantillas profesionales validadas
- Demandas (alimentos, despido)
- Contratos (arriendo, prestación de servicios)
- Cartas de notificación
- Poderes simples

### Dashboard
- Métricas de uso
- Historial de actividad
- Gestión de créditos
- Perfil de usuario

## 🛠️ Stack Tecnológico

### Frontend
- React 18 + TypeScript
- Tailwind CSS
- React Router DOM
- TanStack Query
- Zustand (estado global)
- Framer Motion
- Recharts

### Backend
- Node.js + Express + TypeScript
- Supabase (PostgreSQL)
- JWT Authentication
- bcryptjs

## 📁 Estructura del Proyecto

```
legalizes/
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Layout.tsx
│   │   │   ├── AuthModal.tsx
│   │   │   ├── ChatInterface.tsx
│   │   │   ├── LawSearch.tsx
│   │   │   └── DocumentGenerator.tsx
│   │   ├── pages/
│   │   │   ├── Home.tsx
│   │   │   ├── Dashboard.tsx
│   │   │   ├── Chat.tsx
│   │   │   ├── Laws.tsx
│   │   │   ├── Documents.tsx
│   │   │   └── Profile.tsx
│   │   ├── hooks/
│   │   │   ├── useAuth.ts
│   │   │   └── useChat.ts
│   │   ├── lib/
│   │   │   ├── api.ts
│   │   │   └── utils.ts
│   │   └── styles/
│   │       └── globals.css
│   ├── package.json
│   ├── vite.config.ts
│   └── tsconfig.json
├── backend/
│   ├── src/
│   │   ├── routes/
│   │   │   ├── auth.ts
│   │   │   ├── chat.ts
│   │   │   ├── laws.ts
│   │   │   ├── documents.ts
│   │   │   └── users.ts
│   │   ├── middleware/
│   │   │   └── auth.ts
│   │   ├── utils/
│   │   │   └── chileanLaws.ts
│   │   └── index.ts
│   ├── package.json
│   └── tsconfig.json
└── shared/
    └── types/
        └── index.ts
```

## 🚀 Instalación y Uso

### Requisitos
- Node.js 18+
- npm o yarn
- Cuenta de Supabase

### 1. Clonar y configurar

```bash
git clone <repo-url>
cd legalizes
```

### 2. Backend

```bash
cd backend
npm install
```

Crear archivo `.env`:
```env
PORT=3001
JWT_SECRET=tu-secret-key-super-seguro
SUPABASE_URL=https://tu-proyecto.supabase.co
SUPABASE_SERVICE_KEY=tu-service-key
FRONTEND_URL=http://localhost:5173
```

```bash
npm run dev
```

### 3. Frontend

```bash
cd frontend
npm install
```

Crear archivo `.env`:
```env
VITE_API_URL=http://localhost:3001/api
```

```bash
npm run dev
```

### 4. Base de datos (Supabase)

Ejecutar el siguiente SQL en el SQL Editor de Supabase:

```sql
-- Tabla de usuarios
CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  email TEXT UNIQUE NOT NULL,
  password_hash TEXT NOT NULL,
  nombre TEXT,
  apellido TEXT,
  rut TEXT,
  empresa TEXT,
  tipo_usuario TEXT DEFAULT 'abogado',
  plan TEXT DEFAULT 'free',
  creditos INTEGER DEFAULT 100,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Tabla de conversaciones
CREATE TABLE conversations (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES users(id) ON DELETE CASCADE,
  title TEXT,
  messages JSONB DEFAULT '[]',
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Tabla de documentos
CREATE TABLE documents (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES users(id) ON DELETE CASCADE,
  template_id TEXT,
  title TEXT,
  content TEXT,
  variables JSONB,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Función para decrementar créditos
CREATE OR REPLACE FUNCTION decrement_credits(user_id UUID, amount INTEGER)
RETURNS VOID AS $$
BEGIN
  UPDATE users 
  SET creditos = GREATEST(0, creditos - amount)
  WHERE id = user_id;
END;
$$ LANGUAGE plpgsql;
```

## 📝 Licencia

MIT License - VibeCodingChile.cl

## 📞 Contacto

- Email: contacto@vibecodingchile.cl
- Teléfono: +56 9 2964 8142
- Web: [vibecodingchile.cl](https://vibecodingchile.cl)

---

**Disclaimer:** Legalizes es una herramienta de asistencia legal. Las respuestas generadas por IA deben ser verificadas por un abogado titulado antes de ser utilizadas en procedimientos legales formales.
