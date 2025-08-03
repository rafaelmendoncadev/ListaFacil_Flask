# 🔧 Troubleshooting - ListaFácil

## Problemas Comuns de Deploy

### ❌ "App failed to load" na Railway

**Sintomas:**
- Erro: `[ERROR] Reason: App failed to load.`
- Deploy falha durante a inicialização

**Soluções Implementadas:**

1. **Arquivo WSGI Dedicado** (`wsgi.py`)
   ```python
   # Evita importações circulares
   from app import create_app
   app = create_app()
   ```

2. **Procfile Otimizado**
   ```
   release: python railway_init.py
   web: gunicorn wsgi:app --bind 0.0.0.0:$PORT
   ```

3. **Importações Corrigidas** (`app/__init__.py`)
   - Moveu `from app import models` para dentro da função `create_app()`
   - Evita importações circulares

### ❌ Problemas de Banco de Dados

**Sintomas:**
- Tabelas não existem
- Erro: `no such table: category`

**Soluções:**

1. **Script de Inicialização** (`railway_init.py`)
   - Executa migrações automaticamente
   - Cria categorias padrão
   - Tratamento robusto de erros

2. **Migrações Incluídas**
   - Arquivo: `migrations/versions/2f2050a7d169_initial_migration.py`
   - Cria todas as tabelas necessárias

### ❌ Problemas de Configuração

**Sintomas:**
- Variáveis de ambiente não encontradas
- Configuração incorreta

**Soluções:**

1. **Configuração Híbrida** (`config.py`)
   ```python
   # PostgreSQL para produção, SQLite para desenvolvimento
   DATABASE_URL = os.environ.get('DATABASE_URL')
   if DATABASE_URL and DATABASE_URL.startswith('postgres://'):
       DATABASE_URL = DATABASE_URL.replace('postgres://', 'postgresql://', 1)
   ```

2. **Variáveis Necessárias na Railway:**
   - `SECRET_KEY`: Chave secreta para sessões
   - `DATABASE_URL`: Configurada automaticamente

## 🧪 Testes Locais

### Verificar Importações
```bash
python test_import.py
```

### Testar WSGI
```bash
python wsgi.py
```

### Testar Migrações
```bash
python railway_init.py
```

## 📋 Checklist de Deploy

- [ ] Arquivo `wsgi.py` existe
- [ ] `Procfile` configurado corretamente
- [ ] Migrações criadas (`migrations/versions/`)
- [ ] `requirements.txt` atualizado
- [ ] Variável `SECRET_KEY` configurada na Railway
- [ ] Código commitado e pushed para GitHub

## 🔍 Debug na Railway

1. **Logs de Deploy:**
   - Acesse o dashboard da Railway
   - Vá para "Deployments"
   - Clique no deploy com falha
   - Verifique os logs de build e runtime

2. **Logs de Runtime:**
   - Use o comando: `railway logs`
   - Ou acesse via dashboard

3. **Variáveis de Ambiente:**
   - Verifique se `SECRET_KEY` está definida
   - Confirme se `DATABASE_URL` foi gerada automaticamente

## 📞 Suporte

Se os problemas persistirem:

1. Verifique os logs detalhados na Railway
2. Execute os testes locais
3. Confirme que todas as dependências estão no `requirements.txt`
4. Verifique se o código está na branch `main` do GitHub