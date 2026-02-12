import base64
from io import BytesIO
import qrcode
from . import public_bp
from app.utils.pix import gerar_payload_pix
from flask import render_template, abort, redirect, url_for, flash, request

@public_bp.get("/")
def home():
    ong = get_ong()


    animais = [
        {"nome": "Mel", "status": "Em tratamento", "foto": "img/animais/ariel.jpg", "tipo": "Cão"},
        {"nome": "Jade", "status": "Para adoção", "foto": "img/animais/azeitona.jpg", "tipo": "Cão"},
        {"nome": "Pretinha", "status": "Resgatada", "foto": "img/animais/bebel.jpg", "tipo": "Cão"},
        {"nome": "Thor", "status": "Para adoção", "foto": "img/animais/benjamin.jpg", "tipo": "Cão"},
    ]

    instagram_posts = [
        {
            "url": "https://www.instagram.com/p/DUDz_FLksop/",
            "thumb": "img/insta/post1.jpeg",
            "titulo": "Campanha Apadrinhamento"
        },
        {
            "url": "https://www.instagram.com/p/DUDsOPSkrEc/",
            "thumb": "img/insta/post2.jpeg",
            "titulo": "Resgate da semana"
        },
        {
            "url": "https://www.instagram.com/p/DQjUVBGgOyH/",
            "thumb": "img/insta/reel1.jpeg",
            "titulo": "Bastidores do abrigo"
        },
        {
            "url": "https://www.instagram.com/p/DTOsu4nicIC/",
            "thumb": "img/insta/post3.png",
            "titulo": "Precisamos de ração"
        },
    ]

    return render_template(
        "public/home.html",
        ong=ong,
        animais=animais,
        instagram_posts=instagram_posts
    )

@public_bp.post("/contato")
def contato_post():
    nome = request.form.get("nome")
    email = request.form.get("email")

    if not nome or not email:
        flash("Preencha todos os campos obrigatórios.", "warning")
        return redirect(url_for("public.contato"))

    # aqui você processa/salva/envia email
    flash("Em breve entraremos em contato 💛", "success")
    return redirect(url_for("public.contato"))

@public_bp.get("/como-ajudar")
def como_ajudar():
    return render_template("public/como_ajudar.html")

@public_bp.get("/contato")
def contato():
    return render_template("public/contato.html")

@public_bp.get("/doacao")
def doacao():
    chave_pix = "18.294.547/0001-02"  # CNPJ
    payload = gerar_payload_pix(
        chave=chave_pix,
        nome="Lar da Regina",
        cidade="Guarulhos",
        valor=None  # pode deixar None pra doação livre
    )

    img = qrcode.make(payload)
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    qr_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")
   
    flash("Doação realizada com sucesso! Obrigado 💛", "success")
    
    return render_template("public/doacao.html", pix=chave_pix, qr_base64=qr_base64, payload=payload)

@public_bp.app_context_processor
def inject_ong():
    return {
        "ong": {
            "nome": "Lar da Regina",
            "pix": "18.294.547/0001-02",
            "instagram": "@lardaregina",
            "whatsapp": "5511976187227"
        }
    }


@public_bp.get("/transparencia")
def transparencia():
    relatorios = [
        {
            "mes": "Janeiro/2026",
            "resumo": "Entradas e saídas do mês, com comprovantes principais.",
            "arquivo": "prestacao_2026_01.pdf",
        },
        {
            "mes": "Fevereiro/2026",
            "resumo": "Gastos com ração, clínica e manutenção do espaço.",
            "arquivo": "prestacao_2026_02.pdf",
        },
    ]
    return render_template("public/transparencia.html", relatorios=relatorios)

