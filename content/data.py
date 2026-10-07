"""
Shared lists for the EMM site. Edit here, then run:  python3 build.py

Text that differs by language is written as {"es": "...", "en": "..."}.
"""
import json
from pathlib import Path

# ------------------------------------------------------------------ contact
ORG = {
    "name_es": "Excelencia en Administración Ministerial",
    "name_en": "Excellence Ministry Management",
    "short": "EMM",
    # former name, shown on the About page and home page so returning churches recognize us
    "former_es": "Red Nacional de Iglesias y Ministerios Cristianos",
    "former_en": "National Christian Churches & Ministries Network",
    "former_short": "NCCMN",
    # name on file with the IRS and the bank: used for checks and the copyright line.
    # CONFIRM: change this once the legal name change (or DBA) is filed.
    "legal_name": "National Christian Churches and Ministries Network, Inc.",
    "address": ["400 N New York Ave, Suite 105", "Winter Park, FL 32789"],
    "phone": "407-759-9003",
    "phone_href": "+14077599003",
    "fax": "321-445-9900",
    "email": "info@nccmn.org",
    "apply_email": "apply@nccmn.org",
    "give_url": "https://go.payinvoice.com/nccmn/",
}

LEADERS = [
    {"name": "Rafael González", "role": {"es": "Presidente", "en": "President"},
     "email": "rafael@nccmn.org"},
    {"name": "Manuel Collazo", "role": {"es": "Vicepresidente", "en": "Vice President"},
     "email": "manuel.collazo@nccmn.org"},
    {"name": "Rev. Dr. Pablo A. Jiménez", "role": {"es": "Formación ministerial", "en": "Ministerial formation"},
     "email": "revpablojimenez@nccmn.org"},
]

# ------------------------------------------------------------------ map (home page)
HQ = {"label": "Winter Park, FL", "lonlat": (-81.35, 28.60)}
MAP_PLACES = [
    {"label": "Rochester, NY", "lonlat": (-77.61, 43.16), "count": 1},
    {"label": "Hartford y Manchester, CT", "label_en": "Hartford & Manchester, CT", "lonlat": (-72.6, 41.77), "count": 2},
    {"label": "Stamford, CT", "lonlat": (-73.54, 41.05), "count": 1},
    {"label": "Nueva York, NY", "label_en": "New York City, NY", "lonlat": (-73.92, 40.74), "count": 10},
    {"label": "Norte de Nueva Jersey", "label_en": "Northern New Jersey", "lonlat": (-74.3, 40.66), "count": 2},
    {"label": "Philadelphia, PA", "lonlat": (-75.03, 40.04), "count": 1},
    {"label": "Orange Park, FL", "lonlat": (-81.71, 30.17), "count": 1},
    {"label": "Ocala, FL", "lonlat": (-82.14, 29.19), "count": 1},
    {"label": "Florida Central", "label_en": "Central Florida", "lonlat": (-80.75, 27.75), "count": 7},
    {"label": "Austin, TX", "lonlat": (-97.74, 30.27), "count": 1},
    {"label": "Ceiba, Puerto Rico", "lonlat": (-65.65, 18.26), "count": 1},
]
MAP_STATES = [  # light state labels so the map reads as the U.S.
    ("NY", -75.6, 42.7), ("PA", -77.5, 40.9),
    ("FL", -83.6, 27.0), ("TX", -98.6, 31.4), ("GA", -83.6, 32.6),
    ("NC", -79.4, 35.6), ("VA", -78.6, 37.6), ("OH", -82.8, 40.2),
]

