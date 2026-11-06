"""Corpo da página Personal (index.html), na estrutura de docs/spec-landing.md.

Os prints do app ficam em dist/img/<nome>.webp. Enquanto um print não existe,
a página mostra uma moldura vazia com o nome dele, para a revisão local.
"""
import os

SIGNUP = "https://app.floowapp.com.br/auth?tab=signup"
LOGIN = "https://app.floowapp.com.br/dashboard"
IMG_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "dist", "img")

PRINTS = {
    "hero": "Dashboard do floow no computador: saldo, gastos do mês por categoria, fatura e próximos vencimentos",
    "consultor": "Consultor Financeiro do floow com as análises do dia",
    "visao-geral": "Dashboard com o fluxo de caixa dos últimos meses e o saldo de cada conta",
    "cartao": "Fatura do cartão por fechamento, com parcelas futuras",
    "dividas": "Controle de dívidas com quanto já foi pago e quanto falta",
    "patrimonio": "Carteira de investimentos e bens somados no patrimônio",
    "ritmo": "Ritmo de gastos com a projeção de onde o mês fecha",
}


def shot(nome, cls=""):
    alt = PRINTS[nome]
    for ext in ("webp", "png"):
        if os.path.exists(os.path.join(IMG_DIR, f"{nome}.{ext}")):
            eager = 'fetchpriority="high"' if nome == "hero" else 'loading="lazy"'
            return f'<img class="shot {cls}" src="img/{nome}.{ext}" alt="{alt}" {eager} decoding="async">'
    # shortcut: moldura vazia só serve para revisar local; não publicar sem os prints
    return f'<div class="shot shot-empty {cls}" role="img" aria-label="{alt}"><span>print: {nome}</span></div>'


def faltando():
    return [n for n in PRINTS if not any(os.path.exists(os.path.join(IMG_DIR, f"{n}.{e}")) for e in ("webp", "png"))]


def nav(logo):
    links = "".join(f'<a href="#{h}">{t}</a>' for h, t in
                    (("como", "Como funciona"), ("recursos", "Recursos"), ("planos", "Planos"), ("seguranca", "Segurança")))
    return f'''<header class="nav"><div class="wrap">
  <a href="#topo" class="nav-logo">{logo}</a>
  <nav class="nav-links" aria-label="Seções">{links}</nav>
  <div class="nav-end"><a class="nav-login" href="{LOGIN}">Entrar</a><a class="btn btn-primary btn-sm" href="{SIGNUP}">Começar grátis</a></div>
</div></header>'''


CHECK = '<svg aria-hidden="true" viewBox="0 0 24 24"><path d="M20 6 9 17l-5-5"/></svg>'


def hero(chat):
    selos = ["Conexão pelo Open Finance, regulado pelo Banco Central",
             "Só leitura: o floow não movimenta o seu dinheiro",
             "Seus dados não são vendidos"]
    return f'''<section class="hero"><div class="wrap">
  <div class="hero-top">
  <div class="hero-copy">
    <h1>Saiba para onde vai <em>cada real</em>, sem lançar nada à mão.</h1>
    <p class="lead">Conecte seus bancos pelo Open Finance e o floow importa os lançamentos, separa cada gasto por categoria e avisa no WhatsApp o que vem a seguir.</p>
    <div class="hero-ctas"><a class="btn btn-primary" href="{SIGNUP}">Começar grátis</a><a class="btn btn-ghost" href="#como">Ver como funciona</a></div>
    <p class="hero-note">30 dias do Pro grátis, sem cartão de crédito.</p>
  </div>
  <div class="hero-chat">{chat("WhatsApp", [
      ('A fatura do cartão fecha amanhã. Total de <b class="num">R$ 1.842,30</b>, vence dia 10.', "08:02"),
      ('Ritmo de outubro: <b class="num">R$ 5.171,16</b> de <b class="num">R$ 5.970,00</b> planejados. O mês fechou 13% abaixo do teto.', "08:02"),
      ("Quanto gastei em Alimentação em outubro?", "19:40", True),
      ('<b class="num">R$ 496,59</b>, 13% a mais que em setembro. Em novembro você está em <b class="num">R$ 58,84</b> de R$ 400,00.', "19:40"),
  ], "Exemplo de avisos e respostas do floow no WhatsApp")}</div>
  </div>
  <div class="hero-visual">{shot("hero", "shot-desktop")}</div>
  <ul class="trust">{"".join(f"<li>{CHECK}{s}</li>" for s in selos)}</ul>
</div></section>'''


