# Spec da landing do floow (Para você)

Versão 1, 05/11/2026. Escopo: `index.html`. A página de empresas fica como está até o produto sair.

## 1. Objetivo

A página existe para levar a pessoa ao cadastro. Uma ação principal só, repetida ao longo da página: **Começar grátis**, que leva a `app.floowapp.com.br/auth?tab=signup`. A ação secundária é **Ver como funciona**, que rola até a seção de passos. "Agendar demonstração" não entra: é um produto B2C de R$ 49,90 e ninguém agenda demo para isso.

Em até 5 segundos, quem chega precisa responder sozinho:

| Pergunta | Onde a página responde |
|---|---|
| O que o floow faz? | Título e subtítulo do hero |
| É para mim? | Seção de dores |
| Como funciona? | Três passos |
| Por que confiar? | Faixa de confiança logo abaixo do hero, segurança, FAQ |
| Quanto custa? | Planos, e a linha do trial embaixo do botão |
| O que faço agora? | Botão no hero, depois dos passos, nos planos e no fim |

Métrica principal: taxa de visita para cadastro concluído. Secundárias: clique no CTA por seção e profundidade de rolagem (ver seção 8).

## 2. Para quem

Pessoa física no Brasil, de 25 a 45 anos, com conta e cartão em mais de um banco. Muitas vezes também tem financiamento ou empréstimo e algum investimento. Já tentou planilha ou outro app e largou porque dava trabalho manter.

As dores que a página precisa nomear, na linguagem dela:

1. O salário entra e some, e no fim do mês ela não sabe para onde foi.
2. A fatura do cartão assusta todo mês, e as parcelas antigas se acumulam sem ela ver.
3. Empréstimo, financiamento e parcelado ficam espalhados, sem uma conta de quanto falta.
4. Os investimentos estão em dois ou três bancos, e ela não sabe quanto tem no total.
5. Lançar tudo à mão cansa, e por isso ela desistiu das ferramentas anteriores.

## 3. O que as referências ensinam

Estudei cinco páginas: YNAB, Monarch (duas páginas), Organizze, Meu Dinheiro e Mobills. Resumo do que copiar como padrão e do que evitar.

| Referência | O que faz bem | O que levar para o floow |
|---|---|---|
| YNAB | Título que nomeia a dor emocional; "sem cartão de crédito" colado no botão; imprensa, notas das lojas e estatísticas logo abaixo do hero; cards de dor que levam a páginas próprias; CTA repetido 4 vezes | Hero com dor ou resultado; linha de redução de risco embaixo do botão; prova social perto do CTA; seção de dores |
| Monarch | Título objetivo ("o app de dinheiro tudo em um"); "1 milhão de usuários" no hero; avaliações reais logo depois; cada recurso com título de benefício e print do produto; privacidade (sem anúncio, sem venda de dados) antes do CTA final | Print real do produto em cada recurso; números concretos ("13 mil instituições"); bloco de privacidade antes do fim |
| Organizze | Open Finance com destaque: selo no hero, seção própria, passo a passo e faixa de logos dos bancos; selo RA 1000; contagem de avaliações nas lojas; agente de IA como novidade | Seção de Open Finance com bancos que funcionam e o que acontece depois de conectar; selos de terceiros |
| Meu Dinheiro | Hero só com e-mail e "sem cartão de crédito"; FAQ transparente sobre renovação e reembolso | FAQ com cobrança, cancelamento e o que acontece no fim do trial |
| Mobills | Bloco de LGPD claro | Pouco. A home é um portal de conteúdo e dilui o produto: é o exemplo do que não fazer |

Padrões que se repetem nas páginas que convertem melhor:

- O hero mostra o produto de verdade, não ilustração. O Meu Dinheiro usa ilustração e é o mais fraco nisso.
- A redução de risco vai colada no botão: trial, sem cartão, cancelamento fácil.
- A prova social aparece antes da primeira rolagem ou logo depois.
- Uma ação principal só, sem caminhos concorrentes.
- Entre 8 e 10 seções. O Organizze, com 11 e duas novidades disputando atenção, fica longo.