@public_bp.get("/adote")
def adote():
    ong = get_ong()

    # depois você liga no banco; por enquanto, lista fixa
    animais = [
        {"nome": "Mel", "status": "Em tratamento", "foto": "img/animais/ariel.jpg", "tipo": "Cão"},
        {"nome": "Jade", "status": "Para adoção", "foto": "img/animais/azeitona.jpg", "tipo": "Cão"},
        {"nome": "Pretinha", "status": "Resgatada", "foto": "img/animais/bebel.jpg", "tipo": "Cão"},
        {"nome": "Thor", "status": "Para adoção", "foto": "img/animais/benjamin.jpg", "tipo": "Cão"},
    ]

    checklist = [
        "Ser maior de 18 anos (ou responsável legal)",
        "Ter tempo e condições para cuidar do animal",
        "Casa com ambiente seguro (telas/portões quando necessário)",
        "Compromisso com vacinação, vermifugação e cuidados veterinários",
        "Compromisso com castração (se aplicável) e adoção responsável",
        "Aceitar entrevista/triagem e acompanhamento pós-adoção",
    ]

    return render_template("public/adote.html", ong=ong, animais=animais, checklist=checklist)

def get_ong():
    return {
        "nome": "Lar da Regina",
        "pix": "18.294.547/0001-02",
        "instagram": "@lardaregina",
        "whatsapp": "5511976187227"
    }
    
def get_animais_apadrinhamento():
    base = {
        "tipo": "Cão",
        "sexo": "Não informado",
        "porte": "M",
        "idade": "Até 5 anos",
        "status": "Apadrinhamento",
        "descricao": "Em breve vamos colocar a história completa aqui.",
        "custos": [
            "Ração e alimentação",
            "Medicamentos e cuidados",
            "Veterinário e exames",
        ],
        "total": "R$ —/mês",
        "desde": "—",
        "raca": "Sem raça definida",
        "galeria": [],
    }

    animais = [
        {
            **base,
            "slug": "stelar",
            "nome": "Stelar",
            "sexo": "Fêmea",
            "porte": "G",
            "foto": "img/animais/stelar.jpg",
            "galeria": [
                "img/animais/stelar.jpg",
                "img/animais/stelar2.jpg",
                "img/animais/stelar3.jpg",
            ],
            "descricao": "Oi, eu sou a Stelar... (história resumida)",
            "custos": [
                "Equipe veterinária: R$ 60,00/mês",
                "Banho: R$ 30,00/mês",
                "Antipulgas: R$ 100,00/mês",
                "Fisioterapia: R$ 120,00/mês",
            ],
            "total": "R$ 316,70/mês",
            "desde": "15/11/2024",
            "raca": "Pitbull",
        },

        {**base, "slug":"ariel", "nome":"Ariel", "foto":"img/animais/ariel.jpg"},
        {**base, "slug":"azeitona", "nome":"Azeitona", "foto":"img/animais/azeitona.jpg"},
        {**base, "slug":"bebel", "nome":"Bebel", "foto":"img/animais/bebel.jpg"},
        {**base, "slug":"benjamin", "nome":"Benjamin", "foto":"img/animais/benjamin.jpg"},
        {**base, "slug":"bento-junior", "nome":"Bento Junior", "foto":"img/animais/bento_junior.jpg"},
        {**base, "slug":"bruce", "nome":"Bruce", "foto":"img/animais/bruce.jpg"},
        {**base, "slug":"camela", "nome":"Camela", "foto":"img/animais/camela.jpg"},
        {**base, "slug":"cristal", "nome":"Cristal", "foto":"img/animais/cristal.jpg"},
        {**base, "slug":"daisy", "nome":"Daisy", "foto":"img/animais/daisy.jpg"},
        {**base, "slug":"doguinho", "nome":"Doguinho", "foto":"img/animais/doguinho.jpg"},
        {**base, "slug":"dominique", "nome":"Dominique", "foto":"img/animais/dominique.jpg"},
        {**base, "slug":"dylan", "nome":"Dylan", "foto":"img/animais/dylan.jpg"},
        {**base, "slug":"jubileu", "nome":"Jubileu", "foto":"img/animais/jubileu.jpg"},
        {**base, "slug":"julinha", "nome":"Julinha", "foto":"img/animais/julinha.jpg"},
        {**base, "slug":"junior-sorriso", "nome":"Junior Sorriso", "foto":"img/animais/junior_sorriso.jpg"},
        {**base, "slug":"lola", "nome":"Lola", "foto":"img/animais/lola.jpg"},
        {**base, "slug":"luck", "nome":"Luck", "foto":"img/animais/luck.jpg"},
        {**base, "slug":"milk", "nome":"Milk", "foto":"img/animais/milk.jpg"},
        {**base, "slug":"princesa", "nome":"Princesa", "foto":"img/animais/princesa.jpg"},
        {**base, "slug":"romeu", "nome":"Romeu", "foto":"img/animais/romeu.jpg"},
        {**base, "slug":"simba", "nome":"Simba", "foto":"img/animais/simba.jpg"},
        {**base, "slug":"tirolez", "nome":"Tirolez", "foto":"img/animais/tirolez.jpg"},
    ]

    return animais


