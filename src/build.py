#!/usr/bin/env python3
"""Gera index.html (Personal) e empresas.html (Business) com partes compartilhadas."""
import os, sys
DEPLOY = "--deploy" in sys.argv
OUT = os.path.dirname(os.path.abspath(__file__))

RING_VB = 'viewBox="0.2 4.3 69 33.4"'
def logo(extra=""):
    return (f'<span class="logo {extra}" aria-label="floow"><span>fl</span>'
            f'<svg {RING_VB} aria-hidden="true"><circle cx="16.9" cy="21" r="12.6"/><circle cx="52.5" cy="21" r="12.6"/></svg><span>w</span></span>')

SPRITE = '''<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>
<symbol id="i-check" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></symbol>
<symbol id="i-repeat" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="m17 2 4 4-4 4"/><path d="M3 11v-1a4 4 0 0 1 4-4h14"/><path d="m7 22-4-4 4-4"/><path d="M21 13v1a4 4 0 0 1-4 4H3"/></symbol>
<symbol id="i-bell" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9"/><path d="M10.3 21a1.94 1.94 0 0 0 3.4 0"/></symbol>
<symbol id="i-pie" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M21.2 15.9A10 10 0 1 1 8 2.8"/><path d="M22 12A10 10 0 0 0 12 2v10z"/></symbol>
<symbol id="i-lock" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></symbol>
<symbol id="i-shield" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20 13c0 5-3.5 7.5-7.7 9a1 1 0 0 1-.6 0C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.2-2.7a1.2 1.2 0 0 1 1.6 0C14.5 3.8 17 5 19 5a1 1 0 0 1 1 1z"/><path d="m9 12 2 2 4-4"/></symbol>
<symbol id="i-toggle" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="6" width="20" height="12" rx="6"/><circle cx="16" cy="12" r="2.5"/></symbol>
<symbol id="i-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></symbol>
<symbol id="i-cal" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/></symbol>
<symbol id="i-wallet" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M19 7V4a1 1 0 0 0-1-1H5a2 2 0 0 0 0 4h15a1 1 0 0 1 1 1v4h-3a2 2 0 0 0 0 4h3a1 1 0 0 0 1-1v-2a1 1 0 0 0-1-1"/><path d="M3 5v14a2 2 0 0 0 2 2h15a1 1 0 0 0 1-1v-4"/></symbol>
<symbol id="i-in" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M17 7 7 17"/><path d="M17 17H7V7"/></symbol>
<symbol id="i-compare" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="18" cy="18" r="3"/><circle cx="6" cy="6" r="3"/><path d="M13 6h3a2 2 0 0 1 2 2v7"/><path d="M11 18H8a2 2 0 0 1-2-2V9"/></symbol>
<symbol id="i-chart" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M3 3v16a2 2 0 0 0 2 2h16"/><path d="m19 9-5 5-4-4-3 3"/></symbol>
<symbol id="i-receipt" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M4 2v20l2-1 2 1 2-1 2 1 2-1 2 1 2-1 2 1V2l-2 1-2-1-2 1-2-1-2 1-2-1-2 1Z"/><path d="M16 8h-6a2 2 0 1 0 0 4h4a2 2 0 1 1 0 4H8"/><path d="M12 17.5v-11"/></symbol>
</defs></svg>'''

def ic(name): return f'<svg aria-hidden="true"><use href="#i-{name}"/></svg>'