# ------------------------------------------------------------------ affiliates
AFFILIATES = [
    {"group": {"es": "Iglesia Evangélica Discípulos de Jesucristo (IEDJ)",
               "en": "Iglesia Evangélica Discípulos de Jesucristo (IEDJ)"},
     "items": [
        ("Iglesia R.E.D. (Restaurados en Dios) IEDJ, Inc.", "41 Park St., Manchester, CT 06040"),
        ("Iglesia Evangélica Discípulos de Jesucristo Jehová Shalom", "142 Fairfield Ave., Hartford, CT 06114"),
        ("Iglesia Evangélica Discípulos de Jesucristo en Stamford", "164 Richmond Hill Ave., Stamford, CT 06902"),
        ("Iglesia Evangélica Discípulos de Jesucristo Rochester", "8 Ernst St., Rochester, NY 14621"),
        ("Iglesia La Familia Cristiana IEDJ", "880 E. 180th St., Bronx, NY 10460"),
        ("Iglesia Evangélica Discípulos de Jesucristo del Bronx", "692 Union Ave., Bronx, NY 10455"),
        ("Iglesia Evangélica Discípulos de Jesucristo Monte Hermón", "289 E. 3rd St., New York, NY 10009"),
        ("Iglesia Evangélica Discípulos de Jesucristo de Corona", "102-19 37th Ave., Corona, NY 11368"),
        ("Primera Iglesia Evangélica Discípulos de Jesucristo, Inc.", "135-16 Liberty Ave., South Richmond Hill, NY 11419"),
        ("Iglesia Cristiana Sinaí IEDJ", "58 Stanhope St., Brooklyn, NY 11221"),
        ("Primera Iglesia Evangélica Discípulos de Jesucristo de Brooklyn", "403 Legion St., Brooklyn, NY 11221"),
        ("Primera Misión Evangélica Discípulos de Jesucristo", "1111 East 2nd St., Plainfield, NJ 07060"),
        ("Iglesia Cristiana Templo de Adoración IEDJ", "475 Jersey Ave., Jersey City, NJ"),
        ("Primera Iglesia de Philadelphia IEDJ", "6513 Bustleton Ave., Philadelphia, PA 19149"),
        ("Templo Manahaím IEDJ", "395 Marigold Ave., Kissimmee, FL 34749"),
        ("Iglesia Faro de Esperanza IEDJ", "P.O. Box 65298, Orange Park, FL 32065"),
        ("IEDJ – Iglesia del Este Incorporado", "Ceiba, Puerto Rico"),
        ("IEDJ – Iglesia Fe y Esperanza", "Ocala, FL"),
     ]},
    {"group": {"es": "Iglesias M.I.", "en": "M.I. churches"},
     "items": [
        ("Latin Pentecostal Church of God Inc.", ""),
        ("Iglesia de Dios Pentecostal M.I. Arca de Salvación", ""),
        ("Iglesia Casa de Refugio M.I.", ""),
        ("Iglesia de Dios Pentecostal M.I. Ebenezer", ""),
        ("Iglesia de Dios Pentecostal M.I. Nueva Esperanza", ""),
        ("Iglesia Evangélica de Cristo Inc.", ""),
        ("Iglesia de Dios Pentecostal M.I. Rosa de Sarón", ""),
     ]},
    {"group": {"es": "Otros ministerios relacionados", "en": "Other related ministries"},
     "items": [
        ("Journey Church Inc.", "Fern Park, FL"),
        ("Christian Church The Way to Heaven", "Bronx, NY"),
        ("Iglesia La Buena Semilla", "New York, NY"),
        ("Iglesia Cristiana Príncipe de Paz", "Austin, TX"),
        ("Iglesia Cristiana Amamos a la Gente", "Orlando, FL"),
        ("Home Heroes Foundation Inc.", "Orlando, FL"),
        ("Fundación Ferdinand García", "Sanford, FL 32771"),
        ("Mayordomia.Net", "Ministerio en línea"),
        ("Movimiento La Red", "Orlando, FL"),
     ]},
]

# ------------------------------------------------------------------ documents
# Only files that survived the old backup intact are listed here.
DOCS = {
    "membership_app": "/documents/NCCMNApplicationForMembership.pdf",
    "spd": "/documents/NCCMNSPD.pdf",
}