O que nenhuma das brasileiras faz bem e o floow pode ocupar:

- Mostrar parcelas futuras do cartão e dívidas no mesmo lugar (o floow já faz, desde eb57c2d).
- Conferir o saldo do app com o saldo do banco (está no comparativo com o Meu Dinheiro).
- Ter um consultor de IA que responde no WhatsApp com os números da pessoa (o Organizze tem um agente, mas ligado ao ChatGPT ou Claude da própria pessoa).
- Trial de 30 dias do plano completo, sem cartão. O do Organizze é de 7 dias.

## 4. Estrutura, seção a seção

São dez blocos. Cada um tem um objetivo, e o que não cumpre objetivo sai.

### 4.0 Navegação

- Logo, depois Como funciona, Recursos, Planos e Segurança.
- À direita, Entrar e o botão Começar grátis.
- O seletor "Para você / Para empresas" sai do topo e vai para o rodapé, enquanto empresas estiver "em breve". Hoje ele ocupa o lugar mais caro da página para um produto que não existe.
- No celular: logo, Entrar e um botão curto "Criar conta".

### 4.1 Hero

Objetivo: dizer o que é, para quem, e dar o botão.

- **Título:** promessa de resultado, em até 10 palavras. Três opções para escolher:
  1. "Saiba para onde vai cada real, sem lançar nada à mão."
  2. "Conta, cartão, dívidas e investimentos organizados sozinhos."
  3. "Seu dinheiro organizado sozinho. Você em estado de flow." (mantém a marca)
- **Subtítulo:** uma frase com o mecanismo: "Conecte seus bancos pelo Open Finance e o floow importa, categoriza e avisa no WhatsApp o que vem a seguir."
- **CTA:** Começar grátis. Embaixo, a linha "30 dias do Pro grátis, sem cartão de crédito."
- **Secundário:** "Ver como funciona", em botão de contorno.
- **Visual:** print real do dashboard no computador, com o celular sobreposto mostrando uma mensagem do WhatsApp. Os dados vêm de uma org de demonstração (ver seção 6). Mockup desenhado em HTML não substitui o print.
- **Faixa de confiança** logo abaixo, numa linha só: "Conexão via Open Finance, regulado pelo Banco Central", logos dos bancos confirmados e "Seus dados não são vendidos". Quando houver, entram aqui a nota nas lojas ou o número de usuários.

### 4.2 Dores

Objetivo: a pessoa se reconhecer. São quatro cards curtos, cada um com a dor em uma linha e a resposta do floow em outra:

| Dor | Resposta |
|---|---|
| "O salário entra e some." | Cada gasto entra categorizado, e o resumo do mês mostra para onde foi. |
| "A fatura sempre assusta." | O total de cada fechamento e as parcelas que ainda vêm aparecem antes do vencimento. |
| "Perdi a conta das parcelas e dos empréstimos." | Dívidas com quanto já foi pago e quanto falta, com os parcelados do cartão incluídos. |
| "Meus investimentos estão em vários bancos." | Carteira e patrimônio somados numa visão só. |

### 4.3 Como funciona

Objetivo: tirar o medo de ser trabalhoso. São três passos numerados, cada um com um print pequeno, e o CTA no fim.

1. **Conecte.** Autorize seus bancos pelo Open Finance, ou importe o extrato em OFX ou CSV.
2. **O floow organiza.** Os lançamentos chegam categorizados. Você corrige uma vez, e a regra vale para os próximos parecidos.
3. **Acompanhe e pergunte.** Os avisos chegam no WhatsApp, e o consultor de IA responde suas dúvidas com os seus números.

Junto entra a frase de tempo, se for verdadeira e medida: "Em 5 minutos você vê o mês organizado" (ver pendência P5).

### 4.4 Recursos

Objetivo: provar profundidade. São no máximo cinco blocos alternados, cada um com título de benefício, duas linhas de texto e um print real:

1. Visão geral: saldo, gastos do mês e próximos vencimentos.
2. Cartão de crédito: fatura por fechamento e parcelas futuras.
3. Dívidas: empréstimos, financiamentos e parcelados, com quanto falta.
4. Investimentos e patrimônio: carteira, proventos, imóveis e veículos.
5. Ritmo de gastos: onde o mês deve fechar, com aviso quando uma categoria estoura.

### 4.5 Consultor de IA e WhatsApp

É o diferencial, então ganha seção própria e a maior área visual depois do hero.

- **Título:** "Pergunte ao seu consultor financeiro, no WhatsApp."
- **Visual:** conversa real de WhatsApp, com a pergunta da pessoa e a resposta que começa pelo número.
- **Três pontos:** análises diárias; resposta com os seus dados; nada acontece sem a sua confirmação.
- Antes de publicar, decidir o nome do recurso (ver pendência P6).

### 4.6 Prova social

Objetivo: confiança de gente como a pessoa.

Entram de 3 a 6 depoimentos reais, com nome, cidade e foto ou inicial. Se houver, entram também a nota nas lojas e o número de usuários. **Enquanto não houver depoimento real, a seção não existe.** Depoimento inventado está fora de questão.

### 4.7 Planos

Objetivo: tirar a dúvida do preço sem obrigar um clique a mais. Os dados vêm de `apps/web/lib/stripe/plans.ts` e `lib/plano/acesso.ts`:

| | Free | Pro |
|---|---|---|
| Preço | R$ 0 | R$ 49,90/mês (o Stripe ainda cobra R$ 19,90; ajustar antes de publicar) |
| Inclui | Até 2 contas, lançamentos manuais, dashboard e fluxo de caixa | Contas ilimitadas, Open Finance e OFX/CSV, investimentos, planejamento, suporte prioritário |
| CTA | Criar conta grátis | Testar o Pro grátis por 30 dias |

Embaixo da tabela entram duas linhas: "Toda conta nova começa com 30 dias do Pro, sem cartão de crédito." e "Cancele quando quiser" (ver pendência P3).

### 4.8 Segurança e privacidade

Objetivo: responder ao medo de conectar o banco. São quatro pontos:

1. **Open Finance:** você autoriza no app do banco e pode revogar quando quiser.
2. **Só leitura:** o floow lê os dados e não faz pagamentos nem transferências (ver pendência P4).
3. **Criptografia:** os dados trafegam e ficam guardados criptografados.
4. **Sem venda de dados**, de acordo com a LGPD, com link para a política.

### 4.9 FAQ

São oito perguntas, nesta ordem:

1. Meu banco funciona?
2. O floow mexe no meu dinheiro?
3. O que acontece depois dos 30 dias?
4. Posso cancelar quando quiser?
5. Preciso lançar tudo à mão?
6. Como funcionam os avisos no WhatsApp?
7. O consultor de IA é um consultor de verdade?
8. Tem app para celular?

A resposta da 7 precisa deixar claro que é uma IA e que ela não dá recomendação de investimento regulada.

### 4.10 CTA final e rodapé

- **CTA final:** título curto com o resultado, o botão e a linha do trial.
- **Rodapé:**
  - Para empresas (em breve), Segurança e Perguntas.
  - Termos de uso e Política de privacidade.
  - CNPJ da Limm e e-mail de contato.

## 5. Copy

- Português do Brasil, falando com "você". Frases curtas, com números concretos sempre que possível ("parcela 23 de 60", não "acompanhe suas dívidas").
- Nada de "revolucione", "inteligente", "completo", "solução" nem jargão financeiro sem explicação.
- Os títulos dizem o benefício, e os textos de apoio dizem o mecanismo.
- Toda promessa vem do que o código faz hoje. Se não está em produção, não entra.
- Todo texto passa pela skill humanizer antes de publicar.

## 6. Visual