WOMAN = '''<svg class="woman" viewBox="0 0 400 420" role="img" aria-label="Mulher sentada em posição de meditação, de frente, com os olhos fechados">
  <ellipse cx="200" cy="398" rx="170" ry="14" fill="var(--mat)"/>
  <path d="M158 116 C156 72 244 72 242 116 L248 176 C232 188 168 188 152 176 Z" fill="var(--hair-c)"/>
  <path d="M146 206 C126 250 118 292 112 330" stroke="var(--skin)" stroke-width="21" stroke-linecap="round" fill="none"/>
  <path d="M254 206 C274 250 282 292 288 330" stroke="var(--skin)" stroke-width="21" stroke-linecap="round" fill="none"/>
  <rect x="189" y="146" width="22" height="34" rx="9" fill="var(--skin-shade)"/>
  <g class="chest">
    <path d="M200 172 C167 172 146 180 138 204 L158 306 L242 306 L262 204 C254 180 233 172 200 172 Z" fill="var(--top)"/>
    <path d="M184 173 Q200 194 216 173 Z" fill="var(--skin-shade)"/>
    <path d="M146 206 C138 226 134 240 131 256" stroke="var(--top)" stroke-width="25" stroke-linecap="round" fill="none"/>
    <path d="M254 206 C262 226 266 240 269 256" stroke="var(--top)" stroke-width="25" stroke-linecap="round" fill="none"/>
    <path d="M160 296 H240" stroke="var(--top-shade)" stroke-width="12" stroke-linecap="round"/>
  </g>
  <ellipse cx="200" cy="118" rx="30" ry="35" fill="var(--skin)"/>
  <path d="M168 120 C164 84 236 84 232 120 C228 101 214 92 200 92 C186 92 172 101 168 120 Z" fill="var(--hair-c)"/>
  <circle cx="200" cy="70" r="15" fill="var(--hair-c)"/>
  <path d="M181 123 Q187.5 128.5 194 123 M206 123 Q212.5 128.5 219 123" stroke="var(--hair-c)" stroke-width="2.3" stroke-linecap="round" fill="none"/>
  <path d="M194 139 Q200 143 206 139" stroke="#8A4B3A" stroke-width="2" stroke-linecap="round" fill="none"/>
  <circle cx="181" cy="133" r="5" fill="#E8574A" opacity=".18"/><circle cx="219" cy="133" r="5" fill="#E8574A" opacity=".18"/>
  <path d="M76 356 C76 320 140 300 200 307 C260 300 324 320 324 356 C324 386 262 398 200 394 C138 398 76 386 76 356 Z" fill="var(--pants)"/>
  <path d="M112 356 C150 342 250 342 288 356" stroke="var(--pants-fold)" stroke-width="3" fill="none" stroke-linecap="round"/>
  <path d="M200 312 V340" stroke="var(--pants-fold)" stroke-width="3" stroke-linecap="round"/>
  <ellipse cx="160" cy="358" rx="20" ry="8" transform="rotate(-8 160 358)" fill="var(--skin)"/>
  <ellipse cx="240" cy="358" rx="20" ry="8" transform="rotate(8 240 358)" fill="var(--skin)"/>
  <circle cx="110" cy="334" r="12" fill="var(--skin)"/><circle cx="290" cy="334" r="12" fill="var(--skin)"/>
  <circle cx="104" cy="330" r="4.2" fill="none" stroke="var(--skin-shade)" stroke-width="2"/><circle cx="296" cy="330" r="4.2" fill="none" stroke="var(--skin-shade)" stroke-width="2"/>
</svg>'''

RINGS = '''<svg class="rings" viewBox="0 0 500 510" aria-hidden="true">
  <circle class="r4" cx="250" cy="250" r="244"/>
  <circle class="r3" cx="250" cy="250" r="210"/>
  <circle class="r2" cx="250" cy="250" r="168"/>
  <circle class="r1" cx="250" cy="250" r="126"/>
</svg>'''

def hero_art(chips):
    c = "".join(f'<div class="chip {cls}"><span class="ico {tone}">{ic(icon)}</span><div>{body}</div></div>'
                for cls, tone, icon, body in chips)
    return f'''<div class="hero-art">
  <div class="disc"></div>{RINGS}{WOMAN}
  <span class="flow-label">Estado de flow</span>{c}
</div>'''

def head(title, desc, full):
    top = '<!doctype html>\n<html lang="pt-BR">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n' if full else ''
    return top + f'''<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap">
<link rel="stylesheet" href="{CSS}">
''' + ('<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}</style>\n</head>\n' if full else '')

APP_LOGIN = "https://app.floowapp.com.br/auth"
APP_SIGNUP = "https://app.floowapp.com.br/auth?tab=signup"