ADMIN_DOCS = [
    {"title": {"es": "Modelo de reglamento (By-Laws) para iglesias", "en": "Sample church bylaws"},
     "desc": {"es": "Un documento base, recopilado de buenos ejemplos, para redactar la constitución y el reglamento de su iglesia.",
              "en": "A starting document, compiled from good examples, for drafting your church's constitution and bylaws."},
     "file": "/documents/ChurchBylawsExample.pdf", "lang": "en", "pages": 27},
    {"title": {"es": "Solicitud de membresía", "en": "Membership application"},
     "desc": {"es": "Llénela y envíela a apply@nccmn.org para comenzar el proceso de admisión.",
              "en": "Fill it in and send it to apply@nccmn.org to start the admission process."},
     "file": "/documents/NCCMNApplicationForMembership.pdf", "lang": "en", "pages": 7},
    {"title": {"es": "Descripción del Plan de Retiro Pastoral 403(b)", "en": "Clergy Retirement Plan 403(b) description"},
     "desc": {"es": "Elegibilidad, aportaciones y reglas del plan, en su versión del 1 de enero de 2019.",
              "en": "Eligibility, contributions and plan rules, as of January 1, 2019."},
     "file": "/documents/NCCMNSPD.pdf", "lang": "en", "pages": 9},
    {"title": {"es": "Carta constitutiva de una Comisión de Mayordomía", "en": "Stewardship Commission charter"},
     "desc": {"es": "Ejemplo de carta para organizar la comisión de mayordomía de la iglesia local.",
              "en": "A sample charter for organizing a local church stewardship commission."},
     "file": "/documents/crece/StewardshipCommissionCharter-IEDJ.pdf", "lang": "es", "pages": 7},
    {"title": {"es": "Resolución de conflictos", "en": "Conflict resolution"},
     "desc": {"es": "Guía para atender conflictos en la congregación y en las juntas.",
              "en": "A guide to handling conflict in the congregation and on boards."},
     "file": "/documents/crece/ConflictResolution_sm.pdf", "lang": "en", "pages": 6},
    {"title": {"es": "Cuestionario de estilos ante el conflicto", "en": "Conflict styles survey"},
     "desc": {"es": "Una herramienta breve para que líderes reconozcan cómo responden ante el conflicto.",
              "en": "A short tool to help leaders recognize how they respond to conflict."},
     "file": "/documents/crece/DaleCarnegieSurvey.pdf", "lang": "en", "pages": 2},
    {"title": {"es": "COVID-19: manejando el impacto", "en": "COVID-19: managing the impact"},
     "desc": {"es": "Material de la conferencia con Aura Consuelo Prieto sobre la familia y la iglesia durante la pandemia.",
              "en": "Handout from the talk with Aura Consuelo Prieto on family and church during the pandemic."},
     "file": "/documents/COVID-19-Manejando_el_Impacto.pdf", "lang": "es", "pages": 4},
]

CRECE_DOCS = [
    {"title": {"es": "Liderazgo 101 (presentación)", "en": "Liderazgo 101 (slides)"},
     "desc": {"es": "Taller del 4 de febrero de 2017, basado en el libro de John C. Maxwell.",
              "en": "Workshop from February 4, 2017, based on John C. Maxwell's book."},
     "file": "/documents/crece/Liderazgo101.pdf", "lang": "es", "pages": 104},
    {"title": {"es": "¿Por qué mueren las iglesias?", "en": "Why do churches die?"},
     "desc": {"es": "Qué factores llevan a una congregación a cerrar y cómo evitar ese deterioro. Diapositivas con notas.",
              "en": "What leads a congregation to close, and how to prevent that decline. Slides with notes."},
     "file": "/documents/crece/Autopsia_Slides_with_Notes.pdf", "lang": "es", "pages": 8},
    {"title": {"es": "Plan de predicación: 7 hábitos para el crecimiento espiritual", "en": "Preaching plan: 7 habits for spiritual growth"},
     "desc": {"es": "Siete sermones con texto, tema, propósito y diseño de cada uno.",
              "en": "Seven sermons, each with its text, theme, purpose and design."},
     "file": "/documents/crece/7_Habitos_Plan_Predicacion.pdf", "lang": "es", "pages": 1},
    {"title": {"es": "Primer sermón: Amistad con Dios (Juan 15.12-15)", "en": "First sermon: Friendship with God (John 15:12-15)"},
     "desc": {"es": "Para crecer espiritualmente es necesario tener una profunda amistad con Dios.",
              "en": "To grow spiritually we need a deep friendship with God."},
     "file": "/documents/crece/Amistad_con_Dios.pdf", "lang": "es", "pages": 8},
    {"title": {"es": "Folleto del programa CRECE", "en": "CRECE program brochure"},
     "desc": {"es": "El volante original de los talleres.", "en": "The original workshop flyer."},
     "file": "/documents/crece/Brochure_Volante_NCCMN_CRECE.pdf", "lang": "es", "pages": 1},
]