def dores():
    itens = [("O salário entra e some.", "Cada gasto entra com categoria, e o resumo do mês mostra para onde foi o dinheiro."),
             ("A fatura sempre assusta.", "O total de cada fechamento e as parcelas que ainda vêm aparecem antes do vencimento."),
             ("Perdi a conta das parcelas e dos empréstimos.", "Cada dívida mostra quanto já foi pago e quanto falta, com os parcelados do cartão incluídos."),
             ("Meus investimentos estão em vários bancos.", "A carteira e os seus bens aparecem somados, num patrimônio só.")]
    cards = "".join(f'<div class="dor"><p class="dor-q">“{q}”</p><p>{a}</p></div>' for q, a in itens)
    return f'''<section class="block" id="dores"><div class="wrap">
  <div class="sec-head"><h2>Alguma dessas frases é sua?</h2></div>
  <div class="dores">{cards}</div>
</div></section>'''


def passos():
    itens = [("1", "Conecte", "Autorize seus bancos pelo Open Finance, direto no app do banco. Prefere arquivo? Importe o extrato em OFX ou CSV."),
             ("2", "O floow organiza", "Os lançamentos chegam categorizados. Você corrige uma vez e a regra vale para os próximos parecidos."),
             ("3", "Acompanhe e pergunte", "Os avisos chegam no WhatsApp, e o consultor financeiro de IA responde com os seus números.")]
    cols = "".join(f'<div class="passo"><span class="passo-n num">{n}</span><h3>{t}</h3><p>{d}</p></div>'
                   for n, t, d in itens)
    return f'''<section class="block" id="como"><div class="wrap">
  <div class="sec-head"><h2>Três passos e o mês se organiza sozinho.</h2></div>
  <div class="passos">{cols}</div>
  <div class="sec-cta"><a class="btn btn-primary" href="{SIGNUP}">Começar grátis</a><span>30 dias do Pro, sem cartão de crédito.</span></div>
</div></section>'''


def recursos():
    itens = [("visao-geral", "Você sabe quanto tem e quanto ainda vai sair.",
              "O saldo de cada conta e cartão ao lado do que entrou e saiu nos últimos meses, na mesma tela."),
             ("cartao", "A fatura deixa de ser surpresa.",
              "Cada fechamento mostra o total do mês, e as compras parceladas aparecem nas faturas que ainda vêm."),
             ("dividas", "Empréstimo, financiamento e parcelado, com quanto falta.",
              "Valor total, parcela, juros e quanto já foi pago em cada dívida. Os parcelados do cartão entram sem você cadastrar."),
             ("patrimonio", "Investimentos e bens somados num patrimônio só.",
              "Compras, vendas, dividendos e juros na carteira, ao lado de imóveis e veículos. Pelo Open Finance, as posições do banco chegam sozinhas."),
             ("ritmo", "Você vê onde o mês vai fechar antes de ele fechar.",
              "O ritmo de gastos compara com o seu plano e avisa quando uma categoria está para estourar.")]
    blocos = "".join(f'<div class="recurso{" rev" if i % 2 else ""}"><div class="recurso-copy"><h3>{t}</h3><p>{d}</p></div>{shot(img, "shot-feature")}</div>'
                     for i, (img, t, d) in enumerate(itens))
    return f'''<section class="block" id="recursos"><div class="wrap">
  <div class="sec-head"><h2>Conta, cartão, dívidas e investimentos no mesmo app.</h2></div>
  <div class="recursos">{blocos}</div>
</div></section>'''


def consultor():
    pontos = [("Análises todo dia", "Gastos fora do padrão, metas em risco e oportunidades, a partir dos seus dados."),
              ("Resposta com os seus números", "Pergunte quanto sobrou no mês ou se dá para antecipar uma meta. A resposta começa pelo número."),
              ("Nada sem você", "Quando o consultor sugere uma ação, ela só acontece depois que você confirma.")]
    li = "".join(f"<li><strong>{t}</strong><span>{d}</span></li>" for t, d in pontos)
    return f'''<section class="block" id="consultor"><div class="wrap">
  <div class="sec-head"><h2>Pergunte ao seu consultor financeiro.</h2><p>O consultor é uma inteligência artificial que lê as suas contas. Ele responde no app ou no WhatsApp e, todo dia, aponta o que mudou.</p></div>
  {shot("consultor", "shot-wide")}
  <ul class="pontos pontos-3">{li}</ul>
</div></section>'''