def nav(current, links, cta):
    you = 'aria-current="page"' if current == "p" else ''
    biz = 'aria-current="page"' if current == "b" else ''
    lk = "".join(f'<a href="#{h}">{t}</a>' for h, t in links)
    return f'''<header class="nav"><div class="wrap">
  <a href="{'#topo' if current=='p' else 'index.html'}" style="text-decoration:none">{logo("inst")}</a>
  <nav class="nav-links" aria-label="Seções">{lk}</nav>
  <div class="nav-end">
    <nav class="line-switch" aria-label="Escolha o floow">
      <a href="index.html" {you}>Para você</a><a href="empresas.html" {biz}>Para empresas <span class="soon">Em breve</span></a>
    </nav>
    {(f'<a class="nav-login" href="{APP_LOGIN}">Entrar</a><a class="btn btn-primary btn-sm" href="{APP_SIGNUP}">'+cta+'</a>') if cta else '<span class="btn btn-sm btn-disabled" aria-disabled="true">Em breve</span>'}
  </div>
</div></header>'''

def timeline(items):
    out = []
    for dot, when, title, text, tag in items:
        t = f'<span class="tl-tag">{tag}</span>' if tag else ''
        out.append(f'<div class="tl-item"><div class="tl-dot num">{dot}</div><div class="tl-when">{when}</div><h3>{title}</h3><p>{text}</p>{t}</div>')
    return '<div class="timeline">' + "".join(out) + '</div>'

def bullets(items):
    return '<ul class="bullets">' + "".join(
        f'<li><span class="ico">{ic(i)}</span><div><strong>{t}</strong><span>{d}</span></div></li>' for i, t, d in items) + '</ul>'

def chat(title, msgs):
    m = "".join(f'<div class="msg">{b}<time>{t}</time></div>' for b, t in msgs)
    return f'''<div class="chat" role="img" aria-label="Exemplo de mensagens do floow no WhatsApp">
  <div class="chat-top"><span class="chat-av"><svg {RING_VB}><circle cx="16.9" cy="21" r="12.6" stroke="var(--ring-2)"/><circle cx="52.5" cy="21" r="12.6" stroke="var(--ring-2)"/></svg></span>
  <div><b>floow</b><small>{title}</small></div></div>
  <div class="chat-body">{m}</div>
</div>'''

SAFE = f'''<div class="safe">
  <div>{ic("lock")}<h3>Dados criptografados</h3><p>Suas informações trafegam e ficam guardadas com criptografia.</p></div>
  <div>{ic("toggle")}<h3>Você decide o que conectar</h3><p>Conecte e desconecte contas quando quiser. Os avisos também desligam com um toque.</p></div>
  <div>{ic("shield")}<h3>Sem venda de dados</h3><p>O floow existe para organizar o seu dinheiro. Seus dados não são produto.</p></div>
</div>'''

def faq(items):
    return '<div class="faq">' + "".join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in items) + '</div>'

def cta_final(h, p, primary, secondary, sec_href, cross_q, cross_link, cross_href):
    return f'''<section class="block tight" id="comecar"><div class="wrap">
  <div class="cta-final">
    <div><h2>{h}</h2><p>{p}</p></div>
    <div class="ctas">{(f'<a class="btn btn-primary" href="{APP_SIGNUP}">'+primary+'</a>') if primary else '<span class="btn btn-disabled" aria-disabled="true">Em breve</span>'}<a class="btn btn-ghost" href="{sec_href}">{secondary}</a></div>
  </div>
  <div class="cross"><p>{cross_q}</p><a href="{cross_href}">{cross_link} {ic("arrow")}</a></div>
</div></section>'''

def footer(current):
    return f'''<footer><div class="wrap">
  {logo("inst")}
  <nav aria-label="Rodapé"><a href="index.html">Para você</a><a href="empresas.html">Para empresas <span class="soon">Em breve</span></a><a href="#seguranca">Segurança</a><a href="#perguntas">Perguntas</a></nav>
  <div class="legal"><span>© 2026 floow · Limm Consultoria Ltda</span><span>floowapp.com.br</span></div>
</div></footer>'''