# Files that were cut off in the old backup. Put the originals in static/documents/
# and move each entry into the lists above to publish it again.
MISSING_DOCS = [
    "documents/CashManagementProcedureGenericNCCMN.pdf",
    "documents/UnMomentoParaMayordomía.pdf",
    "documents/NCCMN_Guia_de_Reapertura.pdf",
    "documents/DIPLOMADO_PREVENCION_DE_VIOLENCIA.pdf",
    "documents/2017_05MinistryTech.pdf",
    "documents/NCCMNEvangelismoModerno/EvangelismoModerno-UnaPresentacionDeNCCMN.pdf",
    "documents/NCCMNEvangelismoModerno/ModernEvangelism-NCCMNPresentation.pdf",
    "crece/Leadership101.pdf",
    "crece/Crece_2017-Excelencia-Boards.pdf",
    "crece/CRECE-MayordomiaUnEstiloDeVida-Handouts.pdf",
    "crece/Mayordomia_en_el_Siglo_XXI_Nuevos_corrientes_y retos_Handouts_with_Notes.pdf",
    "CINEFORO/* (all film-forum presentations)",
]

CINE_FORO = [
    {"film": "Belleza colateral", "q": {"es": "¿Qué significa la pérdida? ¿Dónde está Dios en la pérdida?",
                                        "en": "What does loss mean? Where is God in loss?"}},
    {"film": "Avatar", "q": {"es": "¿Cómo cambiaría nuestra teología ante el descubrimiento de vida en otros planetas?",
                             "en": "How would our theology change if we found life on other planets?"}},
    {"film": "Twilight", "q": {"es": "Los elementos teológicos de una serie vendida como romance.",
                               "en": "The theological elements of a series sold as romance."}},
    {"film": "The Blind Side", "q": {"es": "El ayuno que Dios escogió (Isaías 58) y el juicio de las naciones (Mateo 25).",
                                     "en": "The fast God chose (Isaiah 58) and the judgment of the nations (Matthew 25)."}},
    {"film": "The Book of Eli", "q": {"es": "El fin del mundo en el cine y en las Escrituras.",
                                      "en": "The end of the world on screen and in Scripture."}},
    {"film": "Zootopia", "q": {"es": "¿Qué significa ser justo? ¿Cómo expresamos la justicia en tiempos injustos?",
                               "en": "What does it mean to be just? How do we practice justice in unjust times?"}},
]

LINKS = [
    {"name": "Iglesia Evangélica Discípulos de Jesucristo (IEDJ)", "href": "https://www.iedj.org",
     "desc": {"es": "Concilio de iglesias afiliadas a EMM.", "en": "Council of churches affiliated with EMM."}},
    {"name": "Movimiento La Red", "href": "https://movimientolared.com",
     "desc": {"es": "Ministerio relacionado con sede en Orlando, Florida.", "en": "Related ministry based in Orlando, Florida."}},
    {"name": "Red Educativa Genesaret", "href": "https://rededucativagenesaret.com",
     "desc": {"es": "Formación ministerial en español.", "en": "Ministerial education in Spanish."}},
    {"name": "Seminario Teológico Gordon-Conwell – Programa de Ministerios Hispanos",
     "href": "https://drpablojimenez.com/2017/09/29/como-solicitar-admision-al-programa-de-ministerios-hispanos-de-gcts/",
     "desc": {"es": "Cómo solicitar admisión al programa (HMP), explicado por el Dr. Pablo Jiménez.",
              "en": "How to apply to the Hispanic Ministries Program (HMP), explained by Dr. Pablo Jiménez."}},
    {"name": "drpablojimenez.com", "href": "https://drpablojimenez.com",
     "desc": {"es": "Recursos de predicación y liderazgo del Dr. Pablo A. Jiménez.",
              "en": "Preaching and leadership resources from Dr. Pablo A. Jiménez."}},
]

