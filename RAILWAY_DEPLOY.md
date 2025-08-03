# 🚀 Deploy ListaFácil na Railway

## Pré-requisitos
- Conta no GitHub
- Conta na Railway (https://railway.app)
- Código do projeto no GitHub

## Passos para Deploy

### 1. Preparar o Repositório
```bash
git add .
git commit -m "Prepare for Railway deployment"
git push origin main
```

### 2. Criar Projeto na Railway
1. Acesse https://railway.app
2. Faça login com GitHub
3. Clique em "New Project"
4. Selecione "Deploy from GitHub repo"
5. Escolha o repositório ListaFácil

### 3. Configurar Variáveis de Ambiente
Na dashboard da Railway, vá em Variables e adicione:

```
SECRET_KEY=sua-chave-secreta-super-forte-aqui
FLASK_ENV=production
FLASK_DEBUG=False
```

### 4. Banco de Dados
- A Railway criará automaticamente um PostgreSQL
- A variável `DATABASE_URL` será configurada automaticamente
- As migrações serão executadas automaticamente no deploy

### 5. Deploy Automático
- A Railway fará o build e deploy automaticamente
- Aguarde alguns minutos para o processo completar
- Sua aplicação estará disponível na URL fornecida pela Railway

## Arquivos de Configuração

Os seguintes arquivos foram criados/configurados para a Railway:

- **Procfile**: Define comandos de inicialização
- **railway.json**: Configurações específicas da Railway
- **runtime.txt**: Especifica versão do Python
- **requirements.txt**: Dependências incluindo gunicorn e psycopg2
- **railway_init.py**: Script de inicialização do banco
- **.env.example**: Exemplo de variáveis de ambiente

## Funcionalidades Incluídas

✅ **Configuração de Produção**
- Gunicorn como servidor WSGI
- PostgreSQL como banco de dados
- Configurações de segurança
- Logs de produção

✅ **Inicialização Automática**
- Migrações do banco executadas automaticamente
- Categorias padrão criadas automaticamente
- Tratamento de erros durante inicialização

✅ **Segurança**
- CSRF protection habilitada
- Configurações seguras para produção
- Variáveis de ambiente para dados sensíveis

## Monitoramento

Após o deploy, você pode:
- Ver logs em tempo real na dashboard da Railway
- Monitorar uso de recursos
- Configurar domínio customizado
- Configurar variáveis de ambiente adicionais

## Troubleshooting

### Erro de Build
- Verifique se todos os arquivos estão commitados
- Confirme que requirements.txt está atualizado

### Erro de Database
- Verifique se as migrações estão na pasta migrations/
- Confirme que o PostgreSQL foi provisionado

### Erro de Aplicação
- Verifique logs na dashboard da Railway
- Confirme que SECRET_KEY está configurada

## Comandos Úteis

```bash
# Ver logs da aplicação
railway logs

# Conectar ao banco de dados
railway connect

# Executar comandos na aplicação
railway run python manage.py shell
```

🎉 **Sua aplicação ListaFácil estará rodando na Railway!**