# ---------------------------------------------------------------- PERSONAL
END_DOC = "</body>\n</html>" if DEPLOY else ""
def personal():
    cats = [("Casa", 2150.00, "var(--indigo)"), ("Mercado", 1184.20, "var(--coral)"),
            ("Lazer", 480.00, "var(--gold)"), ("Transporte", 316.90, "var(--teal)"), ("Assinaturas", 139.70, "#5B6B80")]
    mx = cats[0][1]
    brl = lambda v: f"{v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    cat_html = "".join(f'<div class="cat"><b>{n}</b><span class="v num">{brl(v)}</span><div class="bar"><i style="width:{v/mx*100:.1f}%;--c:{c}"></i></div></div>' for n, v, c in cats)
    total = sum(v for _, v, _ in cats)
    return f'''{head("floow para você", "floow: suas finanças no automático e você em estado de flow.", DEPLOY)}
{"<body>" if DEPLOY else ""}
<div class="personal" id="topo">
{SPRITE}
{nav("p", [("como","Como funciona"),("recursos","Recursos"),("avisos","Avisos"),("seguranca","Segurança"),("perguntas","Perguntas")], "Começar agora")}
<main>
<section class="hero"><div class="wrap">
  <div class="hero-copy">
    <span class="overline accent">floow · para você</span>
    <h1>Finanças no automático. Sua mente em <em>estado de flow</em>.</h1>
    <p class="lead">O floow organiza suas contas, separa cada gasto por categoria e avisa o que vem a seguir. Você respira tranquilo e sabe exatamente para onde vai o seu dinheiro.</p>
    <div class="hero-ctas"><a class="btn btn-primary" href="{APP_SIGNUP}">Começar agora {ic("arrow")}</a><a class="btn btn-ghost" href="#como">Ver como funciona</a></div>
    <div class="hero-notes"><span>{ic("check")}Categorização automática</span><span>{ic("check")}Avisos no WhatsApp</span><span>{ic("check")}Sem planilha</span></div>
  </div>
  {hero_art([
    ("c1","pos","check",'<strong>Conta de luz paga</strong><span class="num">No automático · R$ 186,40</span>'),
    ("c2","acc","pie",'Você gastou <strong style="display:inline" class="num">R$ 316,90</strong> em transporte neste mês.'),
    ("c3","warn","bell",'<strong>Fatura vence dia 10</strong>Avisamos 3 dias antes.'),
  ])}
</div></section>

<section class="block band" id="como"><div class="wrap">
  <div class="sec-head"><span class="overline accent">Como funciona</span><h2>Um mês inteiro rodando sozinho.</h2><p>Você segue a vida. O floow acompanha cada entrada e cada saída, e só chama sua atenção quando vale a pena.</p></div>
  {timeline([
    ("1","Dia 1","O salário entra","O floow reconhece a entrada e já separa o que tem destino certo: aluguel, contas fixas e assinaturas.","Automático"),
    ("5","Dia 5","Contas fixas em dia","Aluguel, luz e internet aparecem agendadas, com data e valor. Nada vence sem você saber.","Automático"),
    ("15","Dia 15","Aviso de ritmo","No meio do mês, chega no seu WhatsApp como estão os gastos em relação ao mês anterior.",""),
    ("30","Dia 30","Resumo do mês","Quanto entrou, quanto saiu e para onde foi. Um retrato simples, sem planilha.",""),
  ])}
</div></section>

<section class="block" id="recursos"><div class="wrap split">
  <div>
    <span class="overline accent">Clareza</span>
    <h2 style="margin-top:14px">Você sabe para onde vai cada real.</h2>
    <p class="lead" style="margin-top:16px">Tudo o que você gasta ganha nome e lugar. Sem digitar, sem categorizar na mão.</p>
    {bullets([
      ("pie","Categorias automáticas","Mercado, transporte, casa, lazer. Cada gasto encontra o seu lugar sozinho."),
      ("repeat","Recorrências sob controle","Assinaturas e contas fixas identificadas, com data e valor de cada mês."),
      ("wallet","Tudo em um só lugar","Contas e cartões juntos em uma visão, com o saldo sempre atualizado."),
    ])}
  </div>
  <div>
    <div class="phone" role="img" aria-label="Tela do floow no navegador do celular, com saldo e gastos de setembro por categoria">
      <div class="phone-screen">
        <div class="ph-browser"><span class="ph-aa">AA</span><div class="ph-url">{ic("lock")}<span>floowapp.com.br</span></div><span class="ph-reload">{ic("repeat")}</span></div><div class="ph-head">{logo()}</div>
        <div class="ph-card"><div class="ph-label">Saldo da Conta</div><div class="ph-big num">R$ 12.480,35</div><div class="ph-sub">+ 3,2% neste mês</div></div>
        <div class="ph-card"><div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:6px"><b style="color:var(--fg-1);font-size:14px">Setembro por categoria</b><span class="num" style="font-size:12px;color:var(--fg-3)">R$ {brl(total)}</span></div>{cat_html}</div>
        <div class="ph-card" style="display:flex;justify-content:space-between;align-items:center;font-size:13px"><div><b style="color:var(--fg-1);font-weight:500">Internet</b><div class="ph-label">Agendado · amanhã</div></div><span class="num" style="color:var(--fg-1);font-weight:600">− 119,90</span></div>
        <div class="example-tag">Dados de exemplo</div>
      </div>
      <div class="ph-toolbar" aria-hidden="true"><span>‹</span><span>›</span><span>□</span><span>⋯</span></div>
    </div>
  </div>
</div></section>

<section class="block band" id="avisos"><div class="wrap split rev">
  <div>
    <span class="overline accent">Avisos</span>
    <h2 style="margin-top:14px">O floow fala com você no WhatsApp.</h2>
    <p class="lead" style="margin-top:16px">Sem precisar abrir o floow. Um resumo curto no ritmo do seu mês e um aviso quando algo pede atenção.</p>
    {bullets([
      ("bell","Aviso de ritmo","Se os gastos de uma categoria aceleram, você fica sabendo antes do fim do mês."),
      ("cal","Vencimentos","Contas e faturas lembradas com antecedência, com valor e data."),
    ])}
  </div>
  <div>{chat("Avisos automáticos", [
      ('<b>Resumo de ritmo · semana 3</b><div class="kv num"><span>Gastos até agora</span><span>R$ 3.912,40</span><span>Ritmo do mês</span><span>Dentro do esperado</span><span>Maior categoria</span><span>Mercado</span></div>', "08:02"),
      ('Você gastou <b class="num">R$ 316,90</b> em transporte neste mês. É 12% a mais que em agosto.', "08:02"),
      ('A fatura do cartão vence dia 10. Total de <b class="num">R$ 1.842,30</b>. Avisamos de novo na véspera.', "09:15"),
  ])}</div>
</div></section>

<section class="block" id="seguranca"><div class="wrap">
  <div class="sec-head"><span class="overline accent">Segurança</span><h2>Tranquilidade começa pela confiança.</h2></div>
  {SAFE}
</div></section>

<section class="block band" id="perguntas"><div class="wrap">
  <div class="sec-head"><span class="overline accent">Perguntas</span><h2>O que as pessoas perguntam.</h2></div>
  {faq([
    ("Preciso preencher planilha?","Não. O floow organiza e categoriza os lançamentos sozinho. Você só ajusta uma categoria se quiser."),
    ("Como funcionam os avisos no WhatsApp?","Você autoriza o seu número na sua conta floow e passa a receber o resumo de ritmo e os avisos de vencimento. Dá para desligar a qualquer momento."),
    ("O floow vai me cobrar disciplina?","Não. Ele mostra o que aconteceu e o que vem a seguir. As decisões continuam sendo suas."),
    ('Tenho uma empresa. Posso usar o floow?','Em breve. O <a href="empresas.html" style="color:var(--accent-ink);font-weight:600">floow para empresas</a> vai ter fluxo de caixa, contas a pagar, recebíveis e conciliação em um painel só.'),
  ])}
</div></section>

{cta_final("Respire. O floow cuida do resto.", "Crie sua conta em poucos minutos e veja o seu mês organizado.", "Começar agora", "Ver como funciona", "#como",
           "Em breve: o caixa da sua empresa também no automático.", "Conheça o floow para empresas", "empresas.html")}
</main>
{footer("p")}
</div>
{END_DOC}'''