# ------------------------------------------------------------------ video library
# All talks are by Rev. Dr. Pablo A. Jiménez unless noted. "yt" = YouTube id, "vimeo" = Vimeo id.
VIDEO_COLLECTIONS = [
    {"id": "como-predicar", "title": {"es": "Cómo predicar", "en": "How to preach"}, "lang": "es",
     "intro": {"es": "Las partes del sermón, paso a paso.", "en": "The parts of a sermon, step by step."},
     "videos": [
        ("La introducción del sermón", "yt", "LZAHJfskEcE"),
        ("Tipos básicos de sermones cristianos", "yt", "cY9vTt7OKjg"),
        ("Cómo predicar el Credo Apostólico", "yt", "ptkJrtTljIk"),
        ("El título del sermón", "yt", "ANY5VpLDvxc"),
        ("El bosquejo del sermón", "yt", "dD7qj1XYlIw"),
        ("El propósito del sermón", "yt", "fcPTg2Dmbyw"),
        ("La conclusión del sermón", "yt", "mEzInyxtPFs"),
     ]},
    {"id": "comunicacion", "title": {"es": "Comunicación y predicación", "en": "Communication and preaching"}, "lang": "es",
     "intro": {"es": "Siete principios de comunicación aplicados a la predicación.",
               "en": "Seven communication principles applied to preaching."},
     "videos": [
        ("Cómo interpretar la Biblia para hacer una prédica: el método de los tres pasos", "yt", "8qjNOEDizbI"),
        ("Conceptos homiléticos básicos", "yt", "4MsOjYxqDsw"),
        ("Nuevos horizontes en la predicación", "yt", "PqoLcbbHbDg"),
        ("Cómo presentar un sermón efectivo", "yt", "OJoGCayBWpo"),
        ("Interpretación bíblica para la predicación", "yt", "HBiDBChZgls"),
        ("Vocabulario homilético básico", "yt", "XWw8hKk-xeg"),
        ("Fuentes teológicas y sociales de la predicación", "yt", "02nEfW46fGg"),
     ]},
    {"id": "sermon-narrativo", "title": {"es": "El sermón narrativo", "en": "The narrative sermon"}, "lang": "es",
     "intro": {"es": "Predicación y homilética narrativa.", "en": "Narrative preaching and homiletics."},
     "videos": [
        ("Predicación y homilética narrativa, primera parte", "yt", "dPcgBr6xOtI"),
        ("Predicación y homilética narrativa, segunda parte", "yt", "TfNqBcYwsUk"),
        ("Los dones espirituales", "yt", "fwhfWw8SDGU"),
        ("Los frutos del Espíritu", "yt", "XmT0ChOGmUQ"),
     ]},
    {"id": "renueve", "title": {"es": "Renueve su predicación", "en": "Renew your preaching"}, "lang": "es",
     "intro": {"es": "Teología de la predicación, ocasiones especiales e introducciones a libros bíblicos.",
               "en": "Theology of preaching, special occasions and introductions to biblical books."},
     "videos": [
        ("Cómo renovar su predicación: primera parte", "yt", "q1A-L9oAOIE"),
        ("Teología de la predicación, primera parte", "yt", "c2ovsq0pdP0"),
        ("Teología de la predicación, segunda parte", "yt", "1U6EblRT9mc"),
        ("Cómo predicar la Navidad", "yt", "hATA81re4SY"),
        ("El sermón de ocasión especial: bodas y funerales", "yt", "egzs7M41psw"),
        ("Hebreos: introducción a la Epístola a los Hebreos", "yt", "Nfj0RZCy2xU"),
        ("Epístolas petrinas: introducción a 1 Pedro, 2 Pedro y Judas", "yt", "SP4LvQ0nzeg"),
        ("Santiago: introducción a la Epístola general de Santiago", "yt", "G0uyzQlOI-4"),
        ("Apocalipsis: introducción al Apocalipsis y a la literatura apocalíptica", "yt", "qghfDyOo6qc"),
        ("Predicación cibernética: la predicación ante los desafíos de la tecnología", "yt", "uRGj7kwaSEY"),
        ("Oración y ayuno (Isaías 58.6-12)", "yt", "zs00K_yzY0E"),
     ]},
    {"id": "liderazgo", "title": {"es": "Liderazgo cristiano", "en": "Christian leadership"}, "lang": "es",
     "intro": {"es": "Jesús como modelo de líder, visión y misión.", "en": "Jesus as a model leader, vision and mission."},
     "videos": [
        ("Jesús de Nazaret: el modelo del líder", "yt", "u40JW5lnBvU"),
        ("El modelo del líder (conferencia)", "yt", "Ro5JqWpzzQ8"),
        ("El liderazgo: una definición y perspectiva cristiana", "yt", "ceCknxYkur0"),
        ("Teología bíblica del liderazgo", "yt", "ycQk6gmRBJE"),
        ("Evangelización cibernética", "yt", "94TQryYY0bs"),
        ("Cómo desarrollar un proceso de visión", "yt", "HedqhV9ARlQ"),
        ("Bases bíblicas y teológicas de la misión cristiana", "yt", "7Eg6mLSPSNA"),
     ]},
    {"id": "cuidado-pastoral", "title": {"es": "Mentoría y cuidado pastoral", "en": "Mentoring and pastoral care"}, "lang": "es",
     "intro": {"es": "Cómo servir como mentor a los demás y atender situaciones difíciles.",
               "en": "Serving as a mentor and caring for people in hard situations."},
     "videos": [
        ("Cómo manejar conflictos en la iglesia", "yt", "eneLgNECGNw"),
        ("La violencia doméstica: una perspectiva cristiana", "yt", "FdGBbqE5h2M"),
        ("Desafíos contemporáneos al ministerio pastoral", "yt", "Yo7TDCGRY5E"),
        ("El asesoramiento pastoral en perspectiva sistémica", "yt", "SG8mZjFl4u0"),
     ]},
    {"id": "educacion-cristiana", "title": {"es": "Pasión por la educación cristiana", "en": "A passion for Christian education"}, "lang": "es",
     "intro": {"es": "La educación en la iglesia local y una introducción al mundo de la Biblia.",
               "en": "Education in the local church and an introduction to the world of the Bible."},
     "videos": [
        ("El propósito de la educación cristiana", "yt", "dJ2F_FnU0-4"),
        ("La educación cristiana en la iglesia local, primera parte", "yt", "XZPormkIVZQ"),
        ("La educación cristiana en la iglesia local, segunda parte", "yt", "SM98F1Xx78E"),
        ("La educación cristiana en la iglesia local, tercera parte", "yt", "WLUBtd7ADtU"),
        ("El mundo de la Biblia", "yt", "RiGDjS7jEVs"),
        ("La Biblia: apuntes introductorios", "yt", "8KIx1fjvk8A"),
        ("La geografía de Israel", "yt", "t2avg4Jswj0"),
        ("Historia de Israel", "yt", "FDtyNownt9I"),
        ("El intertestamento y los tiempos de Jesús", "yt", "QOyN6r5laCM"),
        ("Jesús de Nazaret: aspectos teológicos", "yt", "NXGVa193IeI"),
        ("Jesús de Nazaret: aspectos históricos", "yt", "4b1d3PE3g24"),
        ("Entorno del Nuevo Testamento I: la economía romana", "yt", "vTEbK_UGMW4"),
        ("Entorno del Nuevo Testamento II: el orden social romano", "yt", "FA3PIiaQ3fU"),
        ("Entorno del Nuevo Testamento III: sociedad y religión romana", "yt", "odP_39Gm0WI"),
        ("El ministerio de la palabra escrita (conferencia de Justo L. González)", "yt", "GuxNj2jGWoY"),
     ]},
    {"id": "teologia", "title": {"es": "Conceptos teológicos", "en": "Theological concepts"}, "lang": "es",
     "intro": {"es": "Introducción a la teología.", "en": "An introduction to theology."},
     "videos": [
        ("¿Qué es la teología? Introducción a la teología 1", "yt", "xmIk-5A76Bs"),
        ("De la escuela bíblica a la escuela de teología", "yt", "nUKfuGYs0xk"),
        ("¿Qué es el quehacer teológico?", "yt", "gxHF3LpxYBU"),
        ("La teología paulina: claves para la interpretación", "yt", "IfbzWF70Vb4"),
     ]},
    {"id": "vida-congregacional", "title": {"es": "Vida congregacional", "en": "Congregational life"}, "lang": "es",
     "intro": {"es": "El ciclo de vida de la congregación, la niñez, la juventud y el crecimiento integral.",
               "en": "The congregation's life cycle, children, youth and whole-life growth."},
     "videos": [
        ("Cómo desarrollar ministerios infantiles en la iglesia", "yt", "i4Jrt3KEVAI"),
        ("Desafíos contemporáneos al ministerio con la niñez y con la juventud", "yt", "mZvWX4Hs65U"),
        ("La espiritualidad en tiempos de incertidumbre", "yt", "GCzeBkwcNi8"),
        ("Crecimiento integral: desafío para la iglesia en el siglo XXI", "yt", "jdB-wM6MIlE"),
        ("¿Por qué mueren las iglesias?", "yt", "Skvz5qZrAMc"),
     ]},
    {"id": "revitalization", "title": {"es": "Revitalización de la iglesia (en inglés)", "en": "Church revitalization"}, "lang": "en",
     "intro": {"es": "Charlas en inglés sobre la iglesia en declive, la iglesia que florece y el poder de la visión.",
               "en": "Talks on the declining church, the thriving church and the power of a vision."},
     "videos": [
        ("Revitalize your Church", "vimeo", "105399834"),
        ("The Declining Church", "vimeo", "105349067"),
        ("The Thriving Church", "vimeo", "105349546"),
        ("The Power of a Vision, part 1", "yt", "eabUqLShUcs"),
        ("The Power of a Vision, part 2", "yt", "COXC5hUJ9ys"),
        ("Ubuntu: a bilingual sermon", "yt", "-0qCepWQ8Dw"),
     ]},
]


