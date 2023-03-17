import frappe
import json 

def create_quota():
    frappe.db.sql(
			f"""
			CREATE TABLE if not exists `__eq_config` 
            (`id` INT DEFAULT 0,
            `users` INT DEFAULT 1,
            `active_users` INT DEFAULT 0,
            `space` INT DEFAULT 0,
            `db_space` INT DEFAULT 0,
            `company` INT DEFAULT 1,
            `used_company` INT DEFAULT 1,
            `count_website_users` INT DEFAULT 0,
            `count_administrator_user` INT DEFAULT 1,
            `valid_till` datetime(6),
            PRIMARY KEY (`id`))
			"""
		)

    # frappe.db.sql(f"""ALTER TABLE __eq_config ADD users INT(8) DEFAULT 1,active_users INT(8) DEFAULT 0, space INT(8) DEFAULT 0, db_space INT(8) DEFAULT 0,
    # company INT(8) DEFAULT 1, used_company INT(8) DEFAULT 1, count_website_users INT(8) DEFAULT 0,
    # count_administrator_users INT(8) DEFAULT 1""")
    # data = frappe.db.sql_ddl("""
	# 		create table if not exists `__eq_config` (
  	# 			`eq_id` int(8)  primary key,
	# 			`users` INT(8) DEFAULT 1,
  	# 			`active_users` INT(8) ,
	# 			`space` INT(8) DEFAULT 0,
	# 			`db_space` INT(8) DEFAULT 0,
	# 			`company` INT(8) NOT NULL DEFAULT 1,
    #           `used_company` INT(8) NOT NULL DEFAULT 1,
  	# 			`count_website_users` INT(8) DEFAULT 0 ,
    #           `count_administrator_user` INT(8) DEFAULT 1,
	# 		) ENGINE=InnoDB ROW_FORMAT=COMPRESSED CHARACTER SET=utf8mb4 COLLATE=utf8mb4_unicode_ci""")
    

def create_sys_config(doc,method=None):
    quota = frappe.get_site_config()['quota']    
    data = create_quota()
    frappe.msgprint(str(quota))
    frappe.msgprint(str(data))
    frappe.db.sql(f"""insert into `__eq_config` (users,active_users,
    space,db_space,company,used_company,count_website_users,count_administrator_user,valid_till)
	values (%s,%s,%s,%s,%s,%s,%s,%s,%s)""",(quota['users'],quota['active_users'],quota['space'],
    quota['db_space'],quota['company'],quota['used_company'],quota['count_website_users'],
    quota['count_administrator_user'],quota['valid_till']))
    