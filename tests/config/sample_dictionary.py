test_config_dict = {'service': "astra",
                    'info': {'description': "Astra 4.0",
                             'contact': {'email': "sharmapuja689@gmail.com",
                                         'number': 3104}},
                    'title': "Astra API Documentation"
                    }
flattened_dict = {'service': 'astra',
                           'info.description': 'Astra 4.0',
                           'info.contact.email': 'sharmapuja689@gmail.com',
                           'info.contact.number': 3104,
                           'title': 'Astra API Documentation'}