- **Prints reais em vez de mockup desenhado.** Criar uma org de demonstração com dados fictícios coerentes (uma pessoa, dois bancos, um cartão, um financiamento, uma carteira) e capturar as telas em 2x, nos dois tamanhos, computador e celular. Os prints vão em WebP ou AVIF, com `width` e `height` declarados.
- **Marca:** coral na linha Personal, indigo como apoio e o anel do logo como elemento gráfico. Não usar a estética Mintlify (verde-menta, gradiente céu, botões pílula), porque ela já foi rejeitada.
- **Tipografia:** Inter no corpo. Fonte de título própria é decisão de marca (ver pendência P7).
- **Ritmo:**
  - Um fundo só.
  - Seções separadas por espaço, sem faixas alternadas.
  - Nada de rótulo em caixa alta acima dos títulos.
- **Movimento:** um só, a entrada suave do print do hero. Respeitar `prefers-reduced-motion`.
- **Acessibilidade:** contraste AA (o coral do botão já está em `#C2453A`), foco visível e texto alternativo descritivo nos prints.

## 7. Técnica

- **HTML estático gerado por `src/build.py`**, como hoje, sem framework.
- **Desempenho:** LCP abaixo de 2,5 s no 4G.
  - CSS abaixo de 30 KB.
  - Print do hero com `fetchpriority="high"`; os demais com `loading="lazy"`.
- **SEO:**
  - `title` e `description` com "controle financeiro", "Open Finance" e "app de finanças".
  - JSON-LD `SoftwareApplication` com `offers` nos dois planos.
  - Favicon, que ainda falta.
- **Cache:** manter a versão no link do CSS (`?v=hash`).

## 8. Medição

- Instalar analytics. O README já aponta essa falta, e a opção mais simples é o Vercel Web Analytics.
- Registrar o clique em cada CTA com a seção de origem (`hero`, `passos`, `planos`, `final`), mais a profundidade de rolagem.
- Repassar os UTMs para o link de cadastro, para medir a conversão por campanha.
- Fazer um teste A/B só depois de ter volume. O primeiro candidato é o título do hero.

## 9. Fora do escopo

- Página de empresas, além de tirar o seletor do topo.
- Blog, conteúdo e comparadores de cartão (o modelo Mobills).
- Agendamento de demonstração.
- Páginas por dor (o modelo YNAB) ficam para uma fase 2, quando houver tráfego pago.

## 10. Pendências que dependem de você

| # | Pergunta | Por que importa |
|---|---|---|
| P1 | Quais bancos funcionam de verdade pelo Open Finance hoje? | A faixa de logos e a pergunta 1 do FAQ. O Itaucard tem a falha de DCR na Polp. |
| P2 | Existem depoimentos, número de usuários ou nota nas lojas? | Sem isso, a seção 4.6 não entra e a faixa de confiança fica só com Open Finance e LGPD. |
| P3 | O cancelamento é pelo portal do Stripe, a qualquer momento? Há reembolso? | A linha "cancele quando quiser" e a pergunta 4 do FAQ. |
| P4 | O floow é só leitura no Open Finance, sem iniciação de pagamento? | A promessa "não mexe no seu dinheiro". |
| P5 | Quanto tempo leva, medido, do cadastro até ver o mês organizado? | A frase de tempo na seção 4.3. Sem medição, ela não entra. |
| P6 | "Consultor financeiro" ou outro nome, como "assistente financeiro"? | Risco de confusão com a atividade regulada pela CVM. |
| P7 | Fonte de título própria ou só Inter? | Identidade visual. |
| P8 | Posso criar a org de demonstração e capturar os prints? | Sem prints reais, o hero e os recursos voltam a ser mockup. |
| P9 | Os termos de uso do Nankin servem, ou vai haver um termo próprio do floow? | Hoje o link do rodapé abre um PDF que fala de arquitetura. |
| P10 | Qual o título do hero (opção 1, 2 ou 3 da seção 4.1)? | É a frase mais lida da página. |

## 11. Ordem de execução

1. Responder as pendências P1, P3, P4, P6 e P10. Sem elas, a página promete o que não pode.
2. Criar a org de demonstração e capturar os prints (P8).
3. Montar a página na ordem da seção 4, ainda sem a seção de prova social.
4. Revisar com humanizer e Impeccable (audit e polish) e conferir em 1440 px e 390 px.
5. Instalar o analytics e publicar.
6. Coletar os depoimentos e incluir a seção 4.6.