def video_count():
    return sum(len(c["videos"]) for c in VIDEO_COLLECTIONS)


# ------------------------------------------------------------------ articles
# Bodies live in content/articles/<slug>.html and stay in their original language.
ARTICLES = [
    {"slug": "padre-nuestro-dia-1",
     "file": "a-journey-from-worry-to-confident-hope-praying-through-the-lords-prayer",
     "title": "A Journey From Worry to Confident Hope: Praying Through the Lord’s Prayer",
     "series": "lords-prayer", "day": 1, "date": "2020-09-13", "author": "Manuel Collazo", "lang": "en"},
    {"slug": "padre-nuestro-dia-2",
     "file": "a-journey-from-worry-to-confident-hope-praying-through-the-lords-prayer-day-2",
     "title": "Day 2: Our Father", "series": "lords-prayer", "day": 2, "date": "2020-09-14", "author": "Manuel Collazo", "lang": "en"},
    {"slug": "padre-nuestro-dia-3",
     "file": "a-journey-from-worry-to-confident-hope-praying-through-the-lords-prayer-day-3",
     "title": "Day 3: May Your Kingdom Come", "series": "lords-prayer", "day": 3, "date": "2020-09-15", "author": "Manuel Collazo", "lang": "en"},
    {"slug": "padre-nuestro-dia-4",
     "file": "a-journey-from-worry-to-confident-hope-praying-through-the-lords-prayer-day-4",
     "title": "Day 4: Give Us Today the Bread We Need Now", "series": "lords-prayer", "day": 4, "date": "2020-09-16", "author": "Manuel Collazo", "lang": "en"},
    {"slug": "padre-nuestro-dia-5",
     "file": "a-journey-from-worry-to-confident-hope-praying-through-the-lords-prayer-day-5",
     "title": "Day 5: Forgive Us the Things We Owe", "series": "lords-prayer", "day": 5, "date": "2020-09-17", "author": "Manuel Collazo", "lang": "en"},
    {"slug": "padre-nuestro-dia-6",
     "file": "a-journey-from-worry-to-confident-hope-praying-through-the-lords-prayer-day-6",
     "title": "Day 6: Don’t Bring Us into the Great Trial, but Rescue Us from Evil", "series": "lords-prayer", "day": 6, "date": "2020-09-18", "author": "Manuel Collazo", "lang": "en"},
    {"slug": "padre-nuestro-dia-7",
     "file": "a-journey-from-worry-to-confident-hope-praying-through-the-lords-prayer-day-7",
     "title": "Day 7: The Kingdom, the Power, and the Glory", "series": "lords-prayer", "day": 7, "date": "2020-09-19", "author": "Manuel Collazo", "lang": "en"},
    {"slug": "the-three-steps", "file": "the-three-steps-biblical-interpretation-for-preaching",
     "title": "The Three Steps: Biblical Interpretation for Preaching", "series": None, "date": "2014-09-12",
     "author": "Rev. Dr. Pablo A. Jiménez", "lang": "en"},
    {"slug": "have-you-noticed", "file": "have-you-noticed", "title": "Have You Noticed?", "series": None,
     "date": "2014-09-02", "author": "Manuel Collazo", "lang": "en"},
    {"slug": "missing-ingredients", "file": "missing-ingredients", "title": "Missing Ingredients", "series": None,
     "date": "2014-08-26", "author": "Manuel Collazo", "lang": "en"},
    {"slug": "a-proclamation", "file": "a-proclamation", "title": "A Proclamation of Thanksgiving (1863)", "series": None,
     "date": "2014-08-26", "author": "Manuel Collazo", "lang": "en"},
]

