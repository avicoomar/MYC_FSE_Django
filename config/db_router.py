"""
As of now this router is non-impactful because all migrations, reads, writes get routed only to "mysql_db" since the apps {"users", "auth", "admin", "sessions", "contenttypes"} are tightly coupled to each other. But future apps (having no relation to previously listed apps) can be put into non_core_apps or lightweight_apps as per the needs
Overview:
models of <core_apps> -------get routed to---------><mysql_db>
models of <non_core_apps> -------get routed to---------><someother_db>
models of <lightweight_apps> -------get routed to--------><sqlite_db>
"""
class DbRouter:

    core_apps = {"users", "auth", "admin", "sessions", "contenttypes"}
    non_core_apps = {}
    lightweight_apps = {}
    
    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.core_apps:
            return "mysql_db"
        if model._meta.app_label in self.non_core_apps:
            pass
        if model._meta.app_label in self.lightweight_apps:
            return "sqlite_db"
        return False

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.core_apps:
            return "mysql_db"
        if model._meta.app_label in self.non_core_apps:
            pass
        if model._meta.app_label in self.lightweight_apps:
            return "sqlite_db"
        return False

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.core_apps:
            return db == "mysql_db" 
        if app_label in self.non_core_apps:
            pass
        if app_label in self.lightweight_apps:
            return "sqlite_db"
        return False
    """
    def allow_relation(self, obj1, obj2, **hints):
        #Allow relations if a model in the core_apps is involved.
        if (obj1._meta.app_label in self.core_apps or obj2._meta.app_label in self.core_apps):
            return True
        return None
    """
