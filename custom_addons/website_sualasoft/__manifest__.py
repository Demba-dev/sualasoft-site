{
    "name": "Website Sualasoft",
    "version": "1.0",
    "category": "Website",
    "summary": "Personnalisation du site Sualasoft : pages, styles et assets.",
    "description": """
        Module pour gérer les pages Home, Services et Contact sur le site Sualasoft.
        Ajoute également les CSS, JS et images personnalisés pour le thème.
    """,
    "author": "Sualasoft",
    "website": "https://www.sualasoft.com",
    "depends": ["website"],
    "data": [
        "security/ir.model.access.csv",
        "data/service_data.xml",
        "data/blog_data.xml",
        "views/layout.xml",
        "views/footer.xml",
        "views/home.xml",
        "views/services.xml",
        "views/contact.xml",
        "views/contact_views.xml",
        "views/reference_views.xml",
        "views/reference_menus.xml",
        "views/reference_portal.xml",
        "views/legal.xml",
        "views/blog_views.xml",
        "views/blog_menus.xml",
        "views/blog.xml",
    ],
    "assets": {
        "web.assets_frontend": [
            "website_sualasoft/static/css/*",
            "website_sualasoft/static/js/*",
            "website_sualasoft/static/img/*",
        ],
    },
    "installable": True,
    "application": True,
    "license": "LGPL-3",
} # type: ignore