SERIES = {"lords-prayer": {"es": "Del afán a la esperanza: orando el Padre Nuestro (7 días)",
                           "en": "From Worry to Confident Hope: praying the Lord’s Prayer (7 days)"}}

MONTHS = {"es": ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto",
                 "septiembre", "octubre", "noviembre", "diciembre"],
          "en": ["January", "February", "March", "April", "May", "June", "July", "August",
                 "September", "October", "November", "December"]}


def fmt_date(iso, lang):
    y, m, d = (int(x) for x in iso.split("-"))
    if lang == "es":
        return f"{d} de {MONTHS['es'][m-1]} de {y}"
    return f"{MONTHS['en'][m-1]} {d}, {y}"


def load_articles(folder: Path):
    out = []
    for a in ARTICLES:
        body = (folder / f"{a['file']}.html").read_text(encoding="utf-8")
        if a.get("day", 1) > 1:  # drop the repeated "Day N: ..." heading at the top of the body
            import re
            body = re.sub(r"^\s*<p><strong>\s*Day [^<]*</strong>\s*</p>\s*", "", body, count=1)
        out.append({**a, "body": body})
    # newest first, series days in order
    out.sort(key=lambda a: (a["date"]), reverse=True)
    for i, a in enumerate(out):
        a["prev"] = out[i + 1] if i + 1 < len(out) else None
        a["next"] = out[i - 1] if i > 0 else None
    return out

