from Data.data import user_setting_dict

login_list = [user_setting_dict[key]['login'] for key in user_setting_dict.keys()]
print(login_list)
