# Matching Brackets

def chk_brackets(item):
    open_list = ['(', '[', '{', '<']
    close_list = [')', ']', '}', '>']
    brkt_used = []
    result = 0
    open_b = []
    pos = 0

    for i in item:
        if i in open_list or i in close_list:
            brkt_used.append(i)
        else:
            continue

    if len(brkt_used) % 2 != 0:
        return 0
    else:
        for b in brkt_used:
            if b in open_list:
                open_b.append(b)
            elif b in close_list:
                pos = close_list.index(b)
                if ((len(open_b) > 0) and (open_list[pos] == open_b[len(open_b) - 1])):
                    open_b.pop()
                else:
                    return 0
    if open_b:
        result = 0
    else:
        result = 1
    return result

strings = ['[{<[z]h>[[^{c]y}(a)t]{ ]d}{a[e]}}[{/}[c]](b)', \
           '<>(/(d<%>)[[+] ][<([d]a{*})<a>[v](u(/)(z)(/))c)d]>', \
           '<<->d[f]<e>>( )(x<v>(v))(u{-}{ })(-)[<u<v>><g>]</(e)>( )', \
           '<(y)[(b)c]v{{x}a}{h}[c]>[c] ( (^))[y(g)]}<{( )c}a><[t]( )u>', \
           '< >{v}< [w][<d>(c){]>vw}<t>{}[*]{y}<c>(%)', \
           '{ }({(h)a]%][(+)x]<d>}{y}(<u>t)(x(%)[/[[{%}u])d{a})<>', \
           '[d]<u<[t]-(u)>><u>[(<y>-)-[(b<->)d]{+}]{(g)}<t>', \
           '(<t{(e)%}>{v})[ [x](^)]<x><^><(t) >[{{h}+<x{d}><<c>z><x>{a}}b]', \
           '{ }[w[<t>(v)^<b>]<-<->><d>]<->(x){{[y(x)(y)]b}}( <{h}v>)', \
           '(%<t>)([ {v}]<a(z[[*] ]c>[<c>[w]{t}(t)x]<{x} >)<%><(x)())g>(^)', \
           '([g](z){(b)z(z)}[t<z>(z)]<<*>^>/){^}<f><[v]>', \
           '({^}^<->){e}< (^)>{( )<[%]->/}<<h{+}>>({*[d]}/)', \
           '<b{ }<z>>(a)<[[<%}[b]{b< >{t{ }>(*)[c]}[<+>[b]u{t}] ]y]>[e]', \
           '[v]<w>{-}(<(z)c(a)>){^<c>}{-[(c)+<y>](t</>)<^>}[%](g)', \
           '( <({-}a[<b><b>-])[-]*>)<(a)><[e]g>[b]< >', \
           '{h}[( )({u}a[a][v]<*>)e]({z}[c](x) z{a}}(y)<^<e[w]>>(<t>v))', \
           '<u>[[x)c]({ }{w}<c>y(g)][t( (/{z}))]<<f>{(f){c}t[a]}(b)>(y)']
for char in strings:
    print(chk_brackets(char), end=' ')