@public_bp.get("/apadrinhamento")
def apadrinhamento_lista():
    ong = get_ong()
    animais = get_animais_apadrinhamento()
    return render_template("public/apadrinhamento_lista.html", ong=ong, animais=animais)

@public_bp.post("/apadrinhamento/form")
def apadrinhamento_form():
    # pega dados do form
    data = {
        "nome": request.form.get("nome"),
        "email": request.form.get("email"),
        "telefone": request.form.get("telefone"),
        "endereco": request.form.get("endereco"),
        "cidade_estado": request.form.get("cidade_estado"),
        "animais": request.form.get("animais"),
        "valor": request.form.get("valor"),
        "dia_doacao": request.form.get("dia_doacao"),
        "pagamento": request.form.get("pagamento"),
        "periodo": request.form.get("periodo"),
        "comentarios": request.form.get("comentarios"),
    }

    # por enquanto: só confirma
    # (depois a gente salva em banco, planilha, ou manda email)
    flash("✅ Obrigado! Recebemos seu pedido de apadrinhamento. Em breve entraremos em contato.", "success")
    return redirect(url_for("public.apadrinhamento_lista"))

@public_bp.get("/apadrinhamento/<slug>")
def apadrinhamento_detalhe(slug):
    ong = get_ong()
    animais = get_animais_apadrinhamento()

    animal = next((a for a in animais if a["slug"] == slug), None)
    if not animal:
        abort(404)

    sugestoes = [a for a in animais if a["slug"] != slug][:4]

    return render_template(
        "public/apadrinhamento_detalhe.html",
        ong=ong,
        animal=animal,
        sugestoes=sugestoes
    )


@public_bp.get("/bazar")
def bazar():
    return render_template("public/bazar.html")

@public_bp.get("/parceiros")
def parceiros():
    ong = get_ong()

    parceiros = [
        {"nome": "Cobasi", "logo": "img/parceiros/cobasi.png", "url": "https://www.cobasi.com.br/"},
        {"nome": "ENIAC", "logo": "img/parceiros/eniac.png", "url": None},
        {"nome": "Radar", "logo": "img/parceiros/radar.png", "url": None},
        {"nome": "ENIAC", "logo": "img/parceiros/colegio_bonvenuto.png", "url": None},
        {"nome": "ENIAC", "logo": "img/parceiros/colegio_geometria.png", "url": None},
        {"nome": "ENIAC", "logo": "img/parceiros/glasser.png", "url": None},
        {"nome": "ENIAC", "logo": "img/parceiros/hamburgueria_vira_latas.png", "url": None},
        {"nome": "ENIAC", "logo": "img/parceiros/eu_sou_bicho.png", "url": None},
        {"nome": "ENIAC", "logo": "img/parceiros/max_locomition.png", "url": None},
        {"nome": "ENIAC", "logo": "img/parceiros/premium.png", "url": None},
        {"nome": "ENIAC", "logo": "img/parceiros/triade.png", "url": None},
        {"nome": "ENIAC", "logo": "img/parceiros/belas_patas.png", "url": None},
        {"nome": "ENIAC", "logo": "img/parceiros/arca_h.png", "url": None},
        {"nome": "ENIAC", "logo": "img/parceiros/ampara.png", "url": None},


        
        
        # ... adicione os demais
    ]

    return render_template("public/parceiros.html", ong=ong, parceiros=parceiros)


@public_bp.get("/quem-somos")
def quem_somos():
    ong = get_ong()
    return render_template("public/quem_somos.html", ong=ong)