# ---------------------------------------------------------------- BUSINESS
def cash_chart():
    vals = [184,190,176,181,195,188,172,178,186,199,205,193,180,187,196,210,202,189,194,203,214,208,196,201,212,220,215,206,212,224]
    W, H, L, R, T, B = 560, 220, 44, 12, 14, 30
    ymin, ymax = 150, 240
    x = lambda i: L + i * (W - L - R) / (len(vals) - 1)
    y = lambda v: T + (ymax - v) * (H - T - B) / (ymax - ymin)
    pts = " ".join(f"{x(i):.1f},{y(v):.1f}" for i, v in enumerate(vals))
    area = f"M{x(0):.1f},{y(ymin):.1f} L" + " L".join(f"{x(i):.1f},{y(v):.1f}" for i, v in enumerate(vals)) + f" L{x(len(vals)-1):.1f},{y(ymin):.1f} Z"
    grid = "".join(f'<line x1="{L}" x2="{W-R}" y1="{y(g):.1f}" y2="{y(g):.1f}" stroke="var(--hair)" stroke-width="1"/><text x="{L-8}" y="{y(g)+4:.1f}" text-anchor="end" font-size="11" fill="var(--fg-3)">{g}k</text>' for g in (160, 190, 220))
    xl = "".join(f'<text x="{x(i):.1f}" y="{H-8}" text-anchor="{a}" font-size="11" fill="var(--fg-3)">{t}</text>' for i, t, a in ((0,"hoje","start"),(10,"+10 dias","middle"),(20,"+20 dias","middle"),(29,"+30 dias","end")))
    ex, ey = x(len(vals)-1), y(vals[-1])
    return f'''<svg viewBox="0 0 {W} {H}" role="img" aria-label="Projeção de caixa para 30 dias, de 184 mil hoje a 224 mil">
  <defs><linearGradient id="gA" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="var(--accent)" stop-opacity=".22"/><stop offset="1" stop-color="var(--accent)" stop-opacity="0"/></linearGradient></defs>
  {grid}<path d="{area}" fill="url(#gA)"/>
  <polyline points="{pts}" fill="none" stroke="var(--accent)" stroke-width="2.2" stroke-linejoin="round" stroke-linecap="round"/>
  <circle cx="{x(0):.1f}" cy="{y(vals[0]):.1f}" r="4" fill="var(--surface)" stroke="var(--accent)" stroke-width="2"/>
  <circle cx="{ex:.1f}" cy="{ey:.1f}" r="4.5" fill="var(--accent)"/>
  <text x="{ex-8:.1f}" y="{ey-10:.1f}" text-anchor="end" font-size="12" font-weight="600" fill="var(--fg-1)">224k</text>
  {xl}
</svg>'''

def business():
    return f'''{head("floow para empresas", "floow para empresas: o caixa da sua empresa no automático, com previsibilidade.", True)}
<body>
<div class="business" id="topo">
{SPRITE}
{nav("b", [("painel","Painel"),("rotina","Rotina"),("recursos","Recursos"),("seguranca","Segurança"),("perguntas","Perguntas")], "")}
<main>
<section class="hero"><div class="wrap">
  <div class="hero-copy">
    <span class="overline accent">floow · para empresas <span class="soon">Em breve</span></span>
    <h1>Finanças no automático. Sua mente em <em>estado de flow</em>.</h1>
    <p class="lead">Contas a pagar, recebíveis e conciliação rodando sozinhos. Você sabe hoje quanto entra, quanto sai e por quantos dias o caixa se sustenta.</p>
    <div class="hero-ctas"><span class="btn btn-disabled" aria-disabled="true">Em breve</span><a class="btn btn-ghost" href="index.html">Conhecer o floow para você</a></div>
    <p class="soon-note">O floow para empresas ainda não está aberto para cadastro ou login.</p>
    <div class="hero-notes"><span>{ic("check")}Conciliação automática</span><span>{ic("check")}Previsão de caixa</span><span>{ic("check")}Avisos no WhatsApp</span></div>
  </div>
  {hero_art([
    ("c1","pos","check",'<strong>Conciliação concluída</strong><span class="num">128 de 128 lançamentos</span>'),
    ("c2","acc","chart",'Seu caixa cobre <strong style="display:inline" class="num">47 dias</strong> no ritmo atual.'),
    ("c3","warn","bell",'<strong>Três boletos vencem sexta</strong><span class="num">Total de R$ 8.240,00</span>'),
  ])}
</div></section>

<section class="block band" id="painel"><div class="wrap">
  <div class="sec-head"><span class="overline accent">Previsibilidade</span><h2>Prazo, valor e consequência na mesma tela.</h2><p>O painel mostra o caixa de hoje, o que entra e sai nos próximos dias e até quando o saldo sustenta a operação.</p></div>
  <div class="dash">
    <div class="dash-top">{logo()}<a class="on" href="#painel">Fluxo de Caixa</a><a href="#recursos">Contas a Pagar</a><a href="#recursos">Recebíveis</a><a href="#recursos">Conciliação</a><span class="example-tag" style="margin-left:auto">Dados de exemplo</span></div>
    <div class="dash-body">
      <div class="kpis">
        <div class="kpi"><small>Caixa hoje</small><b class="num">R$ 184.200</b></div>
        <div class="kpi"><small>A receber · 7 dias</small><b class="num">R$ 62.900</b> <span class="d" style="color:var(--positive)">14 títulos</span></div>
        <div class="kpi"><small>A pagar · 7 dias</small><b class="num">R$ 41.380</b> <span class="d" style="color:var(--fg-3)">9 contas</span></div>
      </div>
      <div class="runway">{ic("chart")}<span>Seu caixa cobre <b class="num">47 dias</b> no ritmo atual.</span></div>
      <div class="split" style="gap:28px;grid-template-columns:1.35fr 1fr;align-items:start">
        <div class="chart"><div class="ph-label" style="margin-bottom:8px">Projeção de caixa · próximos 30 dias</div>{cash_chart()}</div>
        <div>
          <div class="ph-label" style="margin-bottom:4px">Contas a pagar · esta semana</div>
          <div class="tbl-wrap"><table>
            <thead><tr><th>Conta</th><th>Vence</th><th class="r">Valor</th><th>Status</th></tr></thead>
            <tbody class="num">
              <tr><td>Fornecedor Lima</td><td>Qui</td><td class="r">3.180,00</td><td><span class="pill pos">Agendado</span></td></tr>
              <tr><td>Aluguel</td><td>Sex</td><td class="r">4.200,00</td><td><span class="pill pos">Agendado</span></td></tr>
              <tr><td>Energia</td><td>Sex</td><td class="r">860,00</td><td><span class="pill warn">Aprovar</span></td></tr>
            </tbody>
          </table></div>
        </div>
      </div>
    </div>
  </div>
</div></section>

<section class="block" id="rotina"><div class="wrap">
  <div class="sec-head"><span class="overline accent">Rotina</span><h2>Uma semana de caixa sem sustos.</h2><p>O trabalho repetitivo roda sozinho. Você entra só para decidir.</p></div>
  {timeline([
    ("Seg","Segunda","Conciliação pronta","Os lançamentos do fim de semana chegam conciliados com o extrato. Você revisa só as exceções.","Automático"),
    ("Ter","Terça","Recebível confirmado","O cliente pagou o boleto. O floow baixa o título e atualiza a previsão de caixa.","Automático"),
    ("Qua","Quarta","Aviso de vencimentos","Três boletos vencem sexta. Total de R$ 8.240,00. Você decide com dois dias de folga.",""),
    ("Sex","Sexta","Pagamentos no horário","O que foi aprovado sai no vencimento. Sem multa e sem correria no fim do dia.","Automático"),
  ])}
</div></section>

<section class="block band" id="recursos"><div class="wrap">
  <div class="sec-head"><span class="overline accent">Recursos</span><h2>Quatro rotinas do financeiro, um lugar só.</h2></div>
  <div class="feat-grid">
    <div class="feat"><span class="ico">{ic("chart")}</span><h3>Fluxo de caixa</h3><p>Saldo de hoje e projeção dos próximos 30 dias, com base no que já está agendado.</p><div class="quote num">“Seu caixa cobre 47 dias no ritmo atual.”</div></div>
    <div class="feat"><span class="ico">{ic("receipt")}</span><h3>Contas a pagar</h3><p>Boletos e fornecedores organizados por vencimento, com aprovação e agendamento.</p><div class="quote num">“Três boletos vencem sexta. Total de R$ 8.240,00.”</div></div>
    <div class="feat"><span class="ico">{ic("in")}</span><h3>Recebíveis</h3><p>Quem vai pagar, quanto e quando. Títulos baixados sozinhos quando o dinheiro cai.</p><div class="quote num">“R$ 62.900,00 entram nos próximos 7 dias.”</div></div>
    <div class="feat"><span class="ico">{ic("compare")}</span><h3>Conciliação</h3><p>Extrato cruzado com o que foi lançado. O que bate é conciliado; o resto vira uma lista curta.</p><div class="quote num">“128 lançamentos conciliados hoje. 2 pedem revisão.”</div></div>
  </div>
</div></section>

<section class="block" id="avisos"><div class="wrap split">
  <div>
    <span class="overline accent">Avisos</span>
    <h2 style="margin-top:14px">O caixa do dia chega no seu WhatsApp.</h2>
    <p class="lead" style="margin-top:16px">Todo dia de manhã, os números que importam. E um aviso sempre que uma decisão depende de você.</p>
    {bullets([
      ("bell","Resumo diário","Caixa de hoje, o que entra e sai na semana e a cobertura em dias."),
      ("cal","Vencimentos e aprovações","Prazo, valor e o que acontece se nada for feito, na mesma mensagem."),
    ])}
  </div>
  <div>{chat("Avisos da empresa", [
      ('<b>Bom dia. Caixa hoje: <span class="num">R$ 184.200,00</span></b><div class="kv num"><span>A receber · 7 dias</span><span>62.900,00</span><span>A pagar · 7 dias</span><span>41.380,00</span><span>Cobertura</span><span>47 dias</span></div>', "07:30"),
      ('Três boletos vencem sexta. Total de <b class="num">R$ 8.240,00</b>.', "07:30"),
      ('A conta de energia (<span class="num">R$ 860,00</span>) aguarda sua aprovação para sair na sexta.', "10:12"),
  ])}</div>
</div></section>

<section class="block band" id="seguranca"><div class="wrap">
  <div class="sec-head"><span class="overline accent">Segurança</span><h2>O caixa da empresa em boas mãos.</h2></div>
  {SAFE}
</div></section>

<section class="block" id="perguntas"><div class="wrap">
  <div class="sec-head"><span class="overline accent">Perguntas</span><h2>O que as empresas perguntam.</h2></div>
  {faq([
    ("O que é cobertura de caixa?","É por quantos dias o saldo de hoje, somado ao que entra e descontado o que sai, sustenta a operação no ritmo atual."),
    ("Como funciona a conciliação automática?","O floow cruza os lançamentos do extrato com as contas a pagar e a receber. O que bate é conciliado sozinho; o que não bate vai para uma lista curta de revisão."),
    ("O floow substitui o meu contador?","Não. Ele organiza o caixa do dia a dia e entrega os dados conciliados, o que deixa o trabalho do contador mais rápido."),
    ('Já uso o floow pessoal. Preciso de outra conta?','A conta da empresa é separada, para o caixa da empresa não se misturar com o seu. Você pode ter as duas. <a href="index.html" style="color:var(--accent-ink);font-weight:600">Conheça o floow para você</a>.'),
  ])}
</div></section>

{cta_final("Caixa previsível. Cabeça tranquila.", "O floow para empresas chega em breve. Enquanto isso, organize as suas finanças pessoais.", None, "Conhecer o floow para você", "index.html",
           "Quer organizar também as suas finanças pessoais?", "Conheça o floow para você", "index.html")}
</main>
{footer("b")}
</div>
</body>
</html>'''

CSS = "floow.css" if DEPLOY else "floow-v4.css"
DEST = os.path.join(OUT, "dist") if DEPLOY else OUT
os.makedirs(DEST, exist_ok=True)
open(os.path.join(DEST, "index.html"), "w").write(personal())
open(os.path.join(DEST, "empresas.html"), "w").write(business())
if DEPLOY:
    import shutil; shutil.copy(os.path.join(OUT, "floow-v4.css"), os.path.join(DEST, "floow.css"))
print("ok")
