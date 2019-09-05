# Copyright 2014-2015 Grupo ESOC <www.grupoesoc.es>
# Copyright 2017-Apertoso N.V. (<http://www.apertoso.be>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    'name': 'Reservation',
    'summary': "Activity Facility Center Reservation",
    'author': "Eficent, Odoo Community Association (OCA)",
    'category': 'Reservation Management',
    'version': '12.0.1.0.0',
    'license': 'AGPL-3',
    'depends': ['base','hr'],
    'data': [
        'security/reservation_manager_group.xml',
        'security/ir.model.access.csv',
        'views/activity_view.xml',
        'views/activity_place_view.xml',
        'views/reservation_view.xml',
        'views/reservation_admin_view.xml'
             ],
    'demo': [],
    'application': True,
    'development_status': 'Alpha',
    'maintainers': ['cee']
}
