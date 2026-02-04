from admin import Admin


useradmin = Admin("Chams", "Kilowa", "chams@kilo.com", 1999, "tiznit")
useradmin.privileges.get_privileges().append("backdoor")
useradmin.privileges.privileges.append("feed back")
useradmin.show_privileges()
