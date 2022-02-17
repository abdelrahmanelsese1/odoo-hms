{
    'name': "hms",
    'summary': "this is our summary",
    'description': """
    this is the description
    """,

    'data': [
        'security/res_groups.xml',
        'security/ir.model.access.csv',
        'views/hms_patient_view.xml',
        'views/hms_department_view.xml',
        'views/hms_doctor_view.xml',
        'views/hms_log_history_view.xml',
        'views/crm_inherit_view.xml',
        'reports/report.xml',
        'reports/templates.xml',

    ],
    'depends': ['base', 'crm'],
}
