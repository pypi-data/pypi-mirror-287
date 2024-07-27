#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Contact :   liuyuqi.gov@msn.cn
@Time    :   2023/11/13 14:29:00
@License :   Copyright © 2017-2022 liuyuqi. All Rights Reserved.
@Desc    :   github api方式设置 Create or update a repository secret
'''

import requests
import json,sys
import base64

class GithubPulbicKey:
    ''' Github public key '''

    def __init__(self, key_id: str, key: str):
        self.key_id = key_id
        self.key = key


class GithubApi:
    ''' Github api '''

    _api_url = 'https://api.github.com'

    def __init__(self, owner: str, token: str, repo: str):
        self.owner = owner
        self.token = token
        self.repo = repo
        self.public_key = None
        self.sess = requests.Session()
        self.sess.headers.update({
            'Accept': 'application/vnd.github.v3+json',
            'X-GitHub-Api-Version': '2022-11-28',
            'Authorization': f'Bearer {self.token}'
        })

    def get_repo_public_key(self) -> GithubPulbicKey:
        ''' Get a repository public key 
        {
            "key_id": "012345678912345678",
            "key": "xx+dB7TJyvv1234"
        }
        '''
        url = f'{self._api_url}/repos/{self.owner}/{self.repo}/actions/secrets/public-key'
        response = self.sess.get(url)
        print(f'get public key response: {response.text}')
        if response.status_code == 200:
            res_json = response.json()
            self.public_key = GithubPulbicKey(
                res_json['key_id'], res_json['key'])
            return self.public_key
        else:
            print("Failed to get repository public key.")
            print(f"Response status code: {response.status_code}")
            print(f"Response body: {response.text}")
            return None
    
    @staticmethod
    def _base64encode(value):
        """

        :param value: byte, encrypted message
        :return: string
        """
        if sys.version_info <= (3, 1):
            return base64.encodestring(value).decode("utf-8")
        else:
            return base64.encodebytes(value).decode("utf-8")
        
    @staticmethod
    def encrypt_secret_value(value: str, public_key: str):
        ''' Value for your secret, encrypted with LibSodium using the public key retrieved from 
        the Get a repository public key endpoint.
        https://github.com/anna-money/workflow-tools/blob/8a94d18254183847d3706e5a610739b40b48c4e6/workflow_tools/secret.py#L63
          '''
        public_key_encoded = public.PublicKey(public_key.encode("utf-8"), encoding.Base64Encoder())
        sealed_box = public.SealedBox(public_key_encoded)
        encrypted = sealed_box.encrypt(value.encode("utf-8"))
        encrypted_string = GithubApi._base64encode(encrypted)

        # In Python 3.1+ base64.encodebytes inserts "\n" after every 76 bytes of output and
        # adds a trailing newline character to follow RFC 2045
        # https://docs.python.org/3/library/base64.html#base64.encodebytes
        # To make sure GitHub API accepts payload, remove "\n" from the encrypted value.
        result = encrypted_string.replace("\n", "")
        return result

    def set_update_github_secret(self, key: str, value: str):
        url = f'{self._api_url}/repos/{self.owner}/{self.repo}/actions/secrets/{key}'
        if self.public_key is None:
            self.get_repo_public_key()

        if self.public_key is not None:
            secret_value = self.encrypt_secret_value(
                value, self.public_key.key)
            data = {
                'encrypted_value': secret_value,
                'key_id': self.public_key.key_id
            }
            response = self.sess.put(url, json=data)
            if response.status_code == 204:
                print(f"GitHub secret: {key} updated successfully!")
            else:
                print("Failed to update GitHub secret.")
                print(f"Response status code: {response.status_code}")
                print(f"Response body: {response.text}")


if __name__ == '__main__':
    with open("account.json", "r") as file:
        data = json.load(file)
        owner = data["owner"]
        token = data["token"]
        repo = data["repo"]
        github_api = GithubApi(owner=owner, token=token, repo=repo)
        for i in range(data["secret"]):
            key = i["key"]
            value = i["value"]
            github_api.set_update_github_secret(key, value)
