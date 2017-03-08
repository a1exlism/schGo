# -*- coding: utf-8 -*-

def test_check_list():
    ori = {
        'params': {
            'key_1': 'value_1',
            'key_2': 'value_2'
        },
        'tags': ['233', 'fun'],
        'users': [
            {'id': '1'}
        ]

    }

    test = {
        'params': {
            'key_1': 'value_1',
            'key_2': 'value_2'
        },
        'tags': ['233', 'fun', 'sb'],
        'users': [
            {'id': '1'},
            {'id': '2'},
            {'id': '3',
             'balance': 5}
        ]
    }

    def check_dict(test, ori):

        """
        check if all keys in test alse in ori recursively
        values of dict can be value, list or dict

        notice: items can't be set type

        :param test:
        :param ori:
        :return:
        """
        flag = True
        for _ in test:
            if _ not in ori:
                return False

            if isinstance(test[_], dict):
                flag = check_dict(test[_], ori[_])
                if flag is False:
                    break
            elif isinstance(test[_], list):
                for item in test[_]:
                    # assume ori[_] is list type now
                    if isinstance(item, dict):
                        flag = check_dict(item, ori[_][0])
                        if flag is False:
                            break
            elif isinstance(test[_], set):
                raise TypeError
        return flag

    assert check_dict(test, ori) is False, 'check_dict not work'


if __name__ == '__main__':
    test_check_list()