def brl(v):
    return f"{v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def planos():
    free = ["Até 2 contas", "Lançamentos manuais", "Dashboard e fluxo de caixa"]
    pro = ["Contas ilimitadas", "Open Finance e importação de OFX/CSV", "Investimentos",
           "Planejamento e independência financeira", "Suporte prioritário"]
    li = lambda xs: "".join(f"<li>{CHECK}{x}</li>" for x in xs)
    return f'''<section class="block" id="planos"><div class="wrap">
  <div class="sec-head"><h2>Comece grátis. Assine quando fizer sentido.</h2><p>Toda conta nova começa com 30 dias do Pro, sem cartão de crédito.</p></div>
  <div class="plans">
    <div class="plan"><h3>Free</h3><p class="price"><b class="num">R$ 0</b></p><p class="plan-sub">Controle financeiro básico.</p>
      <ul>{li(free)}</ul><a class="btn btn-ghost" href="{SIGNUP}">Criar conta grátis</a></div>
    <div class="plan pro"><h3>Pro</h3><p class="price"><b class="num">R$ 49,90</b><span>/mês</span></p>
      <p class="plan-sub">Gestão financeira completa, com cobrança mensal.</p>
      <ul>{li(pro)}</ul><a class="btn btn-primary" href="{SIGNUP}">Testar o Pro grátis por 30 dias</a></div>
  </div>
  <p class="plans-note">Cancele quando quiser, na tela de planos do app. Se você não assinar, a conta passa para o Free no fim dos 30 dias.</p>
</div></section>'''


def seguranca():
    itens = [("Você autoriza no seu banco", "A conexão pelo Open Finance é aprovada no app do banco, e você encerra quando quiser."),
             ("Só leitura", "O floow vê saldos e lançamentos. Ele não faz pagamentos nem transferências."),
             ("Criptografia", "Seus dados trafegam e ficam guardados com criptografia."),
             ("Sem venda de dados", "O floow segue a LGPD e não vende os seus dados.")]
    cols = "".join(f"<div><h3>{t}</h3><p>{d}</p></div>" for t, d in itens)
    return f'''<section class="block" id="seguranca"><div class="wrap">
  <div class="sec-head"><h2>Como o floow protege os seus dados.</h2></div>
  <div class="safe safe-4">{cols}</div>
</div></section>'''


FAQ = [
    ("Meu banco funciona?", "O floow conecta pelo Open Finance com os bancos que participam do sistema regulado pelo Banco Central. Se o seu banco não aparecer na hora de conectar, dá para importar o extrato em OFX ou CSV."),
    ("O floow mexe no meu dinheiro?", "Não. A conexão pelo Open Finance é só de leitura: o floow vê saldos e lançamentos, mas não faz pagamentos nem transferências."),
    ("O que acontece depois dos 30 dias?", "Se você não assinar o Pro, a conta passa para o Free: até 2 contas e lançamentos manuais, sem importação, Open Finance, investimentos ou planejamento."),
    ("Posso cancelar quando quiser?", "Pode. A assinatura é cancelada na tela de planos do app, a qualquer momento."),
    ("Preciso lançar tudo à mão?", "Não. Pelo Open Finance os lançamentos entram sozinhos e já categorizados. Você corrige uma categoria quando quiser, e a correção vale para os próximos parecidos."),
    ("Como funcionam os avisos no WhatsApp?", "Você autoriza o seu número na conta floow e passa a receber o resumo de ritmo e os avisos de vencimento. Dá para desligar a qualquer momento."),
    ("O consultor de IA é um consultor de verdade?", "É uma inteligência artificial que lê os seus dados no floow. Ela explica gastos, aponta o que mudou e responde perguntas, mas não substitui um profissional certificado nem faz recomendação de investimento."),
    ("Tem app para celular?", "O floow funciona no navegador, no computador e no celular, sem instalar nada."),
]


def final():
    return f'''<section class="block" id="comecar"><div class="wrap final">
  <h2>Respire. O floow cuida do resto.</h2>
  <p>Crie sua conta em poucos minutos e veja o seu mês organizado.</p>
  <a class="btn btn-primary" href="{SIGNUP}">Começar grátis</a>
  <span class="hero-note">30 dias do Pro grátis, sem cartão de crédito.</span>
</div></section>'''


def pagina(logo, chat, faq, footer):
    return f'''{nav(logo)}
<main>
{hero(chat)}
{dores()}
{passos()}
{recursos()}
{consultor()}
{planos()}
{seguranca()}
<section class="block" id="perguntas"><div class="wrap">
  <div class="sec-head"><h2>Perguntas frequentes</h2></div>
  {faq(FAQ)}
</div></section>
{final()}
</main>
{footer}'''


if __name__ == "__main__":
    html = pagina("<span>logo</span>", lambda *a, **k: "<div>chat</div>", lambda f: "<div>faq</div>", "<footer></footer>")
    for sec in ("dores", "como", "recursos", "consultor", "planos", "seguranca", "perguntas", "comecar"):
        assert f'id="{sec}"' in html, sec
    assert html.count(SIGNUP) == 6 and "R$ 49,90" in html and len(FAQ) == 8
    print("ok · prints faltando:", ", ".join(faltando()) or "nenhum")