# ------------------------------------------------------------------ interface text
UI = {
    "es": {
        "skip": "Saltar al contenido",
        "menu": "Menú",
        "nav": [("about", "Nosotros"), ("churches", "Servicios"), ("join", "Únase"),
                ("resources", "Recursos"), ("training", "Formación"),
                ("reflections", "Reflexiones"), ("contact", "Contacto")],
        "give": "Donar",
        "switch": "English",
        "switch_label": "Read this page in English",
        "tagline": "Donde la administración está al servicio de la misión",
        "footer_about": "Organización sin fines de lucro exenta bajo la sección 501(c)(3) del Código de Rentas Internas. Los donativos son deducibles según la ley.",
        "footer_pages": "Páginas",
        "footer_contact": "Oficina central",
        "privacy": "Privacidad",
        "prayer": "Pedir oración",
        "services_nav": [("churches", "Para iglesias"), ("ministers", "Para ministros"),
                         ("exemption", "Exención 501(c)(3)"), ("retirement", "Plan de retiro")],
        "services_label": "Servicios",
        "in_english": "en inglés",
        "in_spanish": "en español",
        "pages": "págs.",
        "page": "pág.",
        "pdf": "PDF",
        "watch": "Ver en YouTube",
        "watch_vimeo": "Ver en Vimeo",
        "videos": "videos",
        "by": "Por",
        "prev": "Anterior",
        "next": "Siguiente",
        "all_reflections": "Todas las reflexiones",
        "article_lang_note": "Este artículo se publicó originalmente en inglés.",
        "lang_name": "Español",
    },
    "en": {
        "skip": "Skip to content",
        "menu": "Menu",
        "nav": [("about", "About"), ("churches", "Services"), ("join", "Join"),
                ("resources", "Resources"), ("training", "Training"),
                ("reflections", "Reflections"), ("contact", "Contact")],
        "give": "Give",
        "switch": "Español",
        "switch_label": "Leer esta página en español",
        "tagline": "Where administration serves the mission",
        "footer_about": "A nonprofit organization exempt under section 501(c)(3) of the Internal Revenue Code. Gifts are tax-deductible as allowed by law.",
        "footer_pages": "Pages",
        "footer_contact": "Main office",
        "privacy": "Privacy",
        "prayer": "Request prayer",
        "services_nav": [("churches", "For churches"), ("ministers", "For ministers"),
                         ("exemption", "501(c)(3) exemption"), ("retirement", "Retirement plan")],
        "services_label": "Services",
        "in_english": "in English",
        "in_spanish": "in Spanish",
        "pages": "pages",
        "page": "page",
        "pdf": "PDF",
        "watch": "Watch on YouTube",
        "watch_vimeo": "Watch on Vimeo",
        "videos": "videos",
        "by": "By",
        "prev": "Previous",
        "next": "Next",
        "all_reflections": "All reflections",
        "article_lang_note": "",
        "lang_name": "English",
    },
}
