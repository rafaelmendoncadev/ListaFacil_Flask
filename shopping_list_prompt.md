# Prompt: Sistema de Controle de Lista de Compras - Micro SAAS

## Visão Geral
Desenvolva um sistema web completo para controle de listas de compras de supermercado usando Flask e SQLite. O sistema deve ser um micro SAAS para uso pessoal, com interface moderna e funcionalidades essenciais.

## Stack Tecnológica
- **Backend**: Flask (Python)
- **Banco de Dados**: SQLite
- **Frontend**: HTML5, CSS3, JavaScript vanilla
- **Styling**: Tailwind CSS (via CDN)
- **Autenticação**: Flask-Login
- **Formulários**: Flask-WTF
- **ORM**: SQLAlchemy

## Funcionalidades Principais

### 1. Autenticação e Usuários
- Sistema de cadastro e login
- Sessões seguras
- Reset de senha por email (opcional)
- Perfil do usuário

### 2. Gestão de Listas
- Criar múltiplas listas de compras
- Nomear e categorizar listas (Ex: "Compras da Semana", "Festa de Aniversário")
- Arquivar/desarquivar listas
- Duplicar listas existentes
- Deletar listas

### 3. Gestão de Itens
- Adicionar itens à lista
- Categorizar itens (Frutas, Carnes, Limpeza, etc.)
- Definir quantidade e unidade (kg, unidade, litros)
- Adicionar preço estimado
- Marcar como comprado/não comprado
- Adicionar notas aos itens
- Busca e filtros por categoria

### 4. Interface e Experiência
- Dashboard com visão geral das listas
- Interface responsiva (mobile-first)
- Modo escuro/claro
- Atalhos de teclado
- Arrastar e soltar para reorganizar itens
- Checkboxes animados
- Notificações toast

### 5. Recursos Extras
- Histórico de compras
- Itens mais comprados (sugestões)
- Calculadora de total estimado
- Exportar lista (PDF/TXT)
- Compartilhar lista via link (somente leitura)
- Estatísticas básicas (gastos por categoria)

## Estrutura do Banco de Dados

### Tabelas Principais:
```sql
Users (id, username, email, password_hash, created_at)
Lists (id, user_id, name, description, category, archived, created_at)
Items (id, list_id, name, category, quantity, unit, estimated_price, is_purchased, notes, position, created_at)
Categories (id, name, color)
PurchaseHistory (id, user_id, item_name, category, price, purchased_at)
```

## Estrutura de Arquivos
```
shopping-list-saas/
├── app.py
├── config.py
├── requirements.txt
├── instance/
│   └── database.db
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── forms.py
│   ├── auth/
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── forms.py
│   ├── main/
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── dashboard.html
│   │   ├── list_detail.html
│   │   └── auth/
│   └── static/
│       ├── css/
│       ├── js/
│       └── images/
```

## Requisitos Técnicos

### Dependências (requirements.txt):
```
Flask==2.3.3
Flask-SQLAlchemy==3.0.5
Flask-Login==0.6.3
Flask-WTF==1.1.1
WTForms==3.0.1
Werkzeug==2.3.7
email-validator==2.0.0
```

### Funcionalidades de Segurança:
- Hash de senhas com Werkzeug
- CSRF protection
- Validação de formulários
- Sanitização de inputs
- Rate limiting básico

### Performance:
- Lazy loading de itens
- Paginação para listas grandes
- Índices no banco de dados
- Compressão de arquivos estáticos

## Interface e Design

### Paleta de Cores Sugerida:
- Primária: #059669 (Verde)
- Secundária: #DC2626 (Vermelho)
- Neutra: #6B7280 (Cinza)
- Fundo: #F9FAFB (Claro) / #1F2937 (Escuro)

### Componentes UI:
- Cards para listas
- Modal para adicionar itens
- Dropdown para categorias
- Toggle switches
- Progress bars
- Loading spinners

## Funcionalidades Avançadas (Opcionais)
- PWA (Progressive Web App)
- Sincronização offline
- Notificações push
- Integração com APIs de supermercados
- OCR para capturar notas fiscais
- Comparação de preços
- Alertas de vencimento

## Critérios de Sucesso
1. Interface intuitiva e responsiva
2. Performance rápida (< 2s carregamento)
3. Funciona offline (básico)
4. Zero bugs críticos
5. Código limpo e documentado
6. Deploy fácil

## Entregáveis
1. Código fonte completo
2. Banco de dados com dados de exemplo
3. Documentação de instalação
4. README com instruções
5. Arquivo de configuração para deploy
6. Testes básicos

## Comandos para Execução
```bash
# Instalação
pip install -r requirements.txt

# Inicialização do banco
flask db init
flask db migrate
flask db upgrade

# Execução
flask run
```

---

**Objetivo Final**: Criar um sistema funcional, moderno e escalável que possa servir como base para um micro SAAS de listas de compras, com foco na experiência do usuário e facilidade de manutenção.