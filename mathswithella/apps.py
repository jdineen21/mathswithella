from django.contrib.admin.apps import AdminConfig

class MathsWithEllaAdminConfig(AdminConfig):
    default_site = 'mathswithella.admin.MathsWithEllaAdminSite'