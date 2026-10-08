# floow — landing pages

Duas páginas estáticas (HTML + CSS, sem framework e sem build obrigatório):

- `dist/index.html` — floow para você (linha Personal, coral)
- `dist/empresas.html` — floow para empresas (linha Business, índigo) — **Em breve**, sem cadastro/login
- `dist/floow.css` — estilos compartilhados (tokens do Brand Guidelines 2026 v2.3)

## Colocar no ar

`dist/` já está pronta para qualquer host estático (Vercel, Netlify, Cloudflare Pages, GitHub Pages, S3).
Diretório de publicação: `dist`. Não há comando de build.

Teste local: `cd dist && python3 -m http.server 8080`

## Editar

O HTML é gerado por `src/build.py` (partes compartilhadas: nav, hero, ícones, FAQ, rodapé).
Edite `src/build.py` ou `src/floow-v4.css` e rode:

    cd src && python3 build.py --deploy    # gera src/dist/ com floow.css

(Sem `--deploy` ele gera a versão usada no artifact do Claude — ignore.)
Também dá para editar `dist/*.html` direto e abandonar o gerador.

## Pendências antes de publicar

- **Links dos CTAs**: "Começar agora" aponta para `#comecar`. Trocar pela URL de cadastro/login do web app.
- **Afirmações a validar**: seção Segurança ("dados criptografados", "sem venda de dados") e FAQ (agendamento de pagamentos, contas pessoal/empresa separadas).
- **Dados de exemplo**: valores no mockup do celular, painel e WhatsApp são ilustrativos (estão marcados).
- **Hero**: ilustração vetorial inline (`WOMAN` em build.py). Pode ser trocada por foto.
- **SEO/compartilhamento**: falta favicon, `og:image`/`og:title` e analytics.
- **Empresas**: quando lançar, remover as tags `.soon`, o botão `.btn-disabled` e a nota `.soon-note`, e voltar os CTAs.
