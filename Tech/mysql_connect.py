import os


def mysql_con(is_prod = 1):
    if is_prod == 0 :
        mysql_settings = {'user': 'ext_tolmachev_a',
                        #'password' : os.getenv('mysql_password'),
                        'password' : 'Pi*m4?nx1s|ZFH4AV}}f|WHBOJ#OF@~r',
                        'host' : '37.143.14.122',
                        'database' : '_dev_lendinvest'
                      }
    elif is_prod == 1:
        mysql_settings = {'user': 'ext_tolmachev_a',
                        #'password' : os.getenv('mysql_password'),
                        'password' : 'ZWY1MWMxNjc0MzVkN',
                        'host' : '91.218.231.34',
                        'database' : 'lendinvest'
                      }

    return mysql_settings
