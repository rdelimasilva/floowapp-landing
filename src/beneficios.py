"""Seção de benefícios da página Personal: cada recurso com um recorte da tela do app (dados de exemplo)."""


def _row(nome, sub, valor, tag=""):
    t = f'<span class="tag">{tag}</span>' if tag else ''
    return (f'<div class="row"><div><b>{nome}</b><small>{sub}</small></div>'
            f'<div class="row-end">{t}<span class="num">{valor}</span></div></div>')


def _tile(cls, demo, label, titulo, texto, kicker):
    return (f'<article class="tile {cls}"><div class="demo" role="img" aria-label="{label}">{demo}</div>'
            f'<div class="tile-copy"><h3>{titulo}</h3><p>{texto}</p><small>{kicker}</small></div></article>')


IMPORTACAO = ('<div class="demo-head"><span class="dot"></span>Open Finance · 3 lançamentos novos</div>'
              + _row("Supermercado", "Cartão final 4821", "− 184,20", "Mercado")
              + _row("Posto de combustível", "Cartão final 4821", "− 210,00", "Transporte")
              + _row("Salário", "Conta corrente", "+ 6.800,00", "Renda"))

REGRA = ('<div class="rule"><span class="chip-q">Descrição contém <b>POSTO</b></span>'
         '<svg aria-hidden="true" viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
         '<span class="chip-a">Transporte</span></div>'
         '<p class="demo-note">Regra criada uma vez. Vale para <b class="num">14</b> lançamentos parecidos.</p>'
         '<div class="bill"><span>Fatura · fecha dia 3</span><b class="num">R$ 1.842,30</b></div>')

DIVIDA = ('<div class="debt"><div><b>Financiamento do carro</b><small class="num">Parcela 1.240,00 · 23 de 60</small></div>'
          '<span class="num pct">38%</span></div>'
          '<div class="meter" aria-hidden="true"><i style="width:38%"></i></div>'
          '<div class="debt-foot num"><span>Pago 28.520,00</span><span>Falta 45.880,00</span></div>')

CARTEIRA = (_row("Renda fixa", "4 ativos", "48.200,00")
            + _row("Ações", "6 ativos", "12.900,00")
            + '<div class="income"><span>Proventos em setembro</span><b class="num">+ 312,40</b></div>')

PATRIMONIO = ('<div class="worth"><small>Patrimônio total</small><b class="num">R$ 612.400</b></div>'
              '<div class="stackbar" aria-hidden="true"><i style="flex:68"></i><i style="flex:12"></i><i style="flex:20"></i></div>'
              '<ul class="legend num"><li><i></i>Imóveis 420.000</li><li><i></i>Veículos 72.000</li><li><i></i>Investimentos 120.400</li></ul>')


def beneficios():
    tiles = [
        _tile("wide", IMPORTACAO, "Lançamentos importados do banco, já com categoria",
              "Contas e cartões importados",
              "Conecte o banco pelo Open Finance e os lançamentos da conta corrente e do cartão entram sozinhos. "
              "Prefere arquivo? Importe o extrato em OFX ou CSV, e o que já existe fica de fora.",
              "Open Finance · OFX · CSV"),
        _tile("wide", REGRA, "Regra de categoria aplicada a lançamentos parecidos e total da fatura",
              "Cada gasto na categoria certa",
              "Você classifica um lançamento uma vez e o floow aplica a mesma regra aos próximos parecidos. "
              "A fatura do cartão aparece com o total de cada fechamento.",
              "Conta corrente · cartão"),
        _tile("", DIVIDA, "Financiamento com 38% pago e parcelas restantes",
              "Dívidas sob controle",
              "Empréstimos e financiamentos com parcela, juros e quanto já foi pago. "
              "As compras parceladas no cartão entram sem você cadastrar.",
              "Empréstimos · financiamentos"),
        _tile("", CARTEIRA, "Carteira de investimentos por classe e proventos do mês",
              "Investimentos acompanhados",
              "Compras, vendas, dividendos, juros e amortizações na mesma carteira. "
              "Pelo Open Finance, as posições do banco chegam sem digitação.",
              "Carteira · proventos"),
        _tile("", PATRIMONIO, "Patrimônio total dividido entre imóveis, veículos e investimentos",
              "Patrimônio em uma visão",
              "Imóveis, veículos e outros bens ao lado do que você tem investido, "
              "para você ver a evolução do seu patrimônio.",
              "Imóveis · veículos · bens"),
    ]
    return '<div class="bento">' + "".join(tiles) + '</div><p class="example-tag bento-tag">Dados de exemplo</p>'


if __name__ == "__main__":
    html = beneficios()
    assert html.count('<article class="tile') == 5 and html.count('class="tile wide"') == 2
    print("ok")
