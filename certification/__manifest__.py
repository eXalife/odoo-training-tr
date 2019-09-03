# Copyright 2014-2015 Grupo ESOC <www.grupoesoc.es>
# Copyright 2017-Apertoso N.V. (<http://www.apertoso.be>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    'name': 'Certification',
    'summary': "Defines certification for different purposes.",
    'author': "Eficent, Odoo Community Association (OCA)",
    'category': 'Certification Management',
    'version': '12.0.1.0.0',
    'license': 'AGPL-3',
    'depends': ['base'],
    'data': ['security/ir.model.access.csv',
             'views/certification_view.xml',
             'views/certification_bodies_view.xml',
             'views/certification_template_pdf.xml',
             'views/report_certification_pdf.xml',
             'views/res_partner.xml',
             'views/standard_view.xml'
             ],
    'demo': ['data/certification_data.xml'],
    'development_status': 'Beta',
    'maintainers': ['ceeficent']
}
