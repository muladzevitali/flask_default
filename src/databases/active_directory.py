from dataclasses import dataclass, field
from typing import (Optional, List)

import ldap

from src.config import ldap as ldap_config


@dataclass(init=True)
class ActiveDirectory:
    email: str = field(default=ldap_config.email)
    password: str = field(default=ldap_config.password)
    protocol_version: int = field(default=3)

    def bind_connection(self, email: str, password: str) -> ldap.ldapobject.SimpleLDAPObject:
        """Bind ldap connection"""
        connection = ldap.initialize("ldap://bog.ge:389", bytes_mode=False)
        connection.protocol_version = self.protocol_version
        connection.set_option(ldap.OPT_REFERRALS, 0)
        connection.simple_bind_s(email, password)

        return connection

    def login_user(self, email: str, password: str) -> Optional[str]:
        """Login user into active directory"""
        try:
            connection = self.bind_connection(email=email, password=password)
            connection.unbind()
            return email
        except ldap.INVALID_CREDENTIALS:
            return None

    def search(self, filter_string: str) -> Optional[List[dict]]:
        """Search users information in AD"""
        result_data = list()
        try:
            connection = self.bind_connection(email=self.email, password=self.password)
            results = connection.search("DC=BOG,DC=GE",
                                        scope=ldap.SCOPE_SUBTREE,
                                        filterstr=f'(|(mail={filter_string}*)(displayName={filter_string}*))',
                                        attrlist=["displayName", "mail", "department", "mobile", 'title',
                                                  'manager', 'telephonenumber', 'physicaldeliveryofficename'])
            while True:
                search_type, search_data = connection.result(results, 0)
                if not len(search_data):
                    break
                if search_type == ldap.RES_SEARCH_ENTRY:
                    search_data = {key: value[0].decode() for key, value in search_data[0][1].items()}
                    result_data.append(search_data)

            connection.unbind()

            return result_data
        except ldap.INVALID_CREDENTIALS:
            print('None')
            return None


if __name__ == '__main__':
    ad = ActiveDirectory()
    search_results = ad.search('vitali')
    print(search_results